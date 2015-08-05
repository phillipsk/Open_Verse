#!/bin/bash

pushd ~/Open_Verse/
sudo apt-get install -y mysql-server
mysql -u root -p
# enter MySQL

# exit MySQL
mysql -u root -p openVdev < Bible_ALL.sql
mysql -u openVuser -popenVpw openVdev
# Enter as created MySQL user and verify successful DB/User connection

# MySQL DB script
create database open-v-dev;