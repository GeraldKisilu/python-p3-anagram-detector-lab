# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list):
        return [word for word in list if sorted(word) == sorted(self.word)]