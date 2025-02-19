# WhatsAppAPI
API Messenger 

o código é python... é necessário instalar o chrome driver

verifique a versão do seu chrome em configurações/ajuda (se for possível atualize)

acesse: https://googlechromelabs.github.io/chrome-for-testing/ (versões novas do chrome)
ou
https://developer.chrome.com/docs/chromedriver/downloads?hl=pt-br (versões anteriores)

instale o chrome driver 

Instale o python depois o comando para o Selenium no terminal:

pip install selenium

teste o chrome driver: 

python -c "
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.google.com')
print(driver.title)
driver.quit()
"

no prompt como administrador

depois coloque esse código para alocar o chrome driver no caminho certo para rodar a API do whats app web:

pip install webdriver-manager

Também no prompt... faça os laços de repetições e teste o código em um número apontando a camera para o QR code que gerar quando executar
o comando do código no terminal


AE DA CERTO 

TMJ
