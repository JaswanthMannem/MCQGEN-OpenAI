conda create -p env python=3.8 -y
source activate ./env
touch .gitignore
pip install -r requirements.txt


MLOPS:
in AMAZON EC2:

sudo apt update
sudo apt-get update
sudo apt upgrade -y
sudo apt install git curl unzip tar make sudo vim wget -y
git clone "your repository"
sudo apt install python3-pip
sudo apt install python3.12-venv
python3 -m venv myenv
source myenv/bin/activate
pip3 install -r requirements.txt
pip3 install langchain_community
python3 -m streamlit run Streamlit.py

If you want to add to openai api key

1. create .env file in your server
 touch .env
 vi .env

go with the security and add inbound rule add the port 8501