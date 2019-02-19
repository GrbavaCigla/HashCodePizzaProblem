from itertools import combinations


def getMinIngredients(rows):
    numTomatos = 0
    numShrooms = 0
    for i in rows:
        for j in i:
            if j == "T":
                numTomatos += 1
            elif j == "M":
                numShrooms += 1
            else:
                raise("Invalid Input: Slice Containing Invalid Ingredient(s)")
    if min(numShrooms, numTomatos) == numShrooms:
        return "mushroom"
    else:
        return "tomato"


def makeSlices(rows):
    minIngredient = getMinIngredients(rows)[0].upper()
    slices = []
    for id1, i in enumerate(rows):
        for id2, j in enumerate(i):
            if j == minIngredient:
                slices.append(" ".join(list(map(str, [id1, id2, id1, id2]))))
    return slices


def getSlice(rows, slice):
    raw_slice = list(map(int, slice.split()))
    row1 = raw_slice[0]
    col1 = raw_slice[1]
    row2 = raw_slice[2]
    col2 = raw_slice[3]
    return[i[col1:col2 + 1] for i in rows[row1:row2 + 1]]


def isValidSlice(rows, slice, minPerSlice, maxPerCels):
    raw_slice = list(map(int, slice.split()))
    row1 = raw_slice[0]
    col1 = raw_slice[1]
    row2 = raw_slice[2]
    col2 = raw_slice[3]
    verticalSize = row2 + 1 - row1
    horizontalSize = col2 + 1 - col1
    size = verticalSize * horizontalSize
    numTomatos = 0
    numShrooms = 0
    if size > maxPerCels:
        return False
    for i in getSlice(rows, slice):
        for j in i:
            if j == "T":
                numTomatos += 1
            elif j == "M":
                numShrooms += 1
            else:
                return False
    if numShrooms < minPerSlice or numShrooms < minPerSlice:
        return False
    return True


def getDistance(slice1, slice2):
    raw_slice1 = list(map(int, slice1.split()))
    raw_slice2 = list(map(int, slice2.split()))
    row1 = raw_slice1[0]
    col1 = raw_slice1[1]
    row2 = raw_slice2[2]
    col2 = raw_slice2[3]
    return (abs(abs(row1-row2)-1), abs(abs(col1-col2)-1))


def expandSlice(slice, right=1, left=1, top=1, bottom=1):
    raw_slice = list(map(int, slice.split()))
    row1 = raw_slice[0]
    col1 = raw_slice[1]
    row2 = raw_slice[2]
    col2 = raw_slice[3]
    return " ".join(list(map(str, [abs(row1-top), abs(col1-right), row2+bottom, col2+left])))


# numRows, numCols, minPerSlice, maxPerCels = list(map(int, input().split()))
# rows = [input() for i in range(numRows)]
numRows, numCols, minPerSlice, maxPerCels = 3, 5, 1, 6
rows = ["TTTTT", "TMMMT", "TTTTT"]
result_slices = ["0 0 2 1", "0 2 2 2", "0 3 2 4"]
slices = makeSlices(rows)


if result_slices == slices:
    print("Did it!")
