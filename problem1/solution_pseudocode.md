# Job Scheduling Problem - Pseudocode and Explanation

## Problem Overview
- Given a list of jobs with start time, end time, and profit.
- Select the maximum number of non-overlapping jobs to maximize profit.

## Pseudocode

### Step 1. Parse the Input
- Split the input string into lines.
- Group every three lines to represent a job (start time, end time, profit).
- Store jobs as a list of tuples.

### Step 2. Sort the Jobs
- Sort jobs by profit in descending order.
- If profits are the same, sort by end time in ascending order.

### Step 3. Select Jobs
- Initialize `selected_jobs` and `total_profit`.
- For each job in the sorted list:
  - If the job's start time is after or at the end time of the last selected job:
    - Select the job.
    - Update `last_end_time` and add the job's profit to `total_profit`.

### Step 4. Calculate Remaining Jobs and Profit
- Determine the jobs that were not selected.
- Calculate the total profit of these remaining jobs.

### Step 5. Main Function - Job Scheduling
- Parse the input to get the list of jobs.
- Use the greedy algorithm to select the best jobs.
- Calculate and return the number of remaining jobs and their total profit.

## Example Input and Output

### Example 1
**Input: """
        0900
        1030
        100
        1000
        1200
        100
        1100
        1200
        100
        """**
**Output: [2,400]**

