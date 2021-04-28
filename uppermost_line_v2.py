def merge(lines1,lines2):
    lines1.extend(lines2)
    all_lines = lines1

    potential_lines = []
    potential_lines.append(all_lines.pop(0))
    potential_lines.append(all_lines.pop(0))
    num_potential_lines = 2

    for line in all_lines:
        last_line = potential_lines[num_potential_lines-1]
        second_to_last_line = potential_lines[num_potential_lines-2]
        inter1_x_val = (last_line[1] - second_to_last_line[1])/(second_to_last_line[0] - last_line[0])
        inter2_x_val = (line[1] - last_line[1])/(last_line[0] - line[0])

        while (inter2_x_val < inter1_x_val):
            potential_lines.pop(num_potential_lines - 1)
            num_potential_lines -= 1;

            if (num_potential_lines == 1): break

            last_line = potential_lines[num_potential_lines-1]
            second_to_last_line = potential_lines[num_potential_lines-2]
            inter1_x_val = (last_line[1] - second_to_last_line[1])/(second_to_last_line[0] - last_line[0])
            inter2_x_val = (line[1] - last_line[1])/(last_line[0] - line[0])
        
        potential_lines.append(line)
        num_potential_lines += 1

    return potential_lines

def find_visible(lines):
    if len(lines) == 2 or len(lines) == 1:
        return lines
    mid = len(lines) // 2

    first_half = find_visible(lines[:mid])
    second_half = find_visible(lines[mid:])

    return merge(first_half, second_half)

def start_algo(lines):
    sorted_by_slope = sorted(lines)
    i = 0
    while i < len(sorted_by_slope)-1:
        if sorted_by_slope[i][0] == sorted_by_slope[i+1][0]:
            if sorted_by_slope[i][1] >= sorted_by_slope[i+1][1]:
                sorted_by_slope.pop(i+1)
            else:
                sorted_by_slope.pop(i)
        else:
            i += 1
    
    return find_visible(sorted_by_slope)

input_lines1 = [(0,0),(-1,1),(1,1),(.5,2),(-.75,-1)]
input_lines1_correct = [(-1, 1), (0.5, 2), (1, 1)]
if start_algo(input_lines1) != input_lines1_correct: print("test 1 failed", start_algo(input_lines1))

input_lines2 = [(0,0),(-1,2),(1,3)]
input_lines2_correct = [(-1,2),(1,3)]
if start_algo(input_lines2) != input_lines2_correct: print("test 2 failed", start_algo(input_lines2))

input_lines3 = [(0,4),(-1,2),(1,3)]
input_lines3_correct = [(-1,2),(0,4),(1,3)]
if start_algo(input_lines3) != input_lines3_correct: print("test 3 failed", start_algo(input_lines3))

input_lines4 = [(0,4),(0,5),(0,3)]
input_lines4_correct = [(0,5)]
if start_algo(input_lines4) != input_lines4_correct: print("test 4 failed", start_algo(input_lines4))

input_lines5 = [(1,4),(.5,3),(-1,2)]
input_lines5_correct = [(-1,2),(1,4)]
if start_algo(input_lines5) != input_lines5_correct: print("test 5 failed", start_algo(input_lines5))

input_lines6 = [(0,0),(1,-5), (.1,0),(-.9,11.1),(.2,0),(-1,12)]
input_lines6_correct = [(-1,12),(1,-5)]
if start_algo(input_lines6) != input_lines6_correct: print("test 6 failed", start_algo(input_lines6))


input_lines7 = [(0,0),(-1,-5), (-.1,0),(.9,11.1),(-.2,0),(1,12)]
input_lines7_correct = [(-1,-5),(1,12)]
if start_algo(input_lines7) != input_lines7_correct: print("test 7 failed", start_algo(input_lines7))

input_lines8 = [(-1.5,-10),(0,0),(.2,0),(1,-14),(.1,-.001),(.9,-11),(-1,-5),(1,-15)]
input_lines8_correct = [(-1.5,-10),(-1,-5),(0,0),(.2,0),(.9,-11),(1,-14)]
if start_algo(input_lines8) != input_lines8_correct: print("test 8 failed", start_algo(input_lines8))

input_lines9 = [(2,1),(1,1),]
input_lines9_correct = [(1,1),(2,1)]
if start_algo(input_lines9) != input_lines9_correct: print("test 9 failed", start_algo(input_lines9))

print("done testing")
