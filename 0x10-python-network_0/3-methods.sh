#!/bin/bash
#Print all http methods accepted by server
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d" "
