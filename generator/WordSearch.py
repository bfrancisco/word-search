class WordSearch:
    def __init__(self, puzzle, words):
        self.puzzle = puzzle
        self.words = words
        self.solution = "non"
    
    def __str__(self):
        s = "Puzzle:\n"
        for row in self.puzzle:
            for c in row:
                s += c + " "
            s += "\n"
        s += "\nSolution:\n" + self.solution
        return s

    def compute_solution():
        # Trie solution?
        return "TODO"