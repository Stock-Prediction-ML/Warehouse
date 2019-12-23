# NiFi

## Setup 

The following steps are required for NiFi setup on an EC2 instance

### Preconfiguration

Some settings are required in the AWS deployment stage.

* In 'Security Groups,' add a custom TCP rule to allow web connection to nifi
  * Type: Custom TCP Rule
  * Protocol: TCP
  * Port Range: 8080 (as example), remember this port
  * Source: Add your IP address (for example); do not allow all connections (0.0.0.0)

### Connect to Instance

With ssh

```bash
$ ssh -i <key_file>.pem ubuntu@<DNS_Name>
```

### Install

Clone this repo over http.

```bash
$ git clone https://github.com/sjmiller8182/Warehouse-Stock-Alternate.git
```

Run [`./install_nifi.sh`](./install_nifi.sh) as sudo to install nifi.

```bash
$ chmod +x ./Warehouse-Stock-Alternate/nifi/install_nifi.sh
$ sudo ./Warehouse-Stock-Alternate/nifi/install_nifi.sh
```
The install script installs the following

* java 8
* NiFi

### Configure and Restart

Configure nifi with the instance IP address

* `$ vi conf/nifi.properties`
* Set `nifi.remote.input.host` to the instance public IP address
* Save changes and close vi
* Restart NiFi by calling `./bin/nifi.sh restart`

```bash
$ sudo ./config.sh <IPv4 Public IP> ./nifi-1.9.2/conf/nifi.properties
```
### Connect

* Connect to NiFi UI
  * In a web browser connect to <Instance_IP_Address>:<Connection_Port>/nifi/
* Now NiFi should be up and running

### Summary

```bash
# connect and git scriptes
$ ssh -i <key_file>.pem ubuntu@<DNS_Name>
$ git clone https://github.com/sjmiller8182/Warehouse-Stock-Alternate.git
$ cd Warehouse-Stock-Alternate/nifi/

# install, configure, and start
$ chmod +x ./install_nifi.sh
$ sudo ./install_nifi.sh
$ sudo ./config.sh <IPv4 Public IP> ./nifi-1.9.2/conf/nifi.properties
$ sudo ./nifi-1.9.2/bin/nifi.sh restart
```

#### References

The following page(s) were used as references:

* http://ijokarumawak.github.io/nifi/2017/01/27/nifi-s2s-local-to-aws/

#### TODO

* Add a CLI command to create/terminate this instance
