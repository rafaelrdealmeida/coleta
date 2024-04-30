import requests
from bs4 import BeautifulSoup
from tinydb import TinyDB, Query


def acessar_pagina(link):
    """
    Responsavel por acessar as paginas web
    """
    pagina = requests.get(link)
    bs = BeautifulSoup(pagina.text, 'html.parser')
    # print(bs)
    return bs

def extrair_infos(link):
    pagina = acessar_pagina(link)
    pdfs = pagina.find_all("h3") # [pdf1,pdf2,pdf3]
    lista_link_pdfs = []
    for pdf in pdfs:
        link_pdf  = pdf.a["href"]
        lista_link_pdfs.append(link_pdf)
        print(link_pdf)
    print(lista_link_pdfs)




def main():
    link = "https://cindesbrasil.org/breves-cindes"
    extrair_infos(link)

if __name__ == "__main__":
    main()