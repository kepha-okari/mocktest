def read_input(input_file):
    """
    Reads the input from the file.
    Returns the number of employees and a dictionary of goodies with their prices.
    """
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    # Extract the number of employees
    num_employees = int(lines[0].split(":")[1].strip())
    
    # Extract the goodies and their prices
    goodies = {}
    for line in lines[2:]:
        if line.strip():
            name, price = line.split(":")
            goodies[name.strip()] = int(price.strip())
    
    return num_employees, goodies

def sort_goodies_by_price(goodies):
    """
    Sorts the goodies by their price.
    Returns a sorted list of tuples (goodie_name, price).
    """
    sorted_goodies = sorted(goodies.items(), key=lambda x: x[1])
    return sorted_goodies

def find_minimum_difference_goodies(sorted_goodies, num_employees):
    """
    Finds the subset of goodies that minimizes the difference between the highest and lowest prices.
    Returns the subset of goodies and the minimum difference.
    """
    min_diff = float('inf')
    min_index = 0
    
    # Sliding window to find the minimum difference subset,
    #keep sliding the window in the sorted list until the subset with least difference is found
    for i in range(len(sorted_goodies) - num_employees + 1):
        current_diff = sorted_goodies[i + num_employees - 1][1] - sorted_goodies[i][1]
        if current_diff < min_diff:
            min_diff = current_diff
            min_index = i
    
    selected_goodies = sorted_goodies[min_index:min_index + num_employees]
    return selected_goodies, min_diff

def write_output(output_file, selected_goodies, min_diff):
    """
    Writes the selected goodies and the minimum difference to the output file.
    """
    with open(output_file, 'w') as file:
        file.write("The goodies selected for distribution are:\n\n")
        for goodie, price in selected_goodies:
            file.write(f"{goodie}: {price}\n")
        file.write(f"\nAnd the difference between the chosen goodie with highest price and the lowest price is {min_diff}\n")

def main(input_file, output_file):
    # Step 1: Read the input from the file
    num_employees, goodies = read_input(input_file)
    
    # Step 2: Sort the goodies by price
    sorted_goodies = sort_goodies_by_price(goodies)
    
    # Step 3: Find the subset of goodies with the minimum difference
    selected_goodies, min_diff = find_minimum_difference_goodies(sorted_goodies, num_employees)
    
    # Step 4: Write the output to the file
    write_output(output_file, selected_goodies, min_diff)

# Example usage
input_file = "sample_input.txt"
output_file = "sample_output.txt"
main(input_file, output_file)
