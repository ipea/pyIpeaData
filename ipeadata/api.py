""" Module to get data from ipeadata.com.br """
import requests as req
import pandas as pd


def basic_api_call(url):
    """
    Calls IpeaData API.

    :param url: (str) URL

    :return: DataFrame with requested data
    :rtype: pandas DataFrame
    """
    response = req.get(url)

    if response.status_code == req.codes.ok:  # pylint: disable=no-member

        json_response = response.json()
        if 'value' in json_response:

            df = pd.DataFrame(json_response['value'])

            # Raises an error if the DataFrame is empty
            if df.empty:
                raise FileNotFoundError('We were unable to find data according to the input parameters.')

            return df

    return None


def get_sources():
    """
    Lists sources from IpeaData containing the following fields:

    1. FNTID: <FILL EXPLANATION>
    2. FNTSIGLA: <FILL EXPLANATION>
    3. MACRO: <FILL EXPLANATION>
    4. REGIONAL: <FILL EXPLANATION>
    5. SOCIAL: <FILL EXPLANATION>

    :return: DataFrame with sources attributes
    :rtype: pandas DataFrame
    """
    return basic_api_call("http://ipeadata2-homologa.ipea.gov.br/api/v1/Fontes")


def get_metadata(id):
    """
    Returns metadata for the given time series.

    :param id: (str) time series id

    :return: Metadata for the given time series
    :rtype: pandas DataFrame
    """
    return basic_api_call("http://ipeadata2-homologa.ipea.gov.br/api/v1/Metadados('%s')" % id)


def get_region_level(id):
    """
    Returns region level for the given time series.

    :param id: (str) time series id

    :return: Region level of a time series
    :rtype: pandas DataFrame
    """
    url = ("http://ipeadata2-homologa.ipea.gov.br/api/v1/Metadados('{}')/Valores?$apply=groupby((NIVNOME))&$orderby=NIV"
           "NOME").format(id)
    return basic_api_call(url)


# pylint: disable=invalid-name
def get_data(id, groupby=None):
    """
    Returns data corresponding to the given time series.

    :param id: (str) time series id

    :return: Data for the given time series
    :rtype: pandas DataFrame
    """
    if groupby is not None:
        df = get_region_level(id)
        if df['NIVNOME'].isin([groupby]).any():
            url = ("http://ipeadata2-homologa.ipea.gov.br/api/v1/AnoValors(SERCODIGO='{}',NIVNOME='{}')?$top=100&$skip="
                   "0&$orderby=SERATUALIZACAO&$count=true").format(id, groupby)
            return basic_api_call(url)
        return None
    url = "http://ipeadata2-homologa.ipea.gov.br/api/v1/ValoresSerie(SERCODIGO='%s')" % id
    return basic_api_call(url)
