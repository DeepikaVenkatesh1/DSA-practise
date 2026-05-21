def Prefix(nums):
    prefix_sum=[]
    current=0
    for num in nums:
        current+=num
        prefix_sum.append(current)
    return prefix_sum
print(Prefix([1,2,3,4,5]))

         