class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
def largestNumber(nums):
    temp = list(map(str,nums))
    temp = sorted(temp, key=LargerNumKey)
    largest_num = "".join(temp)
    return '0' if largest_num[0] == '0' else largest_num

nums = [3,30,34,5,9]
print(largestNumber(nums))