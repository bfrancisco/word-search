import os
# store all possible words for word search data 
WORDLIST = "wordlist.txt"

# from https://github.com/first20hours/google-10000-english
LONGWORDS = "longwords.txt"
MEDWORDS = "mediumwords.txt"

def gen_wordlist(readlst, wrdlst):
    if os.path.exists(wrdlst):
        os.remove(wrdlst)
    wordsfile = open(wrdlst, "a")

    for f in readlst:
        with open(f) as reader:
            words = [w.strip().upper() + '\n' for w in reader.readlines() if len(w.strip()) <= 12]
            wordsfile.writelines(words)
        
    wordsfile.close()

if __name__ == "__main__":
    
    
    gen_wordlist([LONGWORDS, MEDWORDS], WORDLIST)