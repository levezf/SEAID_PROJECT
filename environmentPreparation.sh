#! /bin/bash

echo ""
echo "     Iniciando ...."
echo ""

sudo apt-get install figlet >> /dev/null


figlet SEAID - LEVEZ

echo ""
echo ""
echo "     Instalando Bibliotecas necessárias...."
echo ""

sudo apt-get install -y build-essential cmake pkg-config git-core
sudo apt-get install -y libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install -y libxvidcore-dev libx264-dev
sudo apt-get install -y libgtk2.0-dev
sudo apt-get install -y libatlas-base-dev gfortran


echo ""
echo "     Instalando WiringPi ...."
echo ""

cd ~
git clone git://git.drogon.net/wiringPi
cd ~/wiringPi
./build

echo ""
echo "     Instalando BCM2835 ...."
echo ""

cd ~
wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.56.tar.gz
tar zxvf bcm2835-1.56.tar.gz
cd bcm2835-1.56
./configure
make
sudo make check
sudo make install

echo ""
echo "     Instalando OpenCV ...."
echo ""

cd ~
git clone https://github.com/Itseez/opencv.git
cd ~/opencv
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=Release -D WITH_V4L=ON -D WITH_LIBV4L=ON -D WITH_FFMPEG=1 -D CMAKE_INSTALL_PREFIX=/usr/local ..
make 
sudo make install 
sudo ldconfig

echo ""
echo "     Atualizando Repositórios ...."
echo ""

echo "================================================"
echo ""
echo "________CONCLUIDO________"
echo ""
echo "     Iniciando Reboot ...."
echo ""
sudo reboot