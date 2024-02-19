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

scp set_NHFL.sh 10.10.100.13:~/
scp set_NHFL.sh 10.10.100.14:~/
scp set_NHFL.sh 10.10.100.15:~/

scp set_NHFL.sh 10.10.100.34:~/
scp set_NHFL.sh 10.10.100.35:~/
scp set_NHFL.sh 10.10.100.36:~/

scp set_NHFL.sh 10.10.100.65:~/
scp set_NHFL.sh 10.10.100.66:~/
scp set_NHFL.sh 10.10.100.68:~/

scp set_NHFL.sh 10.10.100.113:~/
scp set_NHFL.sh 10.10.100.114:~/
scp set_NHFL.sh 10.10.100.115:~/
