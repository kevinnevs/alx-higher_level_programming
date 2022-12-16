#!/bin/bash
# sends a delete request to URL passed as first argument and displays body of the response
curl -X DELETE "$1"
