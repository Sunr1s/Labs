# Stubs for each function
def input_data(test_case):
    N, A = test_case
    return N, A

def filter_even_numbers(N, A):
    # Stub implementation
    B = [x for x in A if x % 2 == 0]
    return len(B), B

def sort_even_numbers(B):
    # Stub implementation
    B.sort()
    return B

def output_result(N, B):
    # Stub implementation
    print(f"Size of B = {N}, B = {B}")

def main(test_case):
    N, A = input_data(test_case)
    size, B = filter_even_numbers(N, A)
    B = sort_even_numbers(B)
    output_result(size, B)

# Test cases
test_cases = [
    (5, [2, 4, 6, 8, 10]),
    (5, [1, 3, 5, 7, 9]),
    (6, [1, 2, 3, 4, 5, 6]),
    (7, [-3, 2, -1, 4, 5, -6, 8]),
    (1, [3])
]

# Execute testing using a loop
for test_case in test_cases:
    print(f"Testing with input: {test_case}")
    main(test_case)
    print()
