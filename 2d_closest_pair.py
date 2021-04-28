#nlogn closest pair algorithim

def distance(point1, point2):
    first_term = (point1[0] - point2[0])**2
    second_term = (point1[1] - point2[1])**2
    return (first_term + second_term)**.5

def closest_pair(sorted_by_x, sorted_by_y):
    #base case
    d = 0
    if len(sorted_by_x) <= 3:
        dist1 = distance(sorted_by_x[0], sorted_by_x[1])
        if len(sorted_by_x) == 2:
            return dist1
        dist2 = distance(sorted_by_x[0], sorted_by_x[2])
        dist3 = distance(sorted_by_x[1], sorted_by_x[2])
        return min(dist1, dist2, dist3)
    
    vertical_line = len(sorted_by_x) // 2

    #constant time to split list sorted by x in half
    sorted_x_left = sorted_by_x[:vertical_line]
    sorted_x_right = sorted_by_x[vertical_line:]

    sorted_y_left = []
    sorted_y_right = []
    #linear time to split the list sorted by y in half
    for point in sorted_by_y:
        if point[0] < sorted_by_x[vertical_line][0]:
            sorted_y_left.append(point)
        else:
            sorted_y_right.append(point)
    


    #recursive call
    d = min(closest_pair(sorted_x_left, sorted_y_left), closest_pair(sorted_x_right, sorted_y_right))


    #linear time to find the points around the vertical line

    #If we didn't sort the points before, then we would have to do an nlogn sort call here,
    #but because we have the points already sorted, we only need a linear time loop to 
    #determine what points are within d of the vertical line, making the merge between the two 
    #halfs of the problem linear time with respect to n

    strip_near_vertical_line_sorted_by_y = []
    for point in sorted_by_y:
        if abs(point[0] - sorted_by_x[vertical_line][0]) < d:
            strip_near_vertical_line_sorted_by_y.append(point)

    #See if there are any points that are closer than d, but on opposite sides of the vertical line.
    #This is linear time because, even though we need to check 8 points, for each point around d,
    #thats still linear time so we still haven't gone above the linear time constraint for merging the
    #the two halfs of the recursion problem
    for idx, point in enumerate(strip_near_vertical_line_sorted_by_y):
        for i in range(idx+1, idx+8):
            if i < len(strip_near_vertical_line_sorted_by_y):
                d = min(d, distance(point, strip_near_vertical_line_sorted_by_y[i]))
    
    return d

def starter_function_for_sorting(points):
    #nlogn time to sort by x
    sorted_by_x = sorted(points)
    
    #nlogn time to sort by y
    sorted_by_y = sorted(points, key=lambda x: x[1])
    return closest_pair(sorted_by_x, sorted_by_y)


input_points = [(0,0), (1,1), (-1,1), (1,-1), (4,-1), (0,.5), (2,2), (23,5), (2,.5), (.25,0), (0,.05)]
#output = .05


#time complexity is O(nlogn + nlogn + T(n) = 
#2T(n/2) + O(2n to get points around the vertical line + 7n to see if any points on either side are closer than d))
#O(nlogn + nlogn + nlogn)
#O(3nlogn)
#O(nlogn)

print(starter_function_for_sorting(input_points))