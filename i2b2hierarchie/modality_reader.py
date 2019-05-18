

import urllib3,pprint
from script_pivot_transfert.htmlParser import HTMLParser4OsirisValue
import script_pivot_transfert.csvGithubParser as csvParser

# TODO Parser le TSV au lieu du HTML (ajouter le TSV dans le projet / ou le répcupérer à la volé)
class osiris_value_parser():
    def __init__(self, url):
        self.url=url
        self.proxy_user = ''
        self.proxy_password = ''
        self.proxy_url = ''


    def add_proxy(self, user, password, url):
        self.proxy_user = user
        self.proxy_password = password
        self.proxy_url = url

    def parseWithProxy(self):
        proxy_header = self.proxy_user + ':' + self.proxy_password
        default_headers = urllib3.make_headers(proxy_basic_auth=proxy_header)
        http = urllib3.ProxyManager(self.proxy_url, headers=default_headers)
        contents = http.request('GET', self.url)
        #print('url request finish')
        parser = HTMLParser4OsirisValue()
        #print(contents.data.decode('utf-8'))
        parser.feed(contents.data.decode('utf-8'))

        return parser.data

    def parse(self):
        contents = urllib3.PoolManager().request('GET', self.url)
        parser = HTMLParser4OsirisValue()
        parser.feed(contents.data.decode('utf-8'))

        return parser.data

    def parseFromCsv(self):
        dataelementconcept = self.url.split("/")[-1].split("#")[0]
        return csvParser.get_osiris_value_for_data_element_concept(dataelementconcept)
