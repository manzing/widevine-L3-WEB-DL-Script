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
echo ** Pour utiliser des sous-titres externes (2 maxi), vos fichiers SRT doivent porter exactement le meme nom que le fichier JSON + "-FR" ou "-EN" 
echo ** et se situer dans le dossier du script.
echo **
echo ** Par defaut les langues sont FR et EN. Ex : video.json / video-FR.srt / video-EN.srt
echo **
echo ** Utiliser des sous-titres externes (.srt uniquement) ?
echo *
set /p es="> Tapez "1" pour charger des fichiers srt, sinon "0" puis "Entree" :"

if %es% ==1 (goto :ex_sub) else (goto :no_ex_sub)

:ex_sub
webdl.py -id -k "%key%" -es
pause
goto start

:no_ex_sub
webdl.py -id -k "%key%"
pause
goto start
