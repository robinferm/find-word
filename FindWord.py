import json

def importData():
    with open ("data.txt") as d:
        data = d.readlines()
    data = [x.strip() for x in data]
    return data

# swap x and y
def flipData(data):
    column = ""
    columns = []
    for x in range(len(data[0])):
        for _, v in enumerate(data):
            column += v[x]
        columns.append(column)
        column = ""
    return columns


def findHorizontal(word, data):
    for i, j in enumerate(data):
        if word in j:
            # Set the found word to lower case and return the new data
            newValue = data[i].replace(word, word.lower())
            data[i] = newValue
            return data

        # Find reverse
        if word in j[::-1]:
            newValue = data[i][::-1].replace(word, word.lower())
            data[i] = newValue[::-1]
            return data
    return data

# Swap x and y and search horizontally, then swap back and return
def findVertical(word, data):
    data = flipData(data)
    data = findHorizontal(word, data)
    data = flipData(data)
    return data


def findDiagonal(word, data):
    newData = []
    for j in range(len(data[0])-1, -1, -1):
        string = ""
        for i in range(len(data[0])):
            string += data[i][j]
            j += 1
            if j > len(data[0])-1:
                break
        newData.append(string)

    data = findHorizontal(word, newData)

    return data

    # Main function
def findWord(word):
    data = importData()
    # Search horizontal (and reverse)
    data = findHorizontal(word, data)
    
    # Search vertical (and reverse)
    data = findVertical(word, data)

    # Search diagonal (right top side: \->) (and reverse)
    topDiagonal = findDiagonal(word, data)
    botDiagonal = findDiagonal(word, flipData(data))

    # Restore topDiagonal format
    topDiagonal.reverse()
    tempList = []
    for x in range(len(topDiagonal)):
        tempString = ""
        for y in range(len(topDiagonal)):
            tempString += topDiagonal[y][x]
        tempList.append(tempString)
        topDiagonal.pop()
    topDiagonal = tempList

    # Restore botDiagonal format
    botDiagonal.pop()
    tempList = []
    for z in range(1, len(botDiagonal)+1):
        tempString = ""
        for x in range(len(botDiagonal)):
            tempString += botDiagonal[x][-z]
        tempList.append(tempString)
        botDiagonal.pop(0)
    botDiagonal = tempList
    botDiagonal.reverse()

    # Merge topDiagonal and botDiagonal
    mergedLists = []
    for i in range(len(botDiagonal)): ###############
        mergedLists.append(botDiagonal[i] + topDiagonal[i+1])
    mergedLists.insert(0, topDiagonal[0])

    # Return the matrix (all cases) (returns unedited if word was not found)
    #return json.dumps(mergedLists)
    return mergedLists


#findWord('KABIN')
### Find many ###
# words = ['GILLAU', 'UFDA', 'UKYZ', 'APWDOAKWD']
# for word in words:
#     print()
#     print(f'SEARCHING FOR {word}')
#     result = findWord(word)
#     for r in result:
#         print(r)

### Find one ###
#result = findWord('GILLAU')
#print(result)
## for x in result:
##     print(x)




### Matrix ###
# UFDACYGLKP
# KABINAQXYV
# YLLNGTTAKE
# ZMPLWARZNO
# GVFAIXAAFY
# YMPLPGLSOH
# WGVHFPACKW
# AFTERTLTHU
# TNKIDCBEOS
# ZBAMANSWER