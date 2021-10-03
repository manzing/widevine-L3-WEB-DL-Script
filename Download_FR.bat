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
set /p key="> Entrer le nom du fichier json (avec extension) :"
echo *
echo ** Pour utiliser des sous-titres externes, votre fichier SRT doit porter exactement le meme nom que le fichier JSON **
echo ** 
echo > Utiliser des sous-titres externes (.srt uniquement) ?
echo *
set /p es="> 1 pour charger un fichier srt, sinon 0 :"

if %es% ==1 (goto :ex_sub) else (goto :no_ex_sub)

:ex_sub
webdl.py -id -k "%key%" -es
pause
goto start

:no_ex_sub
webdl.py -id -k "%key%"
pause
goto start
