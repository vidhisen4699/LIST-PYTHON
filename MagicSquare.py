def isMagic( square ):

    result = isMatrix( square )

    if result:

        sums = []

        # diagonal \
        sum = 0
        for x in range(len(square)):
            sum += square[x][x]
        
        sums.append(sum)

        # diagonal /
        sum = 0
        y = len(square) - 1
        for x in range(len(square)):
            sum += square[x][y]
            y -= 1
        
        sums.append(sum)

        # rows _
        sum = 0
        for x in range(len(square)):
            for y in range(len(square)):
                sum += square[x][y]
            sums.append(sum)
            sum = 0
        
        # cols |
        sum = 0
        for x in range(len(square)):
            for y in range(len(square)):
                sum += square[y][x]
            sums.append(sum)
            sum = 0        
        
        # check if all are identical
        val = sums[0]
        for i in range(1, len(sums)):
            if sums[i] != val:
                result = False
                break
    #end if

    return result

# check if is a list of n x n 
def isMatrix( m ):
    result = True

    size = len(m)

    for row in m:
        if len(row) != size:
            result = False
            break
    
    return result

def printMatrix( matrix ):
	for subList in matrix:
		print(subList)

square = [
    [ 8, 1, 6 ],
    [ 3, 5, 7 ],
    [ 4, 9, 2 ]
]

print("Square:")
printMatrix(square)
print()
print(f"Is magic square? {isMagic(square)}")