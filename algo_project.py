import numpy as np
# Step 2: Input Adjacency Matrix
def input_adjacency_matrix():
    # Example adjacency matrix (replace this with your own input method)
    adjacency_matrix = np.array([
        [0, 1, 3, 0],
        [0, 0, 0, 2],
        [0, 0, 0, 5],
        [0, 0, 0, 0]
    ])
    return adjacency_matrix
# Step 3: Compute Matrix Exponential
def compute_matrix_exponential(adjacency_matrix):
    # Using matrix exponential formula to compute
    matrix_exp = np.identity(len(adjacency_matrix))  # Initialize matrix exponential with identity matrix
    k = 1
    while k <= 10:  # You can change the number of iterations as needed
        matrix_exp += np.linalg.matrix_power(adjacency_matrix, k) / np.math.factorial(k)
        k += 1
    return matrix_exp
# Step 4: Extract Relevant Elements
def extract_relevant_elements(matrix_exp):
    # Extracting relevant elements (assuming interest in certain positions)
    relevant_elements = matrix_exp[0][1], matrix_exp[0][2], matrix_exp[1][3]
    return relevant_elements
# Step 5: Determine Path Costs
def determine_path_costs(relevant_elements):
    # Example costs calculation (modify this based on your logic)
    path_costs = [elem * 2 for elem in relevant_elements]
    return path_costs
# Step 6: Identify Shortest Path
def identify_shortest_path(path_costs):
    shortest_path_index = np.argmin(path_costs)
    return shortest_path_index, path_costs[shortest_path_index]
# Main process
def main():
    # Step 2: Input Adjacency Matrix
    adjacency_matrix = input_adjacency_matrix()
    # Step 3: Compute Matrix Exponential
    matrix_exp = compute_matrix_exponential(adjacency_matrix)
    # Step 4: Extract Relevant Elements
    relevant_elements = extract_relevant_elements(matrix_exp)
    # Step 5: Determine Path Costs
    path_costs = determine_path_costs(relevant_elements)
    # Step 6: Identify Shortest Path
    shortest_path_index, shortest_path_cost = identify_shortest_path(path_costs)
    # Step 7: End
    print("Matrix Exponential:", matrix_exp)
    print("Relevant Elements:", relevant_elements)
    print("Path Costs:", path_costs)
    print("Shortest Path Index:", shortest_path_index)
    print("Shortest Path Cost:", shortest_path_cost)

main()