# Job class to store information related to each job
class Job():
    def __init__(self, time, weight, name):
        self.name = name # name of the job, not really necessary, but helpful for visualizing how the order changes (can be thought of as k)
        self.time = time # t_k or the amount of time the job takes to complete
        self.weight = weight # w_k, represents the job’s importance to the business
        self.weight_divided_by_time = weight / time # w_k /t_k , if we sort the jobs by this value in decreasing
                                                    # order we get the optimal order of jobs to maximize weighted 
                                                    # sum of completion times, so we calculate it as soon as the job
                                                    # is created (O(1) time per job, so linear w/ respect to # jobs)
        self.completion_time = -1   # a variable to store the completion time of the job, once the optimal order has been found, starts as -1

    def get_weight_divided_by_time(self): return self.weight_divided_by_time # this is a function that returns the weight_divided_by_time,
                                                                             # for a job. We use it to sort the jobs on in 
                                                                             # minimize_weighted_sum_of_completion_times

# print_jobs is just a class that prints out a list of jobs, and the attributes of each job
def print_jobs(jobs_in):
    print("------- START print_jobs --------")
    for job in jobs_in:
        print("           name:", job.name) # print name of job
        print("completion_time:", job.completion_time) # print completion_time of job
        print("            w/t:", job.get_weight_divided_by_time()) # print w_k/t_k of job
        print("              w:", job.weight) # print w_k of job
        print("              t:", job.time, "\n") # print t_k of job
    print("------- END print_jobs --------\n")

#This is the actual algorithm. It takes in a list of jobs, and sorts them in descending order based on the w_k/t_k of each job.
def minimize_weighted_sum_of_completion_times(jobs):
    jobs.sort(key = Job.get_weight_divided_by_time, reverse = True) # This line uses the sort function in python, 
                                                                    # along with the key functionality and get_weight_divided_by_time
                                                                    # function defined in the job class to sort the jobs by w_k/t_k
                                                                    # in descending order, which is why reverse is set to true.
                                                                    # This is a sorting algo that runs in O(nlogn) with respect to
                                                                    # the number of jobs.
    running_time = 0 # variable used to store how long it has been to set the completion time variables
    weighted_sum_of_completion_times = 0 # variable used to store weighted sum of completion times
    for job in jobs:
        running_time += job.time # update running time
        job.completion_time = running_time # set the completion time of the job
        weighted_sum_of_completion_times += job.weight * job.completion_time # add c_k * w_k for this job, to the weighted sum
    return jobs, weighted_sum_of_completion_times

# This function just runs a test case
def print_test_run(jobs_in):
    print("\n\n=====================", "Print Test Run", "=====================")
    print("jobs BEFORE optimization: ")
    print_jobs(jobs_in)
    job_order, weighted_sum_of_completion_times = minimize_weighted_sum_of_completion_times(jobs_in)
    print("jobs AFTER optimization sorting: ")
    print_jobs(job_order)
    print("WEIGHTED SUM OF COMPLETION TIMES:", weighted_sum_of_completion_times)

# example from the P.S.
jobs1 = [Job(3,2, "job 1"), Job(1,10, "job 2")]
# larger example with more jobs
jobs2 = [Job(3,2, "job 1"), Job(1,10, "job 2"), Job(5,2, "job 3"), Job(25,3, "job 4"), Job(2,70, "job 5")]

print_test_run(jobs1) # minimized weighted sum of completion times = 18, like P.S. says it should be
print_test_run(jobs2) # minimized weighted sum of completion times = 312

