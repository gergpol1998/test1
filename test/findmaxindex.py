def find_max_index(n):
    max_index = 0
    for i in range(1, len(n)):
        if n[i] > n[max_index]:
            max_index = i
    return max_index

my_list = [1,2,1,3,5,6,4]
max_index = find_max_index(my_list)
print("Maximum value index:", max_index)
    
