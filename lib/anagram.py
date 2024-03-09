# your code goes here!

class Anagram():
    def __init__(self, word):
        self.word = word
    def match(self, *words):
        anagrams = []
        sorted_word = sorted(self.word.lower())
        for word_list in words: 
            for word in word_list:
                if sorted(word.lower()) ==sorted_word and word.lower() != self.word.lower():
                    anagrams.append(word)
        return anagrams
       
        
        