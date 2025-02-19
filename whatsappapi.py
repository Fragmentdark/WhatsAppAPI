from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Caminho para o ChromeDriver
caminho_chromedriver = r"D:\Reinaldo\Acadêmico\FACULDADE\Programação\chromedriver.exe"

# Inicializa o navegador Chrome
service = Service(caminho_chromedriver)
driver = webdriver.Chrome(service=service)

# Abre o WhatsApp Web (já logado)
driver.get("https://web.whatsapp.com")

# Aguarde até que o QR Code seja escaneado manualmente
input("Pressione ENTER após escanear o QR Code e carregar o WhatsApp Web...")

# Número de destino e mensagem
numero_destino = "5537991110031"
mensagem = "Olá, esta é uma mensagem de teste enviada pelo seu filho Reinaldo Júnior Alves da Silveira. Obrigado pela Atenção!"

# Abre o chat com o número de destino
link_chat = f"https://web.whatsapp.com/send?phone={numero_destino}"
driver.get(link_chat)

# Aguarde até que o campo de mensagem esteja disponível
try:
    caixa_de_texto = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
    )
    caixa_de_texto.send_keys(mensagem)
    caixa_de_texto.send_keys(Keys.ENTER)
    print("Mensagem enviada com sucesso!")
except Exception as e:
    print(f"Erro ao enviar mensagem: {e}")

# Aguarde alguns segundos antes de fechar o navegador
time.sleep(5)

# Fecha o navegador
driver.quit()