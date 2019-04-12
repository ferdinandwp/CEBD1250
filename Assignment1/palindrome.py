word = input("Enter a word: ")

#read in reverse
if word == word[::-1]:
    print("The word you entered is palindrome")
else:
    print("The word you entered is not a palindrome")