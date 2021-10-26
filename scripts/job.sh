#!/bin/bash

CWD=$(pwd)

cd "$CWD" || exit

cd ..

python3 "$CWD/historybuffer.py"