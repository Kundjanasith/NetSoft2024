import pandas as pd 
import os

df = pd.read_excel('PiK8kE_IP_allocation.xlsx')
print(df.head())

IPs = df['IP address base']
print(len(IPs))
df.dropna(subset=['IP address base'], inplace=True)
IPs = df['IP address base']
print(len(IPs))

def check_ping(hostname):
    response = os.system("ping -c 1 " + hostname)
    return response == 0

file_o = open('check_ping.csv','w')
file_o.write('IP,PING\n')
# for ip in IPs:
for i in range(256):
    ip = '10.10.100.%d'%i
    file_o.write(str(ip)+','+str(check_ping(ip))+'\n')
file_o.close()