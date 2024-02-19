echo US
ssh 10.10.100.13 date
ssh 10.10.100.14 date
ssh 10.10.100.15 date
echo JP
ssh 10.10.100.34 date
ssh 10.10.100.35 date
ssh 10.10.100.36 date
echo TH
ssh 10.10.100.65 date
ssh 10.10.100.66 date
ssh 10.10.100.68 date
echo PH
ssh 10.10.100.113 date
ssh 10.10.100.114 date
ssh 10.10.100.115 date

for i in 13 14 15 34 35 36 65 66 68 113 114 115
do 
    scp piknode-setup-reqs.sh 10.10.100.$i:/home/ubuntu/
    ssh 10.10.100.$i ./pik-node-setup-reqs.sh install_py /home/ubuntu/NetSoft2024
done

