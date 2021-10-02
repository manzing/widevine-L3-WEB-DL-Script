@echo off
mode con: cols=180

:start
echo #############################################################################
echo                               SCRIPT WEB-DL
echo #############################################################################
echo *
echo *      NOTE : La video portera le nom de votre fichier JSON   
echo *              
echo *****************************************************************************
echo *   !! Le fichier json doit etre dans le repertoire du script !!
echo *****************************************************************************
echo *
set /p key="Entrer le nom du fichier json (avec extension) :"

webdl.py -id -k "%key%"
pause
goto start