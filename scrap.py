from bs4 import BeautifulSoup
import requests
import xlwt
import re

book = xlwt.Workbook()
planilha = book.add_sheet('Página1')

planilha.write(0, 0, "Tipo")
planilha.write(0, 1, "Valor")
planilha.write(0,2,"parcelado")

url = "https://lista.mercadolivre.com.br/iphone#D[A:iphone]"

last = 1
i = 1
e = 1
while last <= 1951:
    url = f"https://celulares.mercadolivre.com.br/iphone_Desde_{last}_NoIndex_True"
    if last == 1:
        url = "https://lista.mercadolivre.com.br/iphone#D[A:iphone]"

    resultado = requests.get(url).text
    pagina = BeautifulSoup(resultado, "html.parser")
    boxes = pagina.find_all("div", class_="ui-search-result__content-wrapper")
    for box in boxes:
        h2 = box.find_all("h2", class_="ui-search-item__title")
        for texto in h2:
            planilha.write(i,0,texto.text)
            i += 1
        a = box.find_all("span", class_="price-tag-text-sr-only")
        j = 0
        k = 0
        while j < len(a):
            if not "Antes:" in str(a[j].text):
                if k%2 == 0:
                    valor = str(a[j].text)
                    planilha.write(e,1, valor)
                    e += 1

                k +=1

            j +=1
    print(f"pagina {(last - 1)/50 + 1}")

    last +=50

book.save('iphone.xlsx')
