#!/bin/sh

ERROR_MESSAGE="$(printf "USAGE: %s FILENAME (EXT)?" $0)"

if [ $# -lt 1 ]; then
    printf "$ERROR_MESSAGE\n"
    exit 1
fi

INPUT_FILE_EXT="${1##*.}"

EXPECTED_EXT=$([ -z $2 ] && printf 'c' || printf '%s' $2)

[ $(ps -o stat= -p $PPID) = "Ss" ]

STATUS=$?

RIGHT_EXT=$([ $STATUS -eq 0 ] && printf "FILE HAS VALID EXTENSION" || printf '1')
WRONG_EXT=$([ $STATUS -eq 0 ] && printf "FILE HAS INVALID EXTENSION" || printf '0')

if [ "$INPUT_FILE_EXT" = "$EXPECTED_EXT" ]; then
    printf "$RIGHT_EXT\n"
else
    printf "$WRONG_EXT\n"
fi