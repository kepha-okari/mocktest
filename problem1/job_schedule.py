
def parse_input(input_data):
    """
    Parses the input data into a list of job tuples.

    Args:
        input_data: A string representing the input data.

    Returns:
        A list of tuples, each containing (start_time, end_time, profit).
    """
    lines = input_data.strip().splitlines()
    num_jobs = len(lines) // 3 
    jobs = []

    for i in range(0, len(lines), 3):
        start_time = int(lines[i].strip())
        end_time = int(lines[i + 1].strip())
        profit = int(lines[i + 2].strip())
        jobs.append((start_time, end_time, profit))
    
    return jobs


def select_jobs(jobs):
    """
    Selects jobs to maximize profit using a greedy algorithm.
    Args:
        jobs: A list of tuples, each containing (start_time, end_time, profit).
    Returns:
        A tuple containing a list of selected jobs and the total profit.
    """
    # Sort jobs by profit in descending order and by end time in ascending order
    jobs.sort(key=lambda x: (-x[2], x[1]))

    selected_jobs = []
    last_end_time = 0
    total_earnings = 0

    for start_time, end_time, profit in jobs:
        if start_time >= last_end_time:
            selected_jobs.append((start_time, end_time, profit))
            last_end_time = end_time
            total_earnings += profit

    return selected_jobs, total_earnings



def show_selected_jobs(input_data):
    """
    Calculates the number of remaining jobs and their total earnings.

    Args:
        input_data: A string representing the input data.

    Returns:
        A tuple containing the number of remaining jobs and their total earnings.
    """
    jobs = parse_input(input_data)
    selected_jobs, _ = select_jobs(jobs)
    # selected_jobs_set = set(selected_jobs)
    # num_jobs = len(jobs)
    # remaining_jobs = num_jobs - len(selected_jobs)
    # remaining_earnings = sum(profit for start_time, end_time, profit in jobs if (start_time, end_time, profit) not in selected_jobs_set)

    return selected_jobs
    


def calculate_remaining(jobs, selected_jobs):
    """
    Calculates the number of remaining jobs and their total earnings.
    Args:
        jobs: A list of tuples, each containing (start_time, end_time, profit).
        selected_jobs: A list of tuples, each containing (start_time, end_time, profit) of selected jobs.
    Returns:
        A tuple containing the number of remaining jobs and their total earnings.
    """
    selected_jobs_set = set(selected_jobs)
    num_jobs = len(jobs)
    remaining_jobs = num_jobs - len(selected_jobs)
    remaining_earnings = sum(profit for start_time, end_time, profit in jobs if (start_time, end_time, profit) not in selected_jobs_set)

    return remaining_jobs, remaining_earnings
    

def job_scheduling(input_data):
    """
    Main function to find the optimal job schedule and remaining jobs/earnings.

    Args:
        input_data: A string representing the input data.

    Returns:
        A list containing the number of remaining jobs and the total earnings of those jobs.
    """
    jobs = parse_input(input_data)
    selected_jobs, _ = select_jobs(jobs)
    remaining_jobs, remaining_earnings = calculate_remaining(jobs, selected_jobs)
    
    return [remaining_jobs, remaining_earnings]


if __name__ == "__main__":

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
    job_scheduling(input_data1)
    print("Sample Output 1:", job_scheduling(input_data1))  # Expected Output: [2, 400]
    print("Selected Jobs:", show_selected_jobs(input_data1),"\n")
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
    print("Selected Jobs:", show_selected_jobs(input_data2),"\n")
    job_scheduling(input_data2)

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
    print("Selected Jobs:", show_selected_jobs(input_data3),"\n")
    job_scheduling(input_data3)

    input_data4 = """
    0900
    1000
    100
    1000
    1100
    200
    1100
    1200
    150
    """
    print("Sample Output 4:", job_scheduling(input_data4))  # Expected Output: [1, 100]
    print("Selected Jobs:", show_selected_jobs(input_data4),"\n")

    input_data5 = """
    0900
    0930
    110
    0930
    1000
    70
    1000
    1100
    90
    1100
    1200
    110
    """
    print("Sample Output 5:", job_scheduling(input_data5))  # Expected Output: [1, 100]
    print("Selected Jobs:", show_selected_jobs(input_data5),"\n")