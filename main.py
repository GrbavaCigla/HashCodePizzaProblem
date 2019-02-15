
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


# numRows, numCols, minPerSlice, maxPerCels = list(map(int, input().split()))
# rows = [input() for i in range(numRows)]
numRows, numCols, minPerSlice, maxPerCels = 3, 5, 1, 6
rows = ["TTTTT", "TMMMT", "TTTTT"]
_slices = ["0 0 2 1", "0 2 2 2", "0 3 2 4"]


print(isValidSlice(rows, _slices[0], minPerSlice, maxPerCels))
