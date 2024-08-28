sudo apt update
sudo apt upgrade

sudo apt-get update
sudo apt-get upgrade

sudo apt install code
sudo apt install python3-full
sudo apt install nodejs
sudo apt install npm
sudo apt install netsat

cd Desktop/
git clone https://github.com/babban33/dental-backend .

cd Proj/
git clone https://github.com/babban33/dental

cd dental/
npm i

cd ../backend/
python3 -m venv betic

chmod -R 777 /home/chait/Desktop/Proj/backend/betic
source betic/bin/activate

pip install -r requirements.txt
