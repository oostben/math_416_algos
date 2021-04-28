# Job class
class Job:
# initializer function to create the jobs
def __init__(self,time_in, deadline_in):
    self.time = time_in
    self.deadline = deadline_in

# this is an overloaded less than opterator, all it does is allow you to
# sort jobs using the built in python sort function in nlog(n)
def __lt__(self, other):
    if self.deadline == other.deadline:
        return self.time < other.time
    else:
        return self.deadline < other.deadline
# this is an overloaded function that allows me to print a job
def __repr__(self):
    return "time: " + str(self.time) + " deadline: " + str(self.deadline)

# this is a print memo function to print  the memo with the indexes around it
def print_memo(memo):
print("Starting Print Memo")  
print(" ", [i for i in range(len(memo[0]))])
for i in range(len(memo)):
    print(i,memo[i])
print()

# this is a fucntion that nicely pints a solution, you will see it used in the output
def print_solution(jobs, sequence, memo, num_jobs):
print("================================================")
print("This problem had jobs:")
jobs.sort()
for job in jobs:
    print(job)
print("\nThis problem had max sequence:")
for job in sequence:
    print(job)
print("\nFor this problem we could complete a max of", num_jobs, "jobs")
print("\nThis problem had memo:")
print_memo(memo)


# this is the important function that computes optimal schedule given input jobs using dp
def schedulable_set(jobs):
# first I remove all the jobs with a time longer than their deadline
# these jobs are impossible to complete by their deadline
# I also want to note that this is linear time with respect to the number of jobs
# so it is dominated by the O(nD) 
remove = []
# find the jobs
for i in range(len(jobs)):
    if jobs[i].time > jobs[i].deadline:
        remove.insert(0,i)
# remove the jobs
for i in remove: jobs.pop(i)

# here we sort the jobs in the order of increasing deadline. This is only nlog(n) time,
# so it doesn't affect our runtime (dominated by O(nD))
jobs.sort()

# here we insert a dummmy job at the beginning of jobs. This job will never get considered
# because we will start at index zero, however the reason I added it was to make the indexes
# match up the way the problem is written on paper (n jobs indexed 1 thru n).
# Now jobs[1] is the first job.
jobs.insert(0,Job(0,-1))

# now we get the max deadline by taking the last job in the lists deadline
# we add one to it because pythons range function is exclusive [start,stop),
# soby adding one we are able to consider up to and including the last deadline
max_deadline = jobs[len(jobs)-1].deadline + 1

# here we create the memo
# memo[i][d] can be interpreted as the number of jobs we can complete when considering
# the first i jobs and with a max deadline of d. We initialize with zeros everywhere
# a deadline of 0 has no jobs, considering 0 tasks we can't complete any
memo = [[0 for x in range(max_deadline)] for y in range(len(jobs))]
# back_track is another array the same size as memo, but it is used to store backtracking
# info so we can recover the optimal sequence
# backtrack[i][d] is a list either containing 2 or 3 elements.
# the first 2 elements store the previous i,d, and if there's a third
# it stores the job added at memo[i][j]
back_track = [[[0,0] for x in range(max_deadline)] for y in range(len(jobs))]

# These two for loops are where the time complexity comes from
# outer for loop is D, inner for loop is n so time complexity is O(Dn)
# for each deadline 1 <= d < d_n + 1
for d in range(1,max_deadline):
    # consider each job
    for i in range(1,len(jobs)):
        # first we check to make sure that the job can even be finished in time d
        # if we don't check for this then we could get negative indexes
        # if we see this the job cannot be included so we take memo[i][d] which is the same
        # deadline, considering one less task
        if jobs[i].time > d:
            # store memo plus backtracking info
            memo[i][d] = memo[i-1][d]
            back_track[i][d] = [i-1,d]
        else:
            # general case
            # we could use a max() call to take one of the two cases, however,
            # if we do this we can't recover the backtrack info so we take two separately
            # with an if then statement

            # first we take the case where we add the job, which is one plus the number of
            # jobs that can be completed with d-jobs[i].time as d
            add_job = (memo[i-1][d-jobs[i].time]) + 1

            # second we take the case where we don't add the job (consider same
            # deadline just one less task)
            dont_add_job = memo[i-1][d]

            # take the largest of the two
            if add_job > dont_add_job:
                # store memo plus backtracking info
                memo[i][d] = add_job
                back_track[i][d] = [i-1,d-jobs[i].time, jobs[i]]
            else:
                # store memo plus backtracking info
                memo[i][d] = dont_add_job
                back_track[i][d] = [i-1,d]
#now that the memo is done we backtrack
sequence = []

# initialize i,d to the bottom right memo spot
# we will use i,d to walk backwards
# also note that we cannot walk more than n+D times in our memo,
# so our time complexity is maintained
i = len(jobs) - 1
d = max_deadline - 1
while(memo[i][d]!=0):
    #store backtrack info in temp variable
    temp = back_track[i][d]

    # if we added a job here add it to the sequence at the first spot
    # because we are traversing in reverse
    if len(temp) == 3:
        sequence.insert(0,temp[2])
    # continue traversing
    i = temp[0]
    d = temp[1]
return sequence, memo, memo[len(jobs) - 1][max_deadline - 1]

# test cases
input_1 =[Job(5,11), Job(5,12), Job(9,10)]
sequence, memo, num_jobs = schedulable_set(input_1.copy())
print_solution(input_1, sequence, memo, num_jobs)

input_2 =[Job(1,5), Job(4,4), Job(3,1)]
sequence, memo, num_jobs = schedulable_set(input_2.copy())
print_solution(input_2, sequence, memo, num_jobs)

input_3 =[Job(0,5), Job(2,5), Job(3,3)]
sequence, memo, num_jobs = schedulable_set(input_3.copy())
print_solution(input_3, sequence, memo, num_jobs)

input_4 =[Job(2,10), Job(5,6), Job(3,6)]
sequence, memo, num_jobs = schedulable_set(input_4.copy())
print_solution(input_4, sequence, memo, num_jobs)

input_5 =[Job(1,2), Job(4,5), Job(3,6)]
sequence, memo, num_jobs = schedulable_set(input_5.copy())
print_solution(input_5, sequence, memo, num_jobs)

input_6 =[Job(2,2), Job(2,5)]
sequence, memo, num_jobs = schedulable_set(input_6.copy())
print_solution(input_6, sequence, memo, num_jobs)