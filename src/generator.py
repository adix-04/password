#!/usr/bin/env python
# The goal is to create a custom tailored wordlist or password list for cracking password
# In order for this to work you should have some data about the target 
# based on that,  give key words, number combinations,symbols,names,places to the program and it does the rest
# i dont know what are the chances of this code guessing the password , but i know that its not zero if you can give some valueble data
# The better data == better chances of prediction

import random
import itertools
import os

__author__ = "Adix(Adin NS<adinnavakumar22@gmail.com>)"
__license__ = "GPL"
__version__ = "1.1.0"

message = """\033[33m
        █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
        █              𝗠𝗘𝗡𝗨
        █=============================================
        █ 1.  create random list from words                                     
        █ 2.  create random number combinations                                    
        █ 3.  use common password list
        █ 4.  download password list from intenet
        █ 5.  exit
        █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
\033[0m
"""
banner = """\033[32m
  _      ______         __  __  ____             
 | | /| / / __ \_______/ / /  |/  (_)_ _____ ____
 | |/ |/ / /_/ / __/ _  / / /|_/ / /\ \ / -_) __/
 |__/|__/\____/_/  \_,_/ /_/  /_/_//_\_\\__/_/     
"""
dev = "Developed by adix(Adin N S)           Word Mixer v1.0."

def intro():
    os.system("clear")
    print(banner)
    print(dev)
    print(message)
def option1():
    raw_input = input("\033[1m\033[33;32m[+] Enter high-probability words/number combinations(comma-separated):>\033[0m ")
    base_words = [w.strip() for w in raw_input.split(',') if w.strip()]
    wordlist = generate_passwords(base_words)

    with open("passwords.txt", "w") as f:
        for word in wordlist:
            f.write(word + "\n")
    
    print(f"\033[94m \nGenerated {len(wordlist)} passwords and saved to passwords.txt")
def option2():
    raw_input = input("\033[1m\033[33;32m[+] Enter high-probability number combinations only(comma-separated):>\033[0m ")
    base_words = [w.strip() for w in raw_input.split(',') if w.strip()]
    wordlist = generate_passwords(base_words)

    with open("passwords.txt", "w") as f:
        for word in wordlist:
            f.write(word + "\n")
    
    print(f"\033[94m \nGenerated {len(wordlist)} passwords and saved to passwords.txt")
def option3():
    print("option 3")
def option4():
    print('option4')

  
def generate_passwords(base_words,max_count =1000000):
    result = set()
    result.update(combine_words(base_words))     

    for word in base_words:
        for variant in mutate(word):
            result.add(variant)
            result.update(add_combos(variant))
            if len(result) >= max_count:
                return list(result)[:max_count]
    return list(result)[:max_count]
def common_word():
    print()

#combinig the input words like word1 + word2 + special char  with some special character
def combine_words(words):
    combos = set()
    symbols = ['', '@', '#', '$', '!', '&','%','*']
    word_forms = []
    for word in words:
        word_forms.extend([
            word,
            word.lower(),
            word.upper(),
            word.capitalize()
        ])
    # Pairwise combinations
    for w1, w2 in itertools.permutations(word_forms, 2):
        for s1 in symbols:
            for s2 in symbols:
                combos.add(f"{w1}{s1}{s2}{w2}")   # double-symbol join
                combos.add(f"{w1}{s1}{w2}")       # single-symbol join
    return list(combos)

#mutating the words like -> to uppercase or lowercase or reverse etc ..
def mutate(word):
    variants = [
        word,
        word.lower(),
        word.upper(),
        word.capitalize(),
        word[::-1],  #reverse
        leetspeak(word),
        leetspeak(word[::-1])  #reverse
    ]
    return list(set(variants))

#replacing certain characters to special symbols

def leetspeak(word):
    subs = {'a': '@', 's': '$', 'i': '1', 'e': '3', 'o': '0', 'l': '1', 't': '7','h':'#',}
    return ''.join(subs.get(c.lower(), c) for c in word)

#creating combinations with each word with a number and character 
def add_combos(word):
    combos = []
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    symbols = ['', '!', '@', '#', '$','&','%','.','-']
    for n in numbers:
        for s in symbols:
            combos.append(f"{word}{n}{n}{n}")
            combos.append(f"{word}{s}{n}{random.choice(numbers)}")
            combos.append(f"{n}{s}{word}")
            combos.append(f"{word}{n}{random.choice(numbers)}{random.choice(numbers)}")          
            combos.append(f"{word}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}")
            combos.append(f"{word}{random.choice(symbols)}{random.choice(numbers)}{random.choice(numbers)}")
            combos.append(f"{word}{s}{n}{numbers[int(n)-2]}{numbers[int(n)-3]}")
    return combos
def main():
        while True: 
            intro()
            choice = int(input("\033[1m\033[33;32m[+] Select an option number from the above menu >\033[0m "))
            if choice == 1:
                option1()
            elif choice == 2:
                option2()
            elif choice ==3:
                option3()
            elif choice == 4:
                option4()
            elif choice == 5:
                print(" ")
                print("\033[93mOk bye...")
                print("\033[93mThank you for using...")
                print(" ")
                os.system("exit")
                break
            

if __name__ == "__main__":
        main()