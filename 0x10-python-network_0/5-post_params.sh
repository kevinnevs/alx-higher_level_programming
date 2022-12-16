#!/bin/bash
# takes URL, sends a POST request to passed URL, and displays body response, variable email must be sent with "test@gmail.com", variable subject must be sent with "I will always be here for PLD"
curl -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
