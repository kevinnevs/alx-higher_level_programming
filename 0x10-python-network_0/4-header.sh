#!/bin/bash
# takes in a URL as an argument, sends GET request to URL, and displays the body as response, header varaible X-School-User-Id must be sent with value 98
curl -sH "X-School-User-Id: 98" "$1"
