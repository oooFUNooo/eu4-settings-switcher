@echo off

set EU4PATH1=%HOMEDRIVE%%HOMEPATH%\Documents\Paradox Interactive\Europa Universalis IV
set EU4PATH2=C:\Program Files (x86)\Steam\steamapps\common\Europa Universalis IV

eu4-settings-switcher.py "%EU4PATH1%" --dlc --load settings\DLC.txt
eu4-settings-switcher.py "%EU4PATH1%" --mod --load settings\MOD.txt

cd "%EU4PATH2%"
start eu4.exe
