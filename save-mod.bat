@echo off

set EU4PATH=%HOMEDRIVE%%HOMEPATH%\Documents\Paradox Interactive\Europa Universalis IV

eu4-settings-switcher.py "%EU4PATH%" --mod --save settings\MOD.txt

echo MODの設定をセーブしました。
echo;
pause
