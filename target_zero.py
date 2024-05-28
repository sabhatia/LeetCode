def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) < 2:
        return
    
    indx = 0
    zeros = 0
    max_indx = len(nums)

    while indx + zeros < max_indx:

        # Check if the current number is a zero
        while indx + zeros < max_indx and nums[indx+zeros] == 0:
            zeros += 1
            # print(f'[{indx}][{zeros}]')

        if indx + zeros >= max_indx:
            break

        # Move the value count(zeros) index out to current pos
        nums[indx] = nums[indx + zeros]
        # print(f'[{indx}][{zeros}]: {nums}')
        indx += 1

    for indx in range(1, zeros+1):
        # print(f'nums[{indx}] = 0')
        nums[-indx] = 0

def main():
    i1 = [0,1,0,3,12]
    print(i1)
    moveZeroes(i1)
    print(i1)

    i3 = [0]
    print(i3)
    moveZeroes(i3)
    print(i3)

    i2 = [0,1]
    print(i2)
    moveZeroes(i2)
    print(i2)

    i4 = [1,0,2,0]
    print(i4)
    moveZeroes(i4)
    print(i4)

if __name__ == '__main__':
    main()