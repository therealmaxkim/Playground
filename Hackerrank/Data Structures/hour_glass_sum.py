def hourglassSum(arr):

    #Define a helper function that takes 2 parameters: the array and the left top corner index
    #of the hourglass that you are trying to find.
    def getSum(arr, i, j):
        return arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]

    #Default is the first hourglass
    greatestSum = getSum(arr, 0, 0)

    #Go from the 0 to len(arr)-2 to get 3x3 space. Compare with previous sum to get the max.
    for i in range(0, len(arr)-2):
        for j in range(0, len(arr)-2):
            greatestSum = max(getSum(arr, i, j), greatestSum)

    return greatestSum
