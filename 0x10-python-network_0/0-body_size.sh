#!/bin/bash
# Displaying the results of GET method
curl -sI "$1" | grep -i 'Content-Length' | awk '{print $2}'
