# AutomataController

### 構成
- RaspberryPi zero wh
- Arduino Pro mini
- LittleBits R2D2
- Pi Camera モジュール

### 開発環境
- ~~Python 3.5.9（pyenv virtualenv 使用~~
- Python 3.5.3 (Raspbeery Pi Default)

### ライブラリ
| 名前 | バージョン | 用途  |
|---|---|---|
| ~~firebase-admin~~ | ~~3.2.1~~ | ~~認証~~ |
| flask | 1.1.1 | Web |
| numpy | 1.12.1 | 配列処理 |
| pyserial | 3.4 | シリアル通信 |
| RPi.GPIO | 0.7.0 | GPIO操作 |
| picamera | 1.13 | カメラ操作 |
| opencv | 4.1.1.26 | 画像処理 |
| tensorflow | 1.14.1 | |

### ライブラリインストール方法
- `sudo apt-get install python3-numpy`
- `sudo apt-get install python3-picamera`
- `sudo pip3 install opencv-python`

基本的には `apt-get install python3-パッケージ名` や `pip3 intall パッケージ名`
Tensorflow のみは以下  
`sudo pip3 install https://github.com/lhelontra/tensorflow-on-arm/releases/download/v1.4.1/tensorflow-1.4.1-cp35-none-linux_armv6l.whl
`

### アップデート方法
- `sudo pip3 install --upgrade パッケージ名`

### 実行方法
```
sudo python3 app.py
```

### 備考
- Raspberry Pi と Arduino の連携では Raspberry Pi 側のシリアルポートを解放する必要あり（参考：レシピ 9.23）
- Raspberry Pi のアップデートをすると以前のポート解放の設定が解除されている可能性あり
- シリアルポートの解放を行い、回路図に問題なく、通信した時にエラーの発生なく、期待した動作をしない場合は、送信できているが、受信できていない場合がある
- 上記の場合は Arduino (受信側)の RX, TX の PIN を逆に指定してみたりすると解決することが多かった。
- Raspberry Pi と Arudino の連携でのカスタムシリアル通信ではレベル変換は必須
- mjpg-streamerをインストールすれば、OpenCVの方で映像ストリームを受け取れる
- pyenv でインストールした Python 3.6.5 の環境では `pip install opencv-python` が失敗し、インストールできなかった（3.6系では PiPy に用意されていない？ 3.5 や 3.7 ではあるそう）
- 逆に numpy が import Error を吐くようになった（Python 3.5.9）
