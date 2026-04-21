def replace_at_index(word, index):
    newword = word[:index] + "-" + word[index+1:]
    return newword

uword = input("Enter a word: ")
uindex = int(input("Enter an index: "))

result = replace_at_index(uword, uindex)
print("New word:", result)
