@echo off

cd C:\Klasyk

for /f %%i in ('dir /b/a-d/od/t:c *.zip') do set LAST=%%i
echo =============================================================== >> c:\temp\backup.log
echo Poczatek backupu >> c:\temp\backup.log
date /t >> c:\temp\backup.log  2>&1
time /t >> c:\temp\backup.log  2>&1
echo Najnowszy plik backup Subiekta to %LAST% >> c:\temp\backup.log

REM echo open example.com.pl> ftpcmd.dat
REM echo user ftuser@example.com.pl>> ftpcmd.dat
REM echo mypasswrod>> ftpcmd.dat
REM echo cd bck_sub>> ftpcmd.dat
REM echo pwd>> ftpcmd.dat
REM echo put %LAST%>> ftpcmd.dat
REM echo quit>> ftpcmd.dat
REM ftp -n -s:ftpcmd.dat ftp.example.com.pl

echo open sftp://ftuser@example.com.pl:mypassword@example.com.pl> ftpcmd.dat
echo put C:\Klasyk\%LAST% /bck_sub/>> ftpcmd.dat
echo exit>> ftpcmd.dat

c:\skrypty\winscp.com /script=ftpcmd.dat /ini=nul
del ftpcmd.dat

date /t >> c:\temp\backup.log  2>&1
time /t >> c:\temp\backup.log  2>&1
echo Koniec backupu >> c:\temp\backup.log
