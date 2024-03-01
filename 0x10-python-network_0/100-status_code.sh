#!/bin/bash
# POST method using curl
curl -sw "%{http_code}" -I "$1"
