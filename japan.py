import sys

# Reading the message the user provided
message = sys.argv[1]
words = message.split()

# Building a list of word lengths
# so I can use the largest number later
wordLengths = []
for word in words:
    wordLengths.append(len(word))

charIndex = 0
line = max(wordLengths)

while line > 0:
    for word in words:
#    for word in reversed(words):
        if charIndex < len(word):
            print(word[charIndex] + " ", end='')
        else:
            print("  ", end='')
    print('')
    charIndex += 1
    line -= 1
