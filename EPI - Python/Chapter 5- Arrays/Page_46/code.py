def add_one(number_array):
    carry_over = 0
    for i in range(len(number_array)-1):
        if number_array[i] + 1 + carry_over >= 10:
            number_array[i] = number_array[i] + 1 + carry_over - 10
            carry_over = 1
        else:
            number_array[i] = number_array[i] + 1 + carry_over
            carry_over = 0
    
    if carry_over == 1:
        number_array.insert(0, 1)
    
    return number_array