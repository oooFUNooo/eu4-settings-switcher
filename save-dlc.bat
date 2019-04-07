@echo off

set EU4PATH=%HOMEDRIVE%%HOMEPATH%\Documents\Paradox Interactive\Europa Universalis IV

eu4-settings-switcher.py "%EU4PATH%" --dlc --save settings\DLC.txt

echo DLCの設定をセーブしました。
echo;
pause
