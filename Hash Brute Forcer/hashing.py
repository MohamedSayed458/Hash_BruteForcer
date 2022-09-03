import w_list #my module
import hashlib

hashing = str(input("enter the hash to break: ")) # get hash value from user

hash_type = str(input("enter the hash type: ")) # get hash type from user

wordlist_path = str(input("enter the wordlist path: "))

class Brute_Forcer():
    def hash_brute(self): #create a function to brute force the hash

        obj = w_list.wordlister() #taking object from the w_list.py module, exactly the class wordlister()
        wordlist = obj.read_wordlist(wordlist_path) #using the method read_wordlist from the wordlister() class, adn pass wordlist to it

        #at this point i have a list of names in a list, like this: ['ahmed\n', 'mohamed\n', 'khaled\n', 'hassan\n', 'ebrahim\n', 'hussam\n', 'samy\n', '\n'] so i will have to strip the \n 

        for line in wordlist:
            line = line.strip("\n") #remove the new line
            encodedLine = line.encode("utf-8") #make it as b'mohamed'
            line_hash = hashlib.new(hash_type) #create new object with the hash type 
            line_hash.update(encodedLine) #update to make it know the hash type

            hashed_value = line_hash.hexdigest()

            if hashed_value == hashing:
                print(f"{hashed_value} --> {line}")

x = Brute_Forcer()
x.hash_brute() #calling the hash_brute method

# 0. i have a module called w_list that reads the lines from a list
# 1. pass wordlist from w_list.py
# 2. make for loop to hash every line in the list
# 3. compare the hashed line with the hashing provided
# the md5 hash for mohamed is: 309cd3800aacbd003ac36199fa537295  , let's give it a try
# the out put is:  309cd3800aacbd003ac36199fa537295 --> mohamed
