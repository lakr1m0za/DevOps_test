#!/bin/bash
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y python3
sudo pip3 install notebook -y
sudo jupyter notebook
