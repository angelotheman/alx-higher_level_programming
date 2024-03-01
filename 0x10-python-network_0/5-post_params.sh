#!/bin/bash
# DELETE method using curl
curl -sX POST -d '{"email": "test@gmail.com", "subject": "I will always be here for PLD"}' -H "Content-Type: application/json" "$1"
