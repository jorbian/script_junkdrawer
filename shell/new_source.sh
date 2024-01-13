#!/bin/sh

INCLUDE_LINE="#include <%s>\n"
DEFAULT_HEADERS="stdio.h stdlib.h unistd.h"

HEADERS=""
for H_NAME in $DEFAULT_HEADERS; do
    H_LINE="$(printf "$INCLUDE_LINE" $H_NAME)"
    HEADERS="${HEADERS:+${HEADERS} }${H_LINE}"
done

FUNCTION_NAME="new"
FUNCTION_CODE="$(printf 'void %s(void)\n{\n\treturn;\n}\n\n' $FUNCTION_NAME)"


