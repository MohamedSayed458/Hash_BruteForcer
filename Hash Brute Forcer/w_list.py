class wordlister():
    def read_wordlist(self, wpath):
        file = open(wpath, 'r')
        words = file.readlines()
        return words

