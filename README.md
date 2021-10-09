# widevine-L3-WEB-DL-Script with dual audio tracks support

### Version française ici :
https://github.com/manzing/widevine-L3-WEB-DL-Script/blob/French-English-V2/README_FR.md

This is a script created to WEB-DL L3 Widevine Content.



Original script by Parnexcodes (thanks for his work !) is here :
https://github.com/parnexcodes/widevine-L3-WEB-DL-Script

This modified script add proper support for 2 audio tracks (still allow a single track), intended for french and english (or other languages but MKV tracks tags would be incorrects so please modify the script / or resulting MKV as you need if you want to use another language).

A batch file is provided to make things easier and as "-id" argument is mandatory for dual audio tracks.

This branch will be more deeply modified and will (maybe) offer an easier command interface, and ability to prepare several download.
If possible, a beginning of automation support will be made.

Please note : I am not a developer at all, so don't expect anything great, this is just for fun :)

## How to install
### Requirements
* Python and pip
* Widevine Key Guesser
  * Download zip from https://github.com/parnexcodes/widevine-l3-guesser-modified
  * Activate developer mode in Chrome Extensions
  * Use "Load unpacked" to load the extracted extension folder
* pyfiglet
  * `pip install pyfiglet`
* rich
  * `pip install rich`

### Get the keys
Go to the protected stream you want to download. Activate the plugin (restart may be required after installing the extension) and download the extracted keys (keys.json).


## New in this script : 
* Support of dual audio tracks, support single track as you wish.
* New mandatory argument -k to specify the json file name. Why ? To allow to prepare several json files named according to each video. You don't have to prepare and reload the script each time.
* Using download.bat you have to type in the filename of your json file. This name will be used for the output video
 eg : mymovie.json will output a mymovie.mkv file
* With download.bat, -id argument is implicit and you have to choose video quality and audio track(s). 
* New argument -es allow loading of external subtitles that will be added to the mkv file. Support SRT files only and the sub MUST be named accordingly to the json file.
* Temporary files are deleted after merging.


![cmd exe](https://user-images.githubusercontent.com/2737265/135748724-7dd8fe3a-9890-4341-b79a-ac4181d1aec6.png) 


### Usage

* Copy json file and optionnal external srt file in the script folder.
* SRT files must be named as follow : video.json / video-FR.srt / video-EN.srt
* Launch Download.bat, type the name of json filename and type "1" if you want to add external srt
* Choose video quality or type Enter for best
* Choose French track first
* Choose English track or type enter to use a single audio track
* Wait for download / decryption / merging
* Done !

## Report Issues

Open Issue on Github if you get any problem.

