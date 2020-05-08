#!/bin/sh

# Expected to run in a machine with pandoc installed and addBorders.py in /app

if [ "$#" -lt 3 ]; then
    echo "Illegal number of arguments"
    exit 1
fi

MOUNTPOINT="/data/"
INPUT="$MOUNTPOINT$1"
OUTPUT="$MOUNTPOINT$2"
TEMPLATE="$MOUNTPOINT$3"

for file in $INPUT $TEMPLATE
do
    if [ ! -f "$file" ]; then
        echo "$file doesn't exist"
        exit 1
    fi
done

pandoc "$INPUT" -o "$OUTPUT" -s --reference-doc="$TEMPLATE"

python3 /app/addBorders.py "$OUTPUT"
