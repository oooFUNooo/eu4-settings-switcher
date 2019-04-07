# eu4-settings-switcher
Europa Universalis IVの設定を簡単に切り替えるツールです。

## 導入方法
- 最初に[Python](https://www.python.org)をインストールしておいてください。
- 右上の緑色のボタンから本ツールをダウンロードして、適当な場所に展開してください。

## 使い方
- `save-mod.bat`を実行すると、現在のMODの設定が`settings`フォルダに`MOD.txt`という名前で保存されます。
- `load-mod.bat`を実行すると、保存したMODの設定が復元されます。
- `save-dlc.bat`と`load-dlc.bat`はDLCについて同じことを行います。設定は`DLC.txt`という名前で保存されます。

## 高度な使い方1（複数の設定を使い分ける）
- 設定は好きなだけ作成することができます。
- `save-mod.bat`と`load-mod.bat`を必要なだけコピーして適当な名前に変えてください。
- コピーした`save-mod.bat`と`load-mod.bat`の中にある`MOD.txt`という記述を好きなファイル名に変更してください。
- DLCの場合も同様です。`DLC.txt`という記述を書き換えてください。

## 高度な使い方2（設定を変えた後にEU4を起動する）
- EU4をCドライブ以外にインストールしている方は`eu4-start-sample.bat`の`EU4PATH2`を書き換えてください。
- `eu4-start-sample.bat`を実行すると、日本語化MODが選択された状態でEU4が自動的に起動します。
- `eu4-start-sample.bat`をコピーして書き換えれば、好きな設定で起動できるようになります。

## トラブルシューティング
- EU4の設定がおかしくなった場合は、以下のフォルダにある`settings.old`を`settings.txt`に上書きしてください。

　　`C:¥Users¥ユーザー名¥Documents¥Paradox Interactive¥Europa Universalis IV`

- その他、わからないことがあれば、EU4日本語化プロジェクトのDiscordで直接お尋ねください。
