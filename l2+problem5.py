alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

word = input()

indexList = []

for letter in word:

    if letter in alphabets:
        #print(alphabets.index(l))
        indexList.append(alphabets.index(letter))
    else:
        print("False")

print(indexList)

swap = True

while swap:
    swap = False
        
    for i in range(len(indexList) - 1):
        if indexList[i] > indexList[i+1]:
            indexList[i], indexList[i+1] = indexList[i+1], indexList[i]
            swap = True

print(indexList)

wordList = []

for i in indexList:
    wordList.append(alphabets[i])

print(''.join(wordList))


# Test Case using built in method:

letter = ['h','e','l', 'l', 'o']
letter.sort()
print(letter)
