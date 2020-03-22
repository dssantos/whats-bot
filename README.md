## Como desenvolver

1. Clone o repositório
2. Crie um virtualenv
3. Ative o virtualenv
4. Instale as dependências
5. Instale o chromedriver
6. Crie a pasta treino
7. Execute

```console
git clone https://github.com/dssantos/whats-bot.git
cd whats-bot
python -m venv .whats-bot
source .whats-bot/bin/activate

pip install pip --upgrade
pip install -r requirements.txt

## Baixar o chromedriver

# - Para Chromium
sudo apt install chromium-chromedriver
cp /usr/lib/chromium-browser/chromedriver .

# - Para Google Chrome (https://sites.google.com/a/chromium.org/chromedriver/downloads)
# wget https://chromedriver.storage.googleapis.com/78.0.3904.105/chromedriver_linux64.zip
# unzip chromedriver_linux64.zip
# sudo chmod +x chromedriver

mkdir treino

# Executar
python main.py

# Este erro indica que a versão do chromedrive não é compatível com o navegador:
# OSError: [Errno 8] Exec format error: '/home/pi/dev/python/whats-bot/chromedriver'
```