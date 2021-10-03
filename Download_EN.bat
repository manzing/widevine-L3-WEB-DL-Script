@echo off
mode con: cols=180

:start
echo #############################################################################
echo                               SCRIPT WEB-DL
echo #############################################################################
echo *
echo *      NOTE : Output video will be using the same filename as the input json file   
echo *              
echo *****************************************************************************
echo *                !! json file MUST be in script directory !!
echo *****************************************************************************
echo *
set /p key="> Type the name of json file (with extension) :"
echo *
echo ** To use external sub, sub file must be a SRT and must have the same filename as json file **
echo ** 
echo > Use external sub ? (.srt file only) ?
echo *
set /p es="> Enter 1 to load a srt file, or type 0 :"

if %es% ==1 (goto :ex_sub) else (goto :no_ex_sub)

:ex_sub
webdl.py -id -k "%key%" -es
pause
goto start

:no_ex_sub
webdl.py -id -k "%key%"
pause
goto start
