@echo off

set EU4PATH=%HOMEDRIVE%%HOMEPATH%\Documents\Paradox Interactive\Europa Universalis IV

eu4-settings-switcher.py "%EU4PATH%" --mod --load settings\MOD.txt

echo MODの設定をロードしました。
echo;
pause
