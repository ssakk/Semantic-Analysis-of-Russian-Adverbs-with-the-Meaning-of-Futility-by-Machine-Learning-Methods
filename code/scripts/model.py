from gensim.models import FastText
import wget
import zipfile
import os


class Model(object):
    model_url = 'http://vectors.nlpl.eu/repository/20/181.zip'

    def download(self):
        wget.download(self.model_url)

    def __init__(self):
        if not os.path.exists("181.zip"):
            self.download()
        if not os.path.exists("model/model.model"):
            z = zipfile.ZipFile('181.zip', 'r')
            z.extractall("model")
        self.model = FastText.load("model/model.model")
