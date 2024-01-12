#!/bin/sh

FOLDER_CONTENT=*
PREFIX="do_"

for FILE in $FOLDER_CONTENT; do
    mv $FILE $PREFIX$FILE
done
