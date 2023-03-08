#!/bin/bash
# This script sends a GET request to input URL and displays the body of the response
curl -sL "$1" | grep -Eo '<.*>|^[^{]*$' # -s flag for silent mode, -L flag for automatically following redirects, |-E flag for using extended regular expressions in grep, -o flag for only printing matched string
