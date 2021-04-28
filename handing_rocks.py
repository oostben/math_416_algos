input_arr = [3,5,2,6]

def left_index(iner, ln):
    return (iner - 1) % ln
def right_index(iner, ln):
    return (iner + 1) % ln

for i in range(30):
    print(input_arr)
    temp = input_arr.copy()

    for i in range(len(input_arr)):
        input_arr[i] = (1/3) * temp[left_index(i,len(input_arr))] + (2/3) * temp[right_index(i,len(input_arr))]
