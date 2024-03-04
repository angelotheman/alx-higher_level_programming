#!/bin/bash
# POST method using curl
curl -so /dev/null -w "%{http_code}" "$1"
