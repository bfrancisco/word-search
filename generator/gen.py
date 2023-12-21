from word_search_generator import WordSearch as WSG
from WordSearch import WordSearch
import random

WORDLST = "wordlist.txt"

def get_random_words(n):
    "generate n random words"
    with open(WORDLST) as f:
        words_db = [w.strip() for w in f.readlines()]
        random_words = random.sample(words_db, n) 
    return random_words

def generate_puzzle(sz, n):
    "creates a sz x sz puzzle with n words"
    words = get_random_words(n)
    pz = WSG(" ".join(words))
    pz.level = 3 # all 8 directions
    pz.size = sz
    return WordSearch(pz.puzzle, words)


if __name__ == "__main__":
    # 100 test cases, 20x20 grid, 
    wordSearch = generate_puzzle(15, 10)

    print(wordSearch)
