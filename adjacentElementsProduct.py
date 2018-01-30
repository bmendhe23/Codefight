def adjacentElementsProduct(inputArray):
    return max(inputArray[index]*inputArray[index+1] for index in range(len(inputArray)-1))
