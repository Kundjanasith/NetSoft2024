import pandas as pd 
import numpy as np

df = pd.read_csv('check_ping.csv')
print(df)
print(len(df))
x = np.unique(df['PING'])
print(x)
print(len(x))
dfx = df[df['PING']==True]
print(len(dfx))
print(dfx)

import subprocess
import platform

def test_latency(ip_address):
    # Define the command based on the operating system
    if platform.system().lower() == "windows":
        command = ["ping", "-n", "4", ip_address]
    else:
        command = ["ping", "-c", "4", ip_address]

    try:
        # Run the ping command
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        # Extract and return the average round-trip time from the output
        lines = result.stdout.split('\n')
        for line in lines:
            if "avg" in line.lower():
                return float(line.split('/')[4])
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None

# Example usage:
# ip_to_test = "8.8.8.8"  # Replace with the IP address you want to test
# average_latency = test_latency(ip_to_test)

# if average_latency is not None:
#     print(f"Average latency to {ip_to_test}: {average_latency} ms")
# else:
#     print(f"Unable to determine latency to {ip_to_test}")
file_o = open('check_bandwidth.csv','w')
file_o.write('IP,LATENCY\n')
for ip in dfx['IP']:
    print(ip)
    average_latency = test_latency(ip)
    file_o.write(str(ip)+','+average_latency+'\n')
file_o.close()