# Text to work with
text_a = ("Lorem ipsum dolor! diam amet, consetetur Lorem magna. "
            "sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.")

# Class to store and analyze the text
class TextAnalyzer():
    # stores text as a text parameter
    def __init__(self, text):
        self.text = text.lower()
        self.replace_punctuation()

    def replace_punctuation(self): # Used in constructor to immediately replace the punctuation
        replace_what = ['.', ',', '!', '?']
        for letter in self.text:
            if letter in replace_what:
                self.text = self.text.replace(letter, '')
    
    def freqAll(self):
        freq_dict = {}
        for word in self.text.split():
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1
        return freq_dict

    def freqOf(self, word):
        freq_dict = self.freqAll()
        if word in freq_dict:
            return freq_dict[word]
        else:
            return 0
        

# Test the class
if __name__ == "__main__":
    analyzer = TextAnalyzer(text_a)
    print(analyzer.text)
    print(analyzer.freqAll())
    print(analyzer.freqOf('lorem'))