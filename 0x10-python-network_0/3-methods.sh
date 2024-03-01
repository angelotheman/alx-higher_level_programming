#!/bin/bash
# DELETE method using curl
curl -sI "$1" | grep -i "Allow" | cut -d ' ' -f 2-
