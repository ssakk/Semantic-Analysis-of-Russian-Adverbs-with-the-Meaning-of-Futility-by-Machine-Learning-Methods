import zipfile
import os

from gensim.models import KeyedVectors
import wget


class Model(object):
    model_url = 'http://vectors.nlpl.eu/repository/20/213.zip'

    def download(self):
        wget.download(self.model_url)

    def __init__(self):
        if not os.path.exists("../word_classes/model/model.model"):
            if not os.path.exists("213.zip"):
                self.download()
            z = zipfile.ZipFile('213.zip', 'r')
            z.extractall("model")
        self.model = KeyedVectors.load("model/model.model")
