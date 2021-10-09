@echo off
mode con: cols=180

:start
echo #############################################################################
echo                               SCRIPT WEB-DL
echo #############################################################################
echo *
echo *      NOTE : Output video will use the same filename as the json input file   
echo *              
echo *****************************************************************************
echo *                !! json file MUST be in script directory !!
echo *****************************************************************************
echo *
set /p key="> Type the name of json file (with extension) :"
echo *
echo ** To use external sub (max 2), sub files must be a SRT and must have the same filename as json file + "-FR" or "-EN"  **
echo **
echo ** Subtitles files must be in script directory, like json file.
echo **
echo ** Default languages are FR and EN. Eg: video.json / video-FR.srt / video-EN.srt
echo ** 
echo * Use external sub ? (.srt file only) ?
echo *
set /p es="> Type "1" to load srt file(s), or type "0" and press "Enter" :"

if %es% ==1 (goto :ex_sub) else (goto :no_ex_sub)

:ex_sub
webdl.py -id -k "%key%" -es
pause
goto start

:no_ex_sub
webdl.py -id -k "%key%"
pause
goto start
