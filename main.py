import requests as req
import json
import pandas as pd

def clean_string(text):
    ind_colc = text.find('[')
    print(ind_colc)
    text = text[ind_colc:-2]
    #print(text)
    return  text

def get_values(serie):
    api = "http://ipeadata2-homologa.ipea.gov.br/api/v1/ValoresSerie(SERCODIGO='%s')" % serie
    #api = "http://ipeadata2-homologa.ipea.gov.br/api/v1"
    print(api)
    r = req.get(api)
    if r.status_code == req.codes.ok:
        text = clean_string(str(r.content))
        df = pd.read_json(text)
        return df
    return None

def ipeaData(serie):
    return get_values(serie)


if __name__ == "__main__":
    print(ipeaData('ADMIS'))