#!/bin/bash
# POST method using curl
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
