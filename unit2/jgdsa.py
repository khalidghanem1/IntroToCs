def replaceAtIndex(originalString, index, replacement):
    return originalString[:index] + replacement + originalString[index+1:]

word = input("Enter a word: ")
index = int(input("Enter an index: "))
newPart = input("Enter another word: ")

result = replaceAtIndex(word, index, newPart)
print("New word:", result)
