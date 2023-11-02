#!/usr/bin/bash

cd "$(dirname "$0")"

PROJECT_ROOT=$(realpath ..)
DEFAULT_OUTPUT_DIR="${PROJECT_ROOT}/lib"
SRC_FOLDER_NAME="${PROJECT_ROOT}/src"

GENERIC_MAKEFILE_NAME="staticlib.mk"
GENERIC_MAKEFILE_PATH="$(realpath $GENERIC_MAKEFILE_NAME)"

TARGET_LIB_NAME=$1
TARGET_LIB_DIR="${SRC_FOLDER_NAME}/${TARGET_LIB_NAME}"
TARGET_LIB_FILE="$TARGET_LIB_NAME.a"

raise_error() {
    # 1=DESCRIPTION OF THE ERROR
    # 2=EXIT CODE BASED ON 'sysexits.h' WITH WHICH TO CALL EXIT
    if [[ -z "$1" ]]; then
        MESSAGE="UNKNOWN ERROR"
    else
        MESSAGE=$1
    fi

    # defaults to base value for error messages
    if [[ -z "$2" ]]; then
        ERROR_NO=64
    else
        ERROR_NO=$2
    fi
    echo "$MESSAGE" >&2
    exit $ERROR_NO
}

bad_file() {
    # 1=ITEM WE WERE LOOKING FOR
    # 2=ITEM'S EXPECTED PATH
    if [[ -n $1 && -n $2 ]]; then
        echo "$1 '$2' WAS NOT FOUND."
    else
        raise_error
    fi
}

seeking_better_input() {
    # 1=INPUT PARAM WE NEEDED AND DIDN'T GET
    # 2=WHAT WE NEEDED IT FOR
    if [[ -n $1 && -n $2 ]]; then
        echo "ERROR: PLEASE PROVIDE $1 FOR $2."
    else
        raise_error
    fi
}

if [[ ($# -lt 1) || (! -d "$TARGET_LIB_DIR") ]]; then
    if [[ -n $1 ]]; then
        bad_file "ERROR: LIBRARY FOLDER" "../src/$TARGET_LIB_NAME"
    else
        echo "ERROR: NO INPUT PROVIDED"
    fi
    raise_error "$(seeking_better_input 'VALID FOLDER NAME' 'STATIC LIBRARY TO BE BUILT')" 66
fi

if [[ -z "$2" ]]; then
    OUTPUT_DIR=$DEFAULT_OUTPUT_DIR
else
    OUTPUT_DIR=$2
fi

mkdir -p $OUTPUT_DIR

OUTPUT_PATH="${OUTPUT_DIR}/${TARGET_LIB_FILE}"

if test -f "$OUTPUT_PATH"; then
    echo "A FILE CALLED '$TARGET_LIB_FILE' ALREADY EXITS IN OUTPUT LOCATION."

    read -p "WOULD YOU STILL LIKE TO CONTINUE (y/n)?" CONTINUE

    if ( shopt -s nocasematch; [[ ! (${CONTINUE} =~ ^([y]|yes)?$) ]]); then
        echo "ABORTING (RE)COMPILATION OF STATIC LIBRARY '$TARGET_LIB_FILE'."
        exit 0
    else
        echo "CONTINUING (RE)COMPILATION OF STATIC LIBRARY '$TARGET_LIB_FILE'."
    fi
fi

if [[ ! (-e $GENERIC_MAKEFILE_PATH) ]]; then
    echo "ERROR: $(bad_file 'GENERRIC MAKEFILE' $GENERIC_MAKEFILE_NAME)"
    raise_error "ERROR: $(seeking_better_input 'GENERRIC MAKEFILE' 'BUILDING A STATIC LIBRARY')" 66
fi

make --directory=$TARGET_LIB_DIR       \
     --makefile=$GENERIC_MAKEFILE_PATH \
     out_file=$OUTPUT_PATH          \
