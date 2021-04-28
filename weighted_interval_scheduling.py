class interval:
    def __init__(self, start_time_in, end_time_in, weight_in):
        self.start_time = start_time_in
        self.end_time = end_time_in
        self.weight = weight_in

input_intervals = []

input_intervals.append(interval(0,0,0))
input_intervals.append(interval(0,1.7,2))
input_intervals.append(interval(.5,2.6,4))
input_intervals.append(interval(2,3.5,4))
input_intervals.append(interval(.7,4,7))
input_intervals.append(interval(3.6,4.6,2))
input_intervals.append(interval(3.7,4.7,1))

def compute_opt(intervals):

    memo = [0 for x in range(len(intervals))]

    for j in range(1,len(memo)):
        p_j = 0
        for i in range(len(intervals)):
            if intervals[i].end_time < intervals[j].start_time:
                p_j = i
        memo[j] = max(intervals[j].weight + memo[p_j], memo[j-1])
    print("memo", memo)
    return memo
compute_opt(input_intervals)