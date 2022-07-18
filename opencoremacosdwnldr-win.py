# I will recommend you to use EXE version of this script
#
# You can download it here - https://github.com/xxanqw/OpenCore-MacOS-downloader/releases

import time
import subprocess
from urllib import response
import wget
import gdown
import requests

p = time.sleep
cmd = subprocess.call
down = wget.download
title = 'OpenCore MacOS downloader 0.4a Windows\n--------------------------------------'
fileurl = 'https://repo.xxanqw.xyz/files/hackintosh/macrecoveryapp.7z'
szipurl = 'https://www.7-zip.org/a/7zr.exe'
g = gdown.download


# updater
ver = "b'0.4a'"
webver = 'https://repo.xxanqw.xyz/files/ver/ver.txt'
getver = requests.get(webver)
checkver = str(getver.content)

if str(checkver) != ver: print(title + '\nYour version is outdated, please download new from https://github.com/xxanqw/OpenCore-MacOS-downloader/releases'), input('\n\n\n(press enter to exit)'), exit()

# script
down(fileurl)
cmd("7zr x macrecoveryapp.7z", shell=True)
cmd("del macrecoveryapp.7z", shell=True)
cmd("del 7zr.exe", shell=True)
cmd("cls", shell=True)

Lion = str('Lion')
MLion = str('Mountain Lion')
Mvr = str('Mavericks')
Ysmt = str('Yosemite')
ElC = str('El Capitan')
Sierra = str('Sierra')
HSierra = str('High Sierra')
Mojave = str('Mojave')
Catalina = str('Catalina')
BS = str('Big Sur')
Monterey = str('Monterey')
LTST = str('Latest')

print(title)
print('Choose your distribution\nby typing 1-11 or L for latest version\nPress "Enter" to close app\n')
print('1. Lion (10.7)')
print('2. Mountain Lion (10.8)')
print('3. Mavericks (10.9)')
print('4. Yosemite (10.10)')
print('5. El Capitan (10.11)')
print('6. Sierra (10.12)')
print('7. High Sierra (10.13)')
print('8. Mojave (10.14)')
print('9. Catalina (10.15)')
print('10. Big Sur (11.0)')
print('11. Monterey (12.0)')
print('L. Latest version\n')
print('B. Bundles (Beta)\n\n')
print('Ventura cant be downloaded at the moment\n\n')

answer = input('Your choice: ')

cmd('cls', shell=True)

if answer == str('1'): print(title + '\nDownloading ' + Lion), p(1), cmd("python3 macrecovery.py -b Mac-C3EC7CD22292981F -m 00000000000F0HM00 download", shell=True)
elif answer == str('2'): print(title + '\nDownloading ' + MLion), p(1), cmd("python3 macrecovery.py -b Mac-7DF2A3B5E5D671ED -m 00000000000F65100 download", shell=True)
elif answer == str('3'): print(title + '\nDownloading ' + Mvr), p(1), cmd("python3 macrecovery.py -b Mac-F60DEB81FF30ACF6 -m 00000000000FNN100 download", shell=True)
elif answer == str('4'): print(title + '\nDownloading ' + Ysmt), p(1), cmd("python3 macrecovery.py -b Mac-E43C1C25D4880AD6 -m 00000000000GDVW00 download", shell=True)
elif answer == str('5'): print(title + '\nDownloading ' + ElC), p(1), cmd("python3 macrecovery.py -b Mac-FFE5EF870D7BA81A -m 00000000000GQRX00 download", shell=True)
elif answer == str('6'): print(title + '\nDownloading ' + Sierra), p(1), cmd("python3 macrecovery.py -b Mac-77F17D7DA9285301 -m 00000000000J0DX00 download", shell=True)
elif answer == str('7'): print(title + '\nDownloading ' + HSierra), p(1), cmd("python3 macrecovery.py -b Mac-BE088AF8C5EB4FA2 -m 00000000000J80300 download", shell=True)
elif answer == str('8'): print(title + '\nDownloading ' + Mojave), p(1), cmd("python3 macrecovery.py -b Mac-7BA5B2DFE22DDD8C -m 00000000000KXPG00 download", shell=True)
elif answer == str('9'): print(title + '\nDownloading ' + Catalina), p(1), cmd("python3 macrecovery.py -b Mac-00BE6ED71E35EB86 -m 00000000000000000 download", shell=True)
elif answer == str('10'): print(title + '\nDownloading ' + BS), p(1), cmd("python3 macrecovery.py -b Mac-2BD1B31983FE1663 -m 00000000000000000 download", shell=True)
elif answer == str('11'): print(title + '\nDownloading ' + Monterey), p(1), cmd("python3 macrecovery.py -b Mac-E43C1C25D4880AD6 -m 00000000000000000 download", shell=True)
elif answer == str('L'): print(title + '\nDownloading ' + LTST), p(1), cmd("python3 macrecovery.py -b Mac-E43C1C25D4880AD6 -m 00000000000000000 -os latest download", shell=True)

elif answer == str('B'):

    HSierra_bundle = 'MacOS ' + HSierra + ' Bundle'

    print(title + '\nWelcome to Bundles (Beta)\n')
    print('1. '+ HSierra_bundle)
    print('  | Motherboard: B450\n  | CPU: AMD Zen\n  | GPU: GTX 10**\n\n')

    answer_bundle = input('Your choice: ')
    hsierra_bundle_id = '1-9zPRFTAnmw4RjViG-zRVP0R4cBqhVeC'

    if answer_bundle == str('1'): cmd('cls', shell=True), print(title + '\n\nDownloading ' + HSierra_bundle + '\n\n'), p(1), down(szipurl), print(), p(1), g(id=hsierra_bundle_id), p(1), cmd('cls', shell=True), print(title + '\n\nUnzipping ' + HSierra_bundle + ' \n\n'), p(1), cmd('7zr x HighSierraBundle.7z'), p(1), cmd('cls', shell=True), print(title + '\n\nCleaning up...'), cmd('del HighSierraBundle.7z', shell=True), cmd('del 7zr.exe', shell=True), cmd("del macrecovery.py", shell=True), cmd("del boards.json", shell=True), p(2), cmd('cls', shell=True), print(title + '\n\nHere you go!\nCheck "High Sierra Bundle" folder!\n\nScript by xxanqw - https://xxanqw.xyz/'), p(5), exit()

cmd("del macrecovery.py", shell=True)
cmd("del boards.json", shell=True)
cmd('cls', shell=True)
print(title + '\nAll done!\nScript by xxanqw - https://xxanqw.xyz/')
p(3)
