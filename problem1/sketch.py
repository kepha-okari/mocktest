def job_scheduling(input_data):
    """
    Finds the optimal job schedule to maximize earnings.

    Args:
        input_data: A string representing the input data.

    Returns:
        A list containing the number of jobs left and the total earnings of those jobs.
    """
    
    # Split input data into lines
    lines = input_data.strip().splitlines()
    
    # Determine the number of jobs based on the number of lines
    num_jobs = len(lines) // 3
    
    # Initialize a list to hold job details
    jobs = []
    
    # Extract job details from input data
    for i in range(0, len(lines), 3):
        start_time = int(lines[i].strip())
        end_time = int(lines[i + 1].strip())
        profit = int(lines[i + 2].strip())
        jobs.append((start_time, end_time, profit))
    
    # Sort jobs by profit in descending order and by end time in ascending order
    jobs.sort(key=lambda x: (-x[2], x[1]))
    
    # List to store selected jobs
    selected_jobs = []
    last_end_time = 0
    total_earnings = 0
    
    # Select jobs based on maximum profit and non-overlapping constraint
    for start_time, end_time, profit in jobs:
        if start_time >= last_end_time:
            selected_jobs.append((start_time, end_time, profit))
            last_end_time = end_time
            total_earnings += profit
    
    # Calculate remaining jobs and earnings
    selected_jobs_set = set(selected_jobs)
    remaining_jobs = num_jobs - len(selected_jobs)
    remaining_earnings = sum(profit for start_time, end_time, profit in jobs if (start_time, end_time, profit) not in selected_jobs_set)
    
    return [remaining_jobs, remaining_earnings]

# Sample Input 1
input_data1 = """
0900
1030
100
1000
1200
500
1100
1200
300
"""
print("Sample Output 1:", job_scheduling(input_data1))  # Expected Output: [2, 400]

# Sample Input 2
input_data2 = """
0900
1000
250
0945
1200
550
1130
1500
150
"""
print("Sample Output 2:", job_scheduling(input_data2))  # Expected Output: [2, 400]

# Sample Input 3
input_data3 = """
0900
1030
100
1000
1200
100
1100
1200
100
"""
print("Sample Output 3:", job_scheduling(input_data3))  # Expected Output: [1, 100]
