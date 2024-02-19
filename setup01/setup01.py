import os 

arr = ['13','14','15','34','35','36','65','66','68','113','114','115']
arr0 = ['14','15','35','36','66','68','114','115']
c = 1
for i in arr:
    print(i)
    os.system('ssh 10.10.100.%s date'%i)
    os.system('ssh 10.10.100.%s  \"screen -ls\"'%i)
    os.system('ssh 10.10.100.%s python3 --version'%i)
    os.system('ssh 10.10.100.%s python3 -m pip install flwr'%i)
    os.system('scp piknode-setup-reqs.sh 10.10.100.%s:/home/ubuntu'%i)

    #os.system('ssh 10.10.100.%s python3 -m pip install tensorflow'%i)
    #os.system('ssh 10.10.100.%s  \"git clone https://github.com/Kundjanasith/conventional_FL conventional_FL_NHFL_US\"'%i)
    #os.system('scp config.ini 10.10.100.%s:~/conventional_FL_NHFL_US/config.ini'%i)
    #os.system('scp trainer_main.py 10.10.100.%s:~/conventional_FL_NHFL_US/trainer_mode/main.py'%i)
    #os.system('scp aggregator_main.py 10.10.100.%s:~/conventional_FL_NHFL_US/aggregator_mode/main.py'%i)
    #os.system('ssh 10.10.100.%s  \"screen -ls\"'%i)
    #os.system('ssh -t 10.10.100.%s  \"screen -dmS t && screen -S t -X stuff \'cd ~/conventional_FL_NHFL_US/trainer_mode && python3 main.py\n\' \"'%i)
    #print(i,c) 
    #os.system('ssh 10.10.100.%s  \"screen -ls\"'%i)
    #c = c + 1
    ##for j in arr:
    #    os.system('ssh 10.10.100.%s \"ssh 10.10.100.%s\"'%(i,j))
