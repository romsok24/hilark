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
 /usr/bin/rsync -Prvl --timeout=120 --progress --update 10.9.0.6:/kamery2TB/2020-$(date +"%m")* /bck_monitoring/
 logger "RSYNC: wykonuje $i obieg kopii zdjec monitoringu"
done

if [ $i -eq $MAX_RETRIES ]
then
  echo "Hit maximum number of retries of rsync, giving up."
  logger "RSYNC: Osiagnalem maximum powtorzen. Koncze program"
fi



date

