"""  Your task is to count the sum of the number of steps required to pick up all 3 items - 
('C' - compass), ('M' - map), ('S' - spyglass) from your starting position. 
So the result will be the sum of distance from Y to C, from Y to M and from Y to S (not Y-C-M-S).
Note that you can walk in 8 directions - left, right, up, down and sideways (on the diagonal in any direction). 
Your starting position is 'Y'.

Input: Array with the objects placements.

Output: The length of the path.

Precondition:
3x2 <= array size <= 10x10 """


def navigation(seaside):
    for j in range(len(seaside)):
        for col in range(len(seaside[j])):
            # note the coordinates of each item
            if seaside[j][col] == 'M':
                m = j,col
            if seaside[j][col] == 'S':
                s = j,col
            if seaside[j][col] == 'C':
                c = j,col
            if seaside[j][col] == 'Y':
                y = j,col
    lis = [m,s,c]

    res = 0
    # calculate the distance to each item from the starting position y
    # and add it to the overall result
    for l in lis:
    
        distance = (max(abs(l[0] - y[0]), abs(l[1] - y[1])))
        res += distance
    return res
    

