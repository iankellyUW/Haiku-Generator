import random
import linecache

def countSyllables(word):
    count = 0
    vowels = "aeiouy"
    word = word.lower()
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count

def mapWords():
    dictionary = {}
    wordsList = open(r"C:\Users\Ian\Desktop\words1.txt", "r") #read only copy of words

    newList = open(r"C:\Users\Ian\Desktop\words.txt", "w")
    for word in wordsList:
        newList.write(str(countSyllables(word)) + " " + word) #write the constinants to the file preceeded by their syllables
    newList.close()
    newList = open(r"C:\Users\Ian\Desktop\words.txt", "r")
    count = 0

    wordArray = []
    for word in newList:
        count += 1
        wordArray.append(word)
    print("There are " + str(count) + " words.")
    print("We picked word: ")

def genHaikuLine(syllables):
    haikuLine = []
    while (syllables > 0):
        newList = open(r"C:\Users\Ian\Desktop\words.txt", "r")
        rnd= random.randrange(0, 466513)
        #print("Grabbing line " + str(rnd))
        try: 
            line = newList.readlines()[rnd]
        except Exception as e:
        #    print("Getline Failed")
            newList.close()
        linePiece = line.split()
        if int(linePiece[0]) > syllables:
            continue
        else:
            haikuLine.append(linePiece[1])
            syllables = syllables - int(linePiece[0])
    return haikuLine

def genHaiku():
    print(genHaikuLine(5))
    print(genHaikuLine(7))
    print(genHaikuLine(5))

def main():
    toExit = False
    while(toExit == False):
        toMap = "map"
        toRand = "rnd"
        toHaik = "haiku"
        exit = "exit"
        print("Enter a word")
        txt = input("Enter: ")
        print("You entered: " + txt + ", which has " + str(countSyllables(txt)) + " syllables.")
        if txt == toMap:
            mapWords()
        if txt == toRand:
            num = random.randrange(1,466514)
            print(str(num))
        if txt == toHaik:
            genHaiku()
        if txt == exit:
            toExit = True

if __name__ == "__main__":
    main()