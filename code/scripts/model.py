import gensim
import wget
import zipfile
import os


class Model(object):
    model_url = 'http://vectors.nlpl.eu/repository/20/220.zip'

    def download(self):
        wget.download(self.model_url)

    def __init__(self):
        if not os.path.exists("220.zip"):
            self.download()
        if not os.path.exists("model/model.bin"):
            z = zipfile.ZipFile('220.zip', 'r')
            z.extractall("model")
        self.model = gensim.models.KeyedVectors.load_word2vec_format("model/model.bin", binary=True)
