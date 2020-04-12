#!/bin/sh
# mjpg_streamer開始スクリプト
# インストール方法
# 1. sudo apt-get update
# 2. sudo apt-get install libjpeg9-dev cmake
# 3. sudo git clone https://github.com/jacksonliam/mjpg-streamer.git mjpg-streamer
# 4. cd mjpg-streamer/mjpg-streamer-experimental
# 5. sudo make
# 6. cd
# 7. sudo mv mjpg-streamer/mjpg-streamer-experimental /opt/mjpg-streamer

PORT="9000"
WIDTH="480"
HEIGHT="360"
FRAMERATE="20"
BRIGHTNESS="55"
QUALITY="80"
LD_LIBRARY_PATH=/opt/mjpg-streamer/ /opt/mjpg-streamer/mjpg_streamer \
    -i "input_raspicam.so -fps $FRAMERATE -q $QUALITY -x $WIDTH -y $HEIGHT -br $BRIGHTNESS" \
    -o "output_http.so -p $PORT -w /opt/mjpg-streamer/www"
