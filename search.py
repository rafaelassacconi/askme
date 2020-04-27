
from stackoverflow.api import StackOverflow


class Search:
    """ Generic search class """

    def __init__(self, keywords, items=10):
        self.keywords = keywords
        self.items = items

    def by_keywords(self):
        """ Method to search using keywords """
        return self.__stackoverflow()

    def __stackoverflow(self):
        """ Search on Stack Overflow """
        tags = self.keywords.replace(" ", ";")
        client = StackOverflow()
        return client.search_questions(tags=tags, max=self.items)

    def __yahooanswers(self):
        """ Search on Yahoo Answers """
        raise NotImplementedError
