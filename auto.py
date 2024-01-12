
import pyautogui as pg
import pandas as pd 

# Nesse programa quero automatizar cadastro de produtos a partir de um arquivo .csv, utilizando a biblioteca de automação pyautogui e a biblioteca pandas para leitura do arquivo produtos.csv
# Link para cadastro de produtos: https://dlp.hashtagtreinamentos.com/python/intensivao/login


# 1° passo: Abrir o site do cadastro de produtos
#pg.PAUSE = 1

pg.hotkey("win","d")
pg.press("win")
pg.write("Google Chrome")
pg.press("enter")
pg.click(x=1082, y=597)
pg.hotkey("ctrl", "t")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pg.write(link)
pg.press("enter")
pg.click(x=862, y=473)
pg.write("yvensalmeida21@gmail.com")
pg.press("tab")
pg.write("********")
pg.press("tab")
pg.press("enter")

# 2° analisar dados do arquivo produtos .csv
tabela = pd.read_csv("produtos.csv")
print(tabela)

# 3° Cadastrar um produto

for linha in tabela.index:  
    pg.click(x=780, y=331)
        #codigo
    codigo = tabela.loc[linha, "codigo"]
    pg.write(str(codigo))
    pg.press("tab")
        #marca
    marca = tabela.loc[linha,"marca"]
    pg.write(str(marca))
    pg.press("tab")
        #tipo
    tipo = tabela.loc[linha, "tipo"]
    pg.write(str(tipo))
    pg.press("tab")
        #categoria
    categoria = tabela.loc[linha, "categoria"]
    pg.write(str(categoria))
    pg.press("tab")
        #preco_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pg.write(str(preco_unitario))
    pg.press("tab")
        #custo
    custo = tabela.loc[linha, "custo"]
    pg.write(str(custo))
    pg.press("tab")
        #obs
    obs = tabela.loc[linha,"obs"]
    if not pd.isna(obs):
        pg.write(str(obs))
    pg.press("tab")
        #cadastrar produto
    pg.press("enter")
        #retornar
    pg.scroll(5000)


