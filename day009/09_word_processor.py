import string
sentence = input("Enter a sentence: ")
print([len(word.strip(string.punctuation)) for word in sentence.split()])
