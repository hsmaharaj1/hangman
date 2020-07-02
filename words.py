# 
# This file is to generate random words

import random

# This function returns the number of lastline of words.txt
def get_lastln():
    with open('words.txt', 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
        return len(lines)
        
def generate_words():
    initial = -1
    final = get_lastln()
    index = random.randint(0, int(final))
    file = open("words.txt", "r")
    for line in file:
        initial += 1
        if index == initial:
            return line.strip()
    

if __name__ == '__main__':
    print(generate_words())
