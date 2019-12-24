#!/bin/bash 

# Used for installing all dependencies
# Call with sudo

# install anaconda
curl -O https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
# might need to pipe 'yes' here...
bash Anaconda3-2019.03-Linux-x86_64.sh
# check if there is some user interaction needed...

# install pip
apt install python-pip

source ~/.basbrc

# install python requirements from pip
pip install -r requirements.txt
