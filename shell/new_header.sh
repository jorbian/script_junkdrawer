#!/bin/sh

NEW_HEADER_TEMPLATE="#ifndef _%s_\n#define _%s_\n%s\n#endif /* _%s_ */\n"
NEW_HEADER_PATH="./new.h"
NEW_HEADER_CODE="//"
NEW_HEADER_FILENAME="${NEW_HEADER_PATH##*/}"
NEW_HEADER_MACRO="$(printf $NEW_HEADER_FILENAME | tr '[a-z.]' '[A-Z_]')"

FILL_IN_BLANKS="$NEW_HEADER_MACRO $NEW_HEADER_MACRO $NEW_HEADER_CODE $NEW_HEADER_MACRO"

FILE_CONTENT=$(printf "$NEW_HEADER_TEMPLATE" $FILL_IN_BLANKS)

if ! (test -f "$NEW_HEADER_PATH"); then
    printf "$FILE_CONTENT" > $NEW_HEADER_PATH
fi