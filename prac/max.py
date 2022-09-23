num = [1,3,5,7,9]
max = num[0]
for i_num in range(len(num)):
    if num[i_num] > max:
        max = num[i_num]
print(max)

for i_num in num:
    if i_num > max:
        max = i_num
print(max)

