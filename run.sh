export FLASK_APP=src/WebApi.py

DATETIME=$(date +'%Y-%m-%d')
export LOGFILE="logs/${DATETIME}-log.log"

echo "$(date +'%Y-%m-%d %T') Creating log file $LOGFILE" >> $LOGFILE

echo "$(date +'%Y-%m-%d %T') Starting iot proccess." >> $LOGFILE

while :
do
  echo "$(date +'%Y-%m-%d %T') Git pulling." >> $LOGFILE
  git pull >> $LOGFILE
  echo "$(date +'%Y-%m-%d %T') Starting Flask server." >> $LOGFILE
  python -m flask run >> $LOGFILE
  echo "$(date +'%Y-%m-%d %T') Flask server stopped." >> $LOGFILE
  sleep 0.5
  echo "$(date +'%Y-%m-%d %T') Rebooting..." >> $LOGFILE
done
