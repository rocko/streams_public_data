#!/bin/bash

# Run cronjob every 5 minutes
# */5 * * * *

CWD=$(pwd)

cd "$CWD" || exit

cd ..

python3 "$CWD/historybuffer.py"