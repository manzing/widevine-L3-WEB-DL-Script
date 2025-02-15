import os
import os.path
import json
import subprocess
import argparse
import sys
import pyfiglet
from rich import print
from typing import DefaultDict

title = pyfiglet.figlet_format('WEBDL Script', font='slant')
print(f'[magenta]{title}[/magenta]')
print("by parnex")
print("Required files : yt-dlp.exe, mkvmerge.exe, mp4decrypt.exe, aria2c.exe\n")

arguments = argparse.ArgumentParser()
# arguments.add_argument("-m", "--video-link", dest="mpd", help="MPD url")
#arguments.add_argument("-o", '--output', dest="output", help="Specify output file name with no extension", required=True)
arguments.add_argument("-id", dest="id", action='store_true', help="use if you want to manually enter video and audio id.")
arguments.add_argument("-s", dest="subtitle", help="enter subtitle url")
arguments.add_argument("-es", dest="ex_subtitle", action='store_true', help="load external subtitle")
arguments.add_argument("-k", dest="key", help="Specify input keyfile name", required=True)
args = arguments.parse_args()

key = str(args.key)

with open (key) as json_data:
    config = json.load(json_data)
    json_mpd_url = config[0]['mpd_url']
    try:
        keys = ""
        for i in range(1, len(config)):
            keys += f"--key {config[i]['kid']}:{config[i]['hex_key']} "
    except:
        keys = ""
        for i in range(1, len(config)-1):
            keys += f"--key {config[i]['kid']}:{config[i]['hex_key']} "

currentFile = __file__
realPath = os.path.realpath(currentFile)
dirPath = os.path.dirname(realPath)
dirName = os.path.basename(dirPath)

youtubedlexe = dirPath + '/binaries/yt-dlp.exe'
aria2cexe = dirPath + '/binaries/aria2c.exe'
mp4decryptexe = dirPath + '/binaries/mp4decrypt_new.exe'
mkvmergeexe = dirPath + '/binaries/mkvmerge.exe'
SubtitleEditexe = dirPath + '/binaries/SubtitleEdit.exe'

# mpdurl = str(args.mpd)
output = str(args.key).replace(".json", "")
subtitle = str(args.subtitle)
ex_subFR = str(args.key).replace(".json", "-FR.srt")
ex_subEN = str(args.key).replace(".json", "-EN.srt")

if args.id:
    print(f'Selected MPD : {json_mpd_url}\n')    
    subprocess.run([youtubedlexe, '-k', '--allow-unplayable-formats', '--no-check-certificate', '-F', json_mpd_url])

    vid_id = input("\nEnter Video ID (or press Enter for best) : ")
    if vid_id == "":
            vid_id = "bv"
    audio_id = input("Enter French Audio ID : ")
    audio2_id = input("Enter English Audio ID or press Enter to ignore : ")
    subprocess.run([youtubedlexe, '-k', '--allow-unplayable-formats', '--no-check-certificate', '-f', audio_id, '--fixup', 'never', json_mpd_url, '-o', 'encrypted.m4a', '--external-downloader', aria2cexe, '--external-downloader-args', '-x 16 -s 16 -k 1M'])
    subprocess.run([youtubedlexe, '-k', '--allow-unplayable-formats', '--no-check-certificate', '-f', audio2_id, '--fixup', 'never', json_mpd_url, '-o', 'encrypted2.m4a', '--external-downloader', aria2cexe, '--external-downloader-args', '-x 16 -s 16 -k 1M'])
    subprocess.run([youtubedlexe, '-k', '--allow-unplayable-formats', '--no-check-certificate', '-f', vid_id, '--fixup', 'never', json_mpd_url, '-o', 'encrypted.mp4', '--external-downloader', aria2cexe, '--external-downloader-args', '-x 16 -s 16 -k 1M'])   

else:
    print(f'Selected MPD : {json_mpd_url}\n')
    subprocess.run([youtubedlexe, '-k', '--allow-unplayable-formats', '--no-check-certificate', '-f', 'ba', '--fixup', 'never', json_mpd_url, '-o', 'encrypted.m4a', '--external-downloader', aria2cexe, '--external-downloader-args', '-x 16 -s 16 -k 1M'])
    subprocess.run([youtubedlexe, '-k', '--allow-unplayable-formats', '--no-check-certificate', '-f', 'ba', '--fixup', 'never', json_mpd_url, '-o', 'encrypted2.m4a', '--external-downloader', aria2cexe, '--external-downloader-args', '-x 16 -s 16 -k 1M'])
    subprocess.run([youtubedlexe, '-k', '--allow-unplayable-formats', '--no-check-certificate', '-f', 'bv', '--fixup', 'never', json_mpd_url, '-o', 'encrypted.mp4', '--external-downloader', aria2cexe, '--external-downloader-args', '-x 16 -s 16 -k 1M'])    


print("\nDecrypting .....")
subprocess.run(f'{mp4decryptexe} --show-progress {keys} encrypted.mp4 decrypted.mp4', shell=True)  
subprocess.run(f'{mp4decryptexe} --show-progress {keys} encrypted.m4a decrypted.m4a', shell=True)
if os.path.isfile('encrypted2.m4a'):
    subprocess.run(f'{mp4decryptexe} --show-progress {keys} encrypted2.m4a decrypted2.m4a', shell=True)
else:
        pass



if args.subtitle:
    subprocess.run(f'{aria2cexe} {subtitle}', shell=True)
    os.system('ren *.ttml2 fr.ttml2')
    subprocess.run(f'{SubtitleEditexe} /convert fr.ttml2 srt', shell=True) 
    print("Merging .....")
    subprocess.run([mkvmergeexe, '--ui-language' ,'en', '--output', output +'.mkv', '--language', '0:eng', '--default-track', '0:yes', '--compression', '0:none', 'decrypted.mp4', '--language', '0:fr', '--default-track', '0:yes', '--compression' ,'0:none', 'decrypted.m4a', '--language', '0:eng', '--default-track', '0:no', '--compression' ,'0:none', 'decrypted2.m4a', '--language', '0:fr', '--track-order', '0:0,1:0,2:0,3:0,4:0', 'fr.srt'])
    print("\nAll Done .....")
      
else: 
        pass
        
if args.ex_subtitle:
  print("Merging .....")
  if os.path.isfile('decrypted2.m4a') and os.path.isfile(ex_subFR) and os.path.isfile(ex_subEN):
    subprocess.run([mkvmergeexe, '--ui-language' ,'en', '--output', output +'.mkv', '--language', '0:eng', '--default-track', '0:yes', '--compression', '0:none', 'decrypted.mp4', '--language', '0:fr', '--default-track', '0:yes', '--compression' ,'0:none', 'decrypted.m4a', '--language', '0:eng', '--default-track', '0:no', '--compression' ,'0:none', 'decrypted2.m4a', '--language', '0:fr', ex_subFR , '--track-order', '0:0,1:0,2:0,3:0,4:0', '--language', '0:eng', ex_subEN])
  
  elif os.path.isfile('decrypted2.m4a') and os.path.isfile(ex_subFR):
    subprocess.run([mkvmergeexe, '--ui-language' ,'en', '--output', output +'.mkv', '--language', '0:eng', '--default-track', '0:yes', '--compression', '0:none', 'decrypted.mp4', '--language', '0:fr', '--default-track', '0:yes', '--compression' ,'0:none', 'decrypted.m4a', '--language', '0:eng', '--default-track', '0:no', '--compression' ,'0:none', 'decrypted2.m4a', '--language', '0:fr','--track-order', '0:0,1:0,2:0,3:0,4:0', ex_subFR])
    
  elif os.path.isfile('decrypted2.m4a') and os.path.isfile(ex_subEN):
    subprocess.run([mkvmergeexe, '--ui-language' ,'en', '--output', output +'.mkv', '--language', '0:eng', '--default-track', '0:yes', '--compression', '0:none', 'decrypted.mp4', '--language', '0:fr', '--default-track', '0:yes', '--compression' ,'0:none', 'decrypted.m4a', '--language', '0:eng', '--default-track', '0:no', '--compression' ,'0:none', 'decrypted2.m4a', '--language', '0:eng','--track-order', '0:0,1:0,2:0,3:0,4:0', ex_subEN])      
  
  elif (not os.path.isfile('decrypted2.m4a')) and os.path.isfile(ex_subFR) and os.path.isfile(ex_subEN):
    subprocess.run([mkvmergeexe, '--ui-language' ,'en', '--output', output +'.mkv', '--language', '0:eng', '--default-track', '0:yes', '--compression', '0:none', 'decrypted.mp4', '--language', '0:fr', '--default-track', '0:yes', '--compression' ,'0:none', 'decrypted.m4a', '--language', '0:fr', ex_subFR , '--language', '0:eng','--track-order', '0:0,1:0,2:0,3:0,4:0', ex_subEN])
          
  elif (not os.path.isfile('decrypted2.m4a')) and os.path.isfile(ex_subEN):
    subprocess.run([mkvmergeexe, '--ui-language' ,'en', '--output', output +'.mkv', '--language', '0:eng', '--default-track', '0:yes', '--compression', '0:none', 'decrypted.mp4', '--language', '0:fr', '--default-track', '0:yes', '--compression' ,'0:none', 'decrypted.m4a', '--language', '0:eng','--track-order', '0:0,1:0,2:0,3:0,4:0', ex_subEN])      
  
  else: 
    subprocess.run([mkvmergeexe, '--ui-language' ,'en', '--output', output +'.mkv', '--language', '0:eng', '--default-track', '0:yes', '--compression', '0:none', 'decrypted.mp4', '--language', '0:fr', '--default-track', '0:yes', '--compression' ,'0:none', 'decrypted.m4a', '--language', '0:fr','--track-order', '0:0,1:0,2:0,3:0,4:0', ex_subFR])
  print("\nAll Done .....")           

else:
    print("Merging .....")
    if os.path.isfile('decrypted2.m4a'):
        subprocess.run([mkvmergeexe, '--ui-language' ,'en', '--output', output +'.mkv', '--language', '0:eng', '--default-track', '0:yes', '--compression', '0:none', 'decrypted.mp4', '--language', '0:fr', '--default-track', '0:yes', '--compression' ,'0:none', 'decrypted.m4a', '--language', '0:eng', '--default-track', '0:no', '--compression' ,'0:none', 'decrypted2.m4a', '--language', '0:eng','--track-order', '0:0,1:0,2:0,3:0,4:0'])
    else:
        subprocess.run([mkvmergeexe, '--ui-language' ,'en', '--output', output +'.mkv', '--language', '0:eng', '--default-track', '0:yes', '--compression', '0:none', 'decrypted.mp4', '--language', '0:fr', '--default-track', '0:yes', '--compression' ,'0:none', 'decrypted.m4a', '--language', '0:eng','--track-order', '0:0,1:0,2:0,3:0,4:0'])
        print("\nAll Done .....")    

print("\nDeleting temporary files...")
#delete_choice = int(input("Enter Response : "))

#if delete_choice == 1:
os.remove("encrypted.m4a")
os.remove("encrypted.mp4")
os.remove("decrypted.m4a")
os.remove("decrypted.mp4")
try:    
    os.remove("decrypted2.m4a")
    os.remove("encrypted2.m4a")
    os.remove("fr.srt")
    os.remove("fr.ttml2")
    
except:
    pass
print("\nDone !")    
#else:
 #   pass
