import time
import subprocess
import wget

cmd = subprocess.call
fileurl = 'https://repo.xxanqw.xyz/files/hackintosh/macrecoveryapp.zip'
file = wget.download(fileurl)
cmd("unzip ./macrecoveryapp.zip", shell=True)
cmd("rm -r macrecoveryapp.zip", shell=True)
cmd("rm -r /_MACOSX", shell=True)
cmd("clear", shell=True)

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
print('Ventura cant be downloaded at the moment\n\n')

answer = input('Your choise: ')

cmd('clear', shell=True)

if answer == str('1'): print('\nDownloading ' + Lion), time.sleep(1), subprocess.call("python3 macrecovery.py -b Mac-C3EC7CD22292981F -m 00000000000F0HM00 download", shell=True)
elif answer == str('2'): print('\nDownloading ' + MLion), time.sleep(1), subprocess.call("python3 macrecovery.py -b Mac-7DF2A3B5E5D671ED -m 00000000000F65100 download", shell=True)
elif answer == str('3'): print('\nDownloading ' + Mvr), time.sleep(1), subprocess.call("python3 macrecovery.py -b Mac-F60DEB81FF30ACF6 -m 00000000000FNN100 download", shell=True)
elif answer == str('4'): print('\nDownloading ' + Ysmt), time.sleep(1), subprocess.call("python3 macrecovery.py -b Mac-E43C1C25D4880AD6 -m 00000000000GDVW00 download", shell=True)
elif answer == str('5'): print('\nDownloading ' + ElC), time.sleep(1), subprocess.call("python3 macrecovery.py -b Mac-FFE5EF870D7BA81A -m 00000000000GQRX00 download", shell=True)
elif answer == str('6'): print('\nDownloading ' + Sierra), time.sleep(1), subprocess.call("python3 macrecovery.py -b Mac-77F17D7DA9285301 -m 00000000000J0DX00 download", shell=True)
elif answer == str('7'): print('\nDownloading ' + HSierra), time.sleep(1), subprocess.call("python3 macrecovery.py -b Mac-BE088AF8C5EB4FA2 -m 00000000000J80300 download", shell=True)
elif answer == str('8'): print('\nDownloading ' + Mojave), time.sleep(1), subprocess.call("python3 macrecovery.py -b Mac-7BA5B2DFE22DDD8C -m 00000000000KXPG00 download", shell=True)
elif answer == str('9'): print('\nDownloading ' + Catalina), time.sleep(1), subprocess.call("python3 macrecovery.py -b Mac-00BE6ED71E35EB86 -m 00000000000000000 download", shell=True)
elif answer == str('10'): print('\nDownloading ' + BS), time.sleep(1), subprocess.call("python3 macrecovery.py -b Mac-2BD1B31983FE1663 -m 00000000000000000 download", shell=True)
elif answer == str('11'): print('\nDownloading ' + Monterey), time.sleep(1), subprocess.call("python3 macrecovery.py -b Mac-E43C1C25D4880AD6 -m 00000000000000000 download", shell=True)
elif answer == str('L'): print('\nDownloading ' + LTST), time.sleep(1), subprocess.call("python3 macrecovery.py -b Mac-E43C1C25D4880AD6 -m 00000000000000000 -os latest download", shell=True)

cmd("rm -r macrecovery.py", shell=True)
cmd("rm -r boards.json", shell=True)
cmd('clear', shell=True)
print('All done!')
time.sleep(2)
