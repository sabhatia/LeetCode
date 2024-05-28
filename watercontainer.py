def tank_area(height, l_indx, r_indx):
    ta = min(height[l_indx], height[r_indx]) * (r_indx - l_indx)

    # print(f'Height: {min(height[l_indx], height[r_indx])}')
    # print(f'Width: {(r_indx - l_indx)}')
    # print(f'TA({l_indx},{height[l_indx]}),({r_indx},{height[r_indx]})) = {ta}')

    return ta

def maxArea(height: list[int]) -> int:

    l_indx, r_indx = 0, len(height)-1
    l_wall, r_wall = l_indx, r_indx

    max_area = tank_area(height, l_wall, r_wall)

    print(f'Left-Indx:[{l_wall}] - Height: {height[l_wall]}, Right-Indx:[{r_wall}] - Height:{height[r_wall]}')    
    print(f'Curr Max Area: {max_area}')

    while (l_indx <= r_indx):
        # Update one of the indices
        if height[l_indx] < height[r_indx]:
            l_indx += 1
        else:
            r_indx -= 1

        # if we found a better wall, record it
        ta = tank_area(height, l_indx, r_indx)
        if  ta > max_area:
            l_wall, r_wall, max_area = l_indx, r_indx, ta

    return max_area
    
def main():
    # height = [1,8,6,2,5,4,8,3,7]
    # print(f'Area: {maxArea(height)}')

    # height = [1,1]
    # print(f'Area: {maxArea(height)}')

    # height = [1,2]
    # print(f'Area: {maxArea(height)}')

    # height=[2,3,4,5,18,17,6]
    # print(f'Area: {maxArea(height)}')

    height = [1,0,0,0,0,0,0,2,2]
    print(f'Tank Area: {tank_area(height, 0,8)}')
    print(f'Area: {maxArea(height)}')

    height = [76,155,15,188,180,154,84,34,187,142,22,5,27,183,111,128,50,58,2,112,179,2,100,111,115,76,134,120,118,103,31,146,58,198,134,38,104,170,25,92,112,199,49,140,135,160,20,185,171,23,98,150,177,198,61,92,26,147,164,144,51,196,42,109,194,177,100,99,99,125,143,12,76,192,152,11,152,124,197,123,147,95,73,124,45,86,168,24,34,133,120,85,81,163,146,75,92,198,126,191]
    print(f'Tank Area: {tank_area(height, 0,8)}')
    print(f'Area: {maxArea(height)}')

if __name__ == '__main__':
    main()