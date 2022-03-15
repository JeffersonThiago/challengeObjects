import challenge
import spread
from selenium import webdriver

# nome da planilha e index da folha
SHEET_NAME = 'testeplan'
WORK_SHEET_INDEX = 0

#caminho do webdriver e instância da página rpa_challenge
driver = webdriver.Chrome("C:/Users/jefferson.oliveira/Desktop/chromedriver.exe")
pagina = challenge.rpa_challenge(driver)

#planilha em forma de objeto 
sheet = spread.sheet_object(SHEET_NAME, WORK_SHEET_INDEX)

#conteudo da planinha que é uma lista com varias listas dentro
datas = spread.get_spread_sheet_data(sheet)

#função de acessar o sistema
pagina.open_system()

#função para começar o challenge
pagina.start_challenge()

#preenchendo as 10 rodadas do form
for data in datas:
    pagina.fill_form(data[0],data[1],data[2],data[3],data[4],data[5],data[6])

#capturando o resultado
result = pagina.get_result()

#armazendando o resultado na planilha
spread.update_spread_sheet(sheet, result)



