import flwr as fl 
import tensorflow as tf 
import sys
from keras.utils import to_categorical
import glob
import random
import numpy as np
from keras.optimizers.legacy import SGD
import time 

name = sys.argv[1]

def load_dataset():
    (X_train, Y_train), (X_test, Y_test) = tf.keras.datasets.cifar10.load_data()
    X_train = X_train.astype('float32')
    X_test = X_test.astype('float32')
    X_train = X_train / 255.0
    X_test = X_test / 255.0
    Y_train = to_categorical(Y_train)
    Y_test = to_categorical(Y_test)
    return (X_train, Y_train), (X_test, Y_test)

(_, _), (x_test, y_test) = load_dataset()


def sampling_data():
    (x_train, y_train), (_, _) = load_dataset()
    print(len(x_train))
    num_of_each_dataset = 1000
    print(num_of_each_dataset)
    split_data_index = []
    while len(split_data_index) < num_of_each_dataset:
        item = random.choice(range(x_train.shape[0]))
        if item not in split_data_index:
            split_data_index.append(item)
    new_x_train = np.asarray([x_train[k] for k in split_data_index])
    new_y_train = np.asarray([y_train[k] for k in split_data_index])
    return new_x_train, new_y_train

model = tf.keras.applications.MobileNetV2((32, 32, 3), classes=10, weights=None)
# lr = 0.000025
lr = 0.015
OPTIMIZER = SGD(lr=lr, momentum=0.9, decay=lr/2, nesterov=False) # lr = 0.015, 67 ~ 69%
model.compile(OPTIMIZER, "categorical_crossentropy", metrics=["accuracy"])

class CifarClient(fl.client.NumPyClient):

    def __init__(self, name, log_before, log_after):
        self.name = name
        self.log_before = log_before
        self.log_after = log_after

    def get_parameters(self, config):
        return model.get_weights()

    def fit(self, parameters, config):
        model.set_weights(parameters)
        check_before = glob.glob('%s_localmodel_beforeTraining_ep*.h5'%(self.name))
        pathModel_before = '%s_localmodel_beforeTraining_ep%d.h5'%(self.name,len(check_before))
        check_after = glob.glob('%s_localmodel_afterTraining_ep*.h5'%(self.name))
        pathModel_after = '%s_localmodel_afterTraining_ep%d.h5'%(self.name,len(check_after))
        x_train, y_train = sampling_data()
        _, accuracy = model.evaluate(x_test, y_test)
        tn = time.time()
        self.log_before.write('%s,%d,%f\n'%(tn,len(check_before),accuracy))
        model.save_weights(pathModel_before)
        model.fit(x_train, y_train, epochs=5, batch_size=10)
        _, accuracy = model.evaluate(x_test, y_test)
        tn = time.time()
        self.log_after.write('%s,%d,%f\n'%(tn,len(check_after),accuracy))
        model.save_weights(pathModel_after)
        return model.get_weights(), len(x_train), {}

    # def evaluate(self, parameters, config):
    #     model.set_weights(parameters)
    #     loss, accuracy = model.evaluate(x_test, y_test)
    #     check_after = glob.glob('%s_localmodel_afterTraining_ep*.h5'%(self.name))
    #     tn = time.time()
    #     self.log.write('%s,%d,%f'%(tn,len(check_after),accuracy))
    #     return loss, len(x_test), {"accuracy": float(accuracy)}

file_b = open('log_%s_before.txt'%name,'w')
file_a = open('log_%s_after.txt'%name,'w')
client = CifarClient(name,file_b,file_a)
fl.client.start_client(server_address="[::]:8080", client=client.to_client())