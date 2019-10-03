cls
@echo off
 
:Menu

ECHO.
ECHO ...............................................
ECHO PRESS 1, 2 OR 3 to select your task, or 4 to EXIT.
ECHO ...............................................
ECHO.
ECHO 1 - EMPTY
ECHO 2 - EMPTY
ECHO 3 - EMPTY
ECHO 4 - Exit
ECHO.
SET /P M=Type 1, 2, 3, or 4 then press ENTER:
IF %M%==1 GOTO option1
IF %M%==2 GOTO option2
IF %M%==3 GOTO option3
IF %M%==4 GOTO EOF

:option1
echo Add TEXT/COMMANDS
pause
GOTO Menu

:option2
echo ADD TEXT/COMMANDS
pause
GOTO Menu

:option3
pause
echo ADD TEXT/COMMANDS
GOTO Menu

:EOF
exit