# Finding Anagrams
# This programs accepts two inputs aand deretmines if they are anagrams.

print ("This program compares two srings to determine if they are anagrams.")
print ("Returns TRUE if they are anagrams and FALSE if otherwise.")
print()

word = input("Enter first word: ")
anagram = input("Enter second word: ")
print()

def find_anagram(word, anagram):
    if sorted(word) == sorted(anagram):
        return True
    else:
        return False
       
print(find_anagram(word, anagram))

input("Press ENTER to quit.")

