# Widevine-L3-WEB-DL-Script avec support de 2 pistes audios et sous-titres externes
Ce script permet de faire des WEB-DL de contenu L3 Widevine.

Le script original de Parnexcodes (merci à lui !) est ici :
https://github.com/parnexcodes/widevine-L3-WEB-DL-Script

Ce script modifier ajoute le support de choisir entre une ou 2 pistes audio, dont la 1ère eest considérée comme FR (pour que les tags MKV soient corrects).

Le fichier Download_FR.bat permet d'utiliser facilement le script.

L'intérêt de ces modifications est de permettre la préparation de plusieurs fichiers json (video1.json, video2.json...) ainsi que les subs correspondants si besoin et d'enchainer plus facilement les téléchargements. Ce n'est toutefois pas automatisé car il faut choisir les langues et qualités des flux.

Notez bien que je ne suis pas développeur, n'attendez rien de révolutionnaire :)

## Installation
### Prérequis
* Python et pip (pip est intégré à Python désormais)
https://www.python.org/downloads/

* pyfiglet
  * `pip install pyfiglet`
* rich
  * `pip install rich`

* Widevine Key Guesser (extension Chrome)
  * Télécharger le zip ici https://github.com/parnexcodes/widevine-l3-guesser-modified et décompressez le.
  * Activer le mode développeur dans les extensions Chrome
  * Utilisez "Charger l'extensions non empaquetée" pour charger l'extension et réglez Chrome pour la faire appraitre dans la barre d'outils.


### Récupérer les clés
Allez sur la page de la video à télécharger avec l'extension active, cliquez sur l'extension et télécharger le fichier en cliquant "Download" (keys.json).


## Nouveautés de ce script : 
* Support d'une ou plusieurs pistes audio.
* Nouvel argument ligne de commande -k pour indiquer le fichier json à charger. Vous pouvez ainsi préparer plusieurs fichiers json dans le dossier du script plutôt que remplacer à chaque fois le nom.
* Nouvel argument -es pour charger un fichier de sous-titres externe dans la video (SRT uniquement). Le fichier doit avoir le même nom que le fichier json.
* Les fichiers temporaires sont supprimés d'office à la fin de la fusion (sinon impossible d'enchainer un nouveau fichier).

### Usage

* Copier le fichier json et le sous-titres (optionnel) dans le répertoire du script.
* Lancez download_FR.bat et tapez le nom de vote fichier json. Ce nom sera utilisé pour nommer la vidéo.
  * ex : video.json créera un fichier video.mkv
* Choisissez si vous voulez charger des sous-titres externes (fichier SRT) en tapant "1" , sinon tapez 0 puis "entrée".
* Sélectionnez la qualité vidéo ou tapeez Entrée pour prendre automatiquement la meilleure disponible.
* Tapez l'ID de la piste FR
* Tapez l'ID de la piste English ou tapez Entrée pour ne pas charger de 2eme langue.
* Patientez pendant les download / decryption / fusion MKV
* Fini !

## Report Issues

Open Issue on Github if you get any problem.
