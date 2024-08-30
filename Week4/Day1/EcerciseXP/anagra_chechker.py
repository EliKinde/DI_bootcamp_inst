list_word = []

with open("../sowpods.txt", "r") as f:
    list_word = f.readlines()
    for row in range(len(list_word)):
        list_word[row] = list_word[row].strip()


class AnagramChecker:
    def __init__(self, list_word):
        self.list_word = list_word

    def is_valid_word(self, word):
        if self.word in self.list_word:
            return True
        else:
            return False

    def get_anagrams(self, word):
        pass

    def is_anagrams(self, word1, word2):
        pass


s = input("entr your word ")
word = s.upper()

if word in list_word:
    print(f"The is {word}")
else:
    print("the word is not in the list")
