def add_one(number_array):
    carry_over = 1
    index = len(number_array)-1

    while True:
        if index < 0:
            number_array.insert(0, 1)
            break
        if number_array[index] + carry_over >= 10:
            number_array[index] = number_array[index] + carry_over - 10
            index -= 1
        else:
            number_array[index] = number_array[index] + carry_over
            break
    
    return number_array

if __name__ == "__main__":
    print(add_one([1, 2, 8]))