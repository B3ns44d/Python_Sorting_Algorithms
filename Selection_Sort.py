def selection_sort(input_list):
    
    for idx in range(len(input_list)):

        min_idx = idx
        for j in range( idx +1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
# Swap the minimum value with the compared value

        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]

# add any list of number here 
l = [5,2,4,6,1,3]
selection_sort(l)
print(l)
