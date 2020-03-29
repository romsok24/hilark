#!/bin/bash
#
#  prune_dir - prune directory by deleting files if we are low on space
#
DIR=/kamery2TB
CAPACITY_LIMIT=90

echo -e "\nWykonuje na $(hostname)"

if [ "$DIR" == "" ]
then
    echo "ERROR: directory not specified"
    exit 1
fi

if ! cd $DIR
then
    echo "ERROR: unable to chdir to directory '$DIR'"
    exit 2
fi

if [ "$CAPACITY_LIMIT" == "" ]
then
    CAPACITY_LIMIT=95   # default limit
fi

let CAPACITY=$(df -k . | awk '{gsub("%",""); capacity=$5}; END {print capacity}')


if [ $CAPACITY -gt $CAPACITY_LIMIT ]
then
    #
    # Get list of files, oldest first.
    # Delete the oldest files until
    # we are below the limit. Just
    # delete regular files, ignore directories.
    #
    ls -rt | while read FILE
    do
        if [ -f $FILE ] || [ -d $FILE ]
        then
            if rm -fr $FILE
            then
                echo "Deleted $FILE"

                CAPACITY=$(df -k . | awk '{gsub("%",""); capacity=$5}; END {print capacity}')

                if [ $CAPACITY -le $CAPACITY_LIMIT ]
                then
                    # we're below the limit, so stop deleting
                    exit
                fi
            fi
        fi
    done
else
  echo -e "Nie trzeba czyscic $DIR. Zajetosc: $CAPACITY podczas gdy limit: $CAPACITY_LIMIT.\n"
fi
