# guess the word game
# Create the Sentence and split the sentence by split method
sentence = input().split()

# assign a length
length = []

# create a loop function
for i in sentence:
    L = len(i)
    if L%2 == 1: # assign the ood value
        length.append(len(i))
    else:
        length.append(0)

if max(length) == 0:
    print("Better luck next time")

else:
    print(sentence[length.index(max(length))])
