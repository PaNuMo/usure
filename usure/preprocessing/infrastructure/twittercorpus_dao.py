from .corpus_dao import CorpusDAO
from pandas import DataFrame

class TwitterCorpusDAO(CorpusDAO):
    
    def get_corpus(self) -> DataFrame:
        return self._get_corpus("tweets.txt")

    def store_corpus(self, data):
        self._store_corpus("twitter", data)