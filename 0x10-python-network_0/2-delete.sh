#!/bin/bash
# script that sends a delete request to URL passed as first argument
# And displays body of the response
curl -X DELETE "$1"
