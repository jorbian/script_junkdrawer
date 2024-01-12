#!/bin/sh

PREFIX=
SUFFIX=.py
BOILERPLATE="#!/usr/bin/python3\n\ndef %s():\n\tpass"

for ARG in "$@"; do
    FILENAME="$PREFIX$ARG$SUFFIX"
    CODE=$(printf "$BOILERPLATE" "$ARG")

    if test -f $FILENAME; then
        continue
    else
        printf '%s\n' "$CODE" > $FILENAME
    fi
done