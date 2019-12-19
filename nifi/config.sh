#!/bin/bash

ip=${1}
file=${2:-./nifi-1.10.0/conf/nifi.properties}

sed -i "/nifi.remote.input.host=/ s/nifi.remote.input.host=/nifi.remote.input.host=$1/" $2
