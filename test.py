
# Q1> wap to shift the all 0 value at the last position in array without shifting any value

arr = [6,8,2,31,4,0,0,0,0,3,2,0,]
result = []

l = len(arr)
for i in range(l-1, -1, -1):
    if arr[i]!=0:
        result.insert(0, arr[i])
    else:
        result.append(arr[i])
print(result)


# output
# [6, 8, 2, 31, 4, 3, 2, 0, 0, 0, 0, 0]

