#!/bin/bash
# script that takes in a URL, sends request, and displays the size of body of the response
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2
