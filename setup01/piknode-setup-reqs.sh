#!/bin/bash

function install_py
{
    sudo apt install -y software-properties-common
    sudo add-apt-repository -y ppa:deadsnakes/ppa
    sudo apt update -y
    sudo apt install -y python3.9 python3-pip virtualenv python-setuptools
    cd $1
    python3.9 -m venv .venv
    source .venv/bin/activate
    pip install setuptools tensorflow flwr

}

case $1 in
  install_py)
    install_py $2
    ;;
  *)
    echo "no match on input -> $1"
    ;;
esac