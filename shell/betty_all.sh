#!/usr/bin/bash

FOLDER=$([ -n "$1" ] && echo "$1" || echo "$(pwd)")

C_FILES=($(find $FOLDER -name "*.[ch]" -type f -print))

for file in "${C_FILES[@]}"; do
   betty "$file"
done
