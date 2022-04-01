#!/usr/bin/env bash

# Setup
set -e # exist if commands return non-zero exit status
set -u # treat unset variables as errors with param expansion

# Download words.txt file from the URL below
URL="https://raw.githubusercontent.com/AllenDowney/ThinkPython2/master/code/words.txt"

wget ${URL}

