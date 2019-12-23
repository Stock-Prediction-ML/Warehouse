#! /bin/bash

# Script for installing nifi on an EC2 instance
# Call this with sudo

apt update
apt upgrade

# install java 8 for nifi
apt install openjdk-8-jdk

# install nifi
wget https://archive.apache.org/dist/nifi/1.9.2/nifi-1.9.2-bin.tar.gz
tar xvf nifi-1.9.2-bin.tar.gz

# remove zipped file
rm -f nifi-*.tar.gz
