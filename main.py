# Passo 1 - Entrar no sistema da empresa
import pyautogui #pip install pyautogui - interacao mouse, teclado e tela
import time #ja vem, é nativo
import pandas #pip install pandas - banco de dados

pyautogui.PAUSE = 0.3
def abrirpesquisa():
    pyautogui.keyDown('command')
    pyautogui.keyDown('space')
    pyautogui.keyUp('command')
    pyautogui.keyUp('space')

# Abrir o navegador
abrirpesquisa()
pyautogui.write('safar')
pyautogui.press('enter')
time.sleep(1) # aqui eu quero uma pausa de 3s para o safari abrir

# Entrar no site
pyautogui.hotkey('command', 'n') # abrir nova aba para garantir que esteja no campo do site
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(2) # aqui eu quero uma pausa de 3s para pagina carregar
pyautogui.click(3322, 1009)

# Importar a base de dados
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for i in tabela.index:
    # Cadastrar os produtos
    pyautogui.click(3322, 1009)  # selecionar primeiro local do formulario
    #codigo
    cod = tabela.loc[i,'codigo']
    pyautogui.write(str(cod))
    pyautogui.press('tab')
    #marca
    marca = tabela.loc[i,'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')
    #tipo
    tipo = tabela.loc[i,'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')
    #categoria
    cat = tabela.loc[i,'categoria']
    pyautogui.write(str(cat))
    pyautogui.press('tab')
    #preço unitário
    pu = tabela.loc[i,'preco_unitario']
    pyautogui.write(str(pu))
    pyautogui.press('tab')
    #custo
    cu = tabela.loc[i,'custo']
    pyautogui.write(str(cu))
    pyautogui.press('tab')
    #obs
    obs = tabela.loc[i,'obs']
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press('tab')
    #clicar em enviar
    pyautogui.press('enter')
    pyautogui.press('home')

# Finalizado