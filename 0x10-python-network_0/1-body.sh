#!/bin/bash
# GET method using curl
curl -sI "$1" | grep "HTTP/1.1 200 0K" >/dev/null && curl -s "$1"
