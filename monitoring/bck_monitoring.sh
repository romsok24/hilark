#/bin/bash

cat /dev/null > /tmp/bck_monitoring.log
exec > /tmp/bck_monitoring.log
exec 2>&1

# Trap interrupts and exit instead of continuing the loop
trap "echo Exited!; exit;" SIGINT SIGTERM

MAX_RETRIES=50
i=0

# Set the initial return value to failure
false

while [ $? -ne 0 -a $i -lt $MAX_RETRIES ]
do
 i=$(($i+1))
 /usr/bin/rsync -Prvl --progress --update 10.x.y.z:/kamery2TB/$(date +"%y")-$(date +"%m")* /bck_monitoring/
done

if [ $i -eq $MAX_RETRIES ]
then
  echo "Hit maximum number of retries of rsync, giving up."
fi



date

