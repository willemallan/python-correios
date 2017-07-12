from bs4 import BeautifulSoup
import requests

class Correios:

    CORREIOS = []
    ENTREGUE = False

    def __init__(self, codigo_rastreio):
        r = requests.post('http://www2.correios.com.br/sistemas/rastreamento/resultado_semcontent.cfm', data={'Objetos': codigo_rastreio })
        html = BeautifulSoup(r.text, "html.parser")
        table = html.body.div.table

        for tr in table.find_all('tr'):
            for td in tr.find_all('td'):

                if "sroDtEvent" in td['class']:

                    dados = td.text
                    dados = dados.replace('\r', '')
                    dados = dados.replace('\t', '')
                    dados = dados.split("\n")

                    hora = dados[1].strip()
                    data = dados[2].strip()
                    local = dados[3].strip()

                elif "sroLbEvent" in td['class']:

                    dados = td.text
                    dados = dados.replace('\r', '')
                    dados = dados.replace('\t', '')
                    dados = dados.split("\n")

                    titulo = dados[1].strip()
                    try:
                        descricao = dados[6].strip()
                    except:
                        descricao = ""

            self.CORREIOS.append({
                'hora': hora,
                'data': data,
                'local': local,
                'titulo': titulo,
                'descricao': descricao,
            })


correio = Correios('OA317156932BR')
print correio.CORREIOS
print correio.ENTREGUE