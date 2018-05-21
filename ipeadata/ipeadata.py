""" Module to get data from ipeadata.com.br """
import requests as req
import pandas as pd


def basic_api_call(api):
    """
    Function to make a call on ipedata api
    :param api: url on api
    :return: a dataFrame with data
    """
    response = req.get(api)
    if response.status_code == req.codes.ok: # pylint: disable=no-member
        json_response = response.json()
        if 'value' in json_response:
            try:
                data_frame = pd.DataFrame(json_response['value'])
                return data_frame
            except Exception: # pylint: disable=broad-except
                return None
    return None

def get_sources():
    """
    Get sources from ipea web site
    :return: a data frame with the information
    """
    api = "http://ipeadata2-homologa.ipea.gov.br/api/v1/Fontes"
    return basic_api_call(api)

def get_metadata(serie=None):
    """
    Return metadata of a serie
    :param serie: serie to search for otherwise return metadata for all series
    :return: a data frame
    """
    url_final = "('%s')" % serie if serie is not None else ''
    api = "http://ipeadata2-homologa.ipea.gov.br/api/v1/Metadados%s" % url_final
    return basic_api_call(api)

# pylint: disable=invalid-name
def ipeadata(serie):
    """
    Return the values from a given serie
    :param serie: a serie to search for
    :return: a data frame with the values
    """
    api = "http://ipeadata2-homologa.ipea.gov.br/api/v1/ValoresSerie(SERCODIGO='%s')" % serie
    return basic_api_call(api)


if __name__ == "__main__":
    print(ipeadata('ADMIS'))
