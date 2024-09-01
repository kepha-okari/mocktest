# Solution 2 Pseudocode

## Overview
This solution selects goodies for employees such that the difference between the highest and lowest prices in the selected subset is minimized.

## Process

### Step  1. **Read Input File**
   - **Purpose:** Read the number of employees and the list of goodies with their prices from an input file.
   - **Steps:**
     1. Open the input file.
     2. Extract the number of employees from the first line.
     3. Extract the goodies and their prices from the subsequent lines.
     4. Store the goodies and prices in a dictionary.

### Step 2. **Sort Goodies by Price**
   - **Purpose:** Sort the goodies based on their prices in ascending order.
   - **Steps:**
     1. Use a sorting function to order the dictionary by price.
     2. Store the sorted goodies as a list of tuples.

### Step 3. **Find the Minimum Difference Subset**
   - **Purpose:** Identify the subset of `M` consecutive goodies that minimizes the difference between the highest and lowest prices.
   - **Steps:**
     1. Use a sliding window approach to iterate over the sorted list.
     2. For each window, calculate the difference between the first and last items.
     3. Track and return the minimum difference and the corresponding subset of goodies.

### Step 4. **Write Output File**
   - **Purpose:** Write the selected goodies and the calculated minimum difference to an output file.
   - **Steps:**
     1. Open the output file.
     2. Write the selected goodies with their prices.
     3. Write the minimum difference between the highest and lowest prices.

## Accessing Files

### 1. **Input File (`sample_input.txt`)**
   - **Content:** Contains the number of employees and a list of goodies with their prices.
   - **Example:**
     ```plaintext
     Number of employees: 4
     Goodies and Prices:
     Fitbit Plus: 7980
     IPods: 22349
     MI Band: 999
     Cult Pass: 2799
     Macbook Pro: 229900
     Digital Camera: 11101
     Alexa: 9999
     Sandwich Toaster: 2195
     Microwave Oven: 9800
     Scale: 4999
     ```

### 2. **Output File (`sample_output.txt`)**
   - **Content:** Contains the selected goodies for distribution and the minimum price difference.
   - **Example:**
     ```plaintext
     The goodies selected for distribution are:

     Fitbit Plus:
