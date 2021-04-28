
# class Intersection:
#     lines1_inters = []
#     lines2_inters = []

#     i = 0
#     j = 0

#     left_point_from_lines1_inters = (0,0)
#     right_point_from_lines1_inters = (0,0)

#     left_point_from_lines2_inters = (0,0)
#     right_point_from_lines2_inters= (0,0)

#     def __init__(self, lines1_inters, lines2_inters, i, j):
#         print("iinters",lines1_inters, lines2_inters)
#         self.lines1_inters = lines1_inters
#         self.lines2_inters = lines2_inters
#         self.i = i
#         self.j = j

#     def line1_seg_right(self):
#         self.i = min(self.i+1, len(self.lines1_inters)-2)
#         return
    
#     def line1_seg_left(self):
#         self.i = max(0, self.i-1)
#         return

#     def line2_seg_right(self):
#         self.j = min(self.j+1, len(self.lines2_inters)-2)
#         return

#     def line2_seg_left(self):
#         self.j = max(0, self.j-1)
#         return

    
#     def calculate_intercept(self):
#         print(self.lines1_inters)
#         point1l = self.lines1_inters[self.i]
#         point1r = self.lines1_inters[self.i+1]

#         point2l = self.lines2_inters[self.j]
#         point2r = self.lines2_inters[self.j+1]

#         line1_slope = (point1r[1] - point1l[1]) / (point1r[0] - point1l[0])
#         line1_y_inter = point1l[1] - (line1_slope * point1l[0])

#         line2_slope = (point2r[1] - point2l[1]) / (point2r[0] - point2l[0])
#         line2_y_inter = point2l[1] - (line2_slope * point2l[0])


#         x_of_inter = ((line2_y_inter-line1_y_inter)/(line2_slope-line1_slope))
#         y_of_inter = line1_slope * x_of_inter + line1_y_inter

#         return (x_of_inter, y_of_inter) 


# def merge(lines1,lines2):
#     print("merger",lines1,lines2 )
#     if len(lines1) == 0: return lines2
#     if len(lines2) == 0: return lines1

#     lines1_intercepts = []
#     lines2_intercepts = []

#     for i in range(len(lines1)-1):
#         x_of_inter = ((lines1[i][1]-lines1[i+1][1])/(lines1[i+1][0]-lines1[i][0]))
#         y_of_inter = lines1[i][0] * x_of_inter + lines1[i][1]
#         lines1_intercepts.append((x_of_inter, y_of_inter))

#     for i in range(len(lines2)-1):
#         x_of_inter = ((lines2[i][1]-lines2[i+1][1])/(lines2[i+1][0]-lines2[i][0]))
#         y_of_inter = lines2[i][0] * x_of_inter + lines2[i][1]
#         lines2_intercepts.append((x_of_inter, y_of_inter))


#     x_of_inter = ((lines2[0][1]-lines1[-1][1])/(lines2[0][0]-lines1[-1][0]))
#     # y_of_inter = lines2[0][0] * x_of_inter + lines2[0][1]

#     if lines1_intercepts[-1][0] < x_of_inter < lines2_intercepts[0][0]
#         return lines1.extend(lines2)

#     x_of_inter = ((lines2[-1][1]-lines1[0][1])/(lines2[-1][0]-lines1[0][0]))
#     # y_of_inter = lines2[-1][0] * x_of_inter + lines2[-1][1]

#     if len(lines1_intercepts) == 1 and len(lines2_intercepts):
#         x_of_inter = ((lines2[0][1]-lines1[0][1])/(lines2[0][0]-lines1[0][0]))
#         if x_of_inter < lines1_intercepts[0][0]:
#             return[lines1[0]].extend(lines2)
#         x_of_inter = ((lines2[-1][1]-lines1[-1][1])/(lines2[-1][0]-lines1[-1][0]))
#         if x_of_inter > lines2_intercepts[0][0]:
#             return lines1.extend([lines2[-1]])

#     if lines2_intercepts[-1][0] < x_of_inter < lines1_intercepts[0][0]
#         return [lines1[0], lines2[-1]

#     intersection = Intersection(lines1_intercepts, lines2_intercepts, 0, 0)

#     count = 0
#     while count < (2 * (len(lines1) + len(lines2))):
#         inter = intersection.calculate_intercept()

#         if inter[0] < intersection.lines1_inters[intersection.i][0]: intersection.line1_seg_left()
#         if inter[0] > intersection.lines1_inters[intersection.i+1][0]: intersection.line1_seg_right()

#         if inter[0] < intersection.lines2_inters[intersection.j][0]: intersection.line2_seg_left()
#         if inter[0] > intersection.lines2_inters[intersection.j+1][0]: intersection.line2_seg_right()

#         count += 1

#     inter = intersection.calculate_intercept()
#     i = 0
#     while lines1_intercepts[i] < inter[0]:
#         i+=1
#     lines1 = lines1[:i+1]

#     i = 0
#     while lines2_intercepts[i] < inter[0]:
#         i+=1

#     lines1.extend(lines2)

#     return lines1

# def find_visible(lines):
#     if len(lines) == 2:
#         if lines[0][0] == lines[1][0]:
#             if lines[0][1] > lines[1][1]: return lines[:1]
#             else: return lines[1:]
#         else: return sorted(lines)
    
#     elif len(lines) == 3:
#         slope0 = lines[0][0]
#         slope1 = lines[1][0]
#         slope2 = lines[2][0]

#         y_inter0 = lines[0][1]
#         y_inter1 = lines[1][1]
#         y_inter2 = lines[2][1]

#         sorted_by_slopes = sorted([(slope0,y_inter0),(slope1,y_inter1),(slope0,y_inter0)])
#         x_of_inter = ((sorted_by_slopes[2][1]-sorted_by_slopes[0][1])/(sorted_by_slopes[2][0]-sorted_by_slopes[0][0]))
#         y_of_inter = sorted_by_slopes[0][0] * x_of_inter + sorted_by_slopes[0][1]
#         if y_of_inter < sorted_by_slopes[1][0] * x_of_inter + sorted_by_slopes[1][1]: 
#             return sorted_by_slopes
#         else: 
#             sorted_by_slopes.pop(1)
#             return sorted_by_slopes

    

#     mid = len(lines) // 2

#     first_half = find_visible(lines[:mid])
#     second_half = find_visible(lines[mid:])

#     return merge(first_half, second_half)

# input_lines = [(0,0),(-1,1),(1,1),(.5,2),(-.75,-1)]
# print(find_visible(sorted(input_lines)))