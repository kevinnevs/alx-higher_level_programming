#!/bin/bash
# takes URL, sends a POST request to passed URL, and displays body response, with specified email and subject
curl -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
