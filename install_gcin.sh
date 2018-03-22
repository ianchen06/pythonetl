#!/bin/sh
set -ex

sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 835AB0E3

cat <<EOF>>/etc/apt/sources.list
deb http://hyperrate.com/gcin-ubuntu1604 eliu release
EOF

sudo apt-get update && sudo apt-get install -y gcin
