"""
This problem was asked by Amazon.

Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14.

"""
def common_denom(nums: list):
    common=set(())
    # each num in list 
    for num in nums:
        curr_denoms=set(())
        # each n in num
        for i in range(1, num+1):
            if not num%i:
                curr_denoms.add(i)
        if len(common) > 0:
            common.intersection_update(curr_denoms)
        else:
            common=curr_denoms
    return max(list(common))
        

if __name__ == '__main__':
    test=[42, 56, 14]
    print(common_denom(test))