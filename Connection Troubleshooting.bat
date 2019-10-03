cls
@echo off
 
:Menu

ECHO.
ECHO ...............................................
ECHO PRESS 1, 2 OR 3 to select your task, or 4 to EXIT.
ECHO ...............................................
ECHO.
ECHO 1 - Release/Renew
ECHO 2 - Flush all
ECHO 3 - Ping google
ECHO 4 - Exit
ECHO.
SET /P M=Type 1, 2, 3, or 4 then press ENTER:
IF %M%==1 GOTO option1
IF %M%==2 GOTO option2
IF %M%==3 GOTO option3
IF %M%==4 GOTO EOF

:option1
ipconfig /release
ipconfig /renew
pause
GOTO Menu

:option2
IPCONFIG /FLUSHDNS
NBTSTAT -R
NBTSTAT -RR
NETSH INT RESET ALL
NETSH INT IP RESET
NETSH WINSOCK RESET
pause
GOTO Menu

:option3
ping www.google.com
pause
GOTO Menu

:EOF
exit