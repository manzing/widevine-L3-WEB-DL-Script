# widevine-L3-WEB-DL-Script with dual audio tracks support
This is a script created to WEB-DL L3 Widevine Content.

Original script by Parnexcodes (thanks for his work !) is here :
https://github.com/parnexcodes/widevine-L3-WEB-DL-Script

This modified script add proper support for 2 audio tracks, french and english (or other languages but MKV tracks tags would be incorrects so please modify the script as you need if you intend to use another audio).
A batch file is (or will be) provided to make things easier and as "-id" argument is mandatory for dual audio tracks.

Other branch will be more deeply modified and will (maybe) offer an easier command interface, and ability to prepare several download.
https://github.com/manzing/widevine-L3-WEB-DL-Script/tree/New-argument-for-input 

Please note : I am not a developer at all, so don't expect anything great, this is just for fun :)

## How to use
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

### Decode the video
Download the widevine-L3-WEB-DL-Script from here (Code -> Download zip). Copy the downloaded keys.json file to the same folder.

Run the downloader with `python webdl.py -o <name_without_extension>` from the folder you downloaded and extracted the script from.

The script will look in the keys.json file, starting from the second element in the JSON array. If the script can't find any keys, either modify the script (line 27 and 31), or the keys.json. See <https://gist.github.com/parnexcodes/74fef2e33a2171031000a97c371a1a65> for examples for some common use cases.

If there are multiple `mpd_url`s in the file and it isn't working, try changing them around. You can also change the `mpd_url` for a custom one if you have one.

### Options
-id and -s are optional (**id** to manually enter video and audio id from ytdl, **s** for subtitle url.). **Subtitle part is bugged right now**.

## Report Issues

Open Issue on Github if you get any problem.
