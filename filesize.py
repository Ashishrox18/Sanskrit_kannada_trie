import os

def calculate_size_difference(file1, file2):
    size1 = os.path.getsize(file1)
    size2 = os.path.getsize(file2)

    difference = size1 - size2
    percentage_decrease = (difference / size1) * 100

    return difference, percentage_decrease

# Example usage
file1 = './kannadaexcel/uniqsansk.txt'
file2 = './kannadaexcel/sansletspin.txt'

difference, percentage_decrease = calculate_size_difference(file1, file2)

print(f"Difference in size: {difference} bytes")
print(f"Percentage decrease: {percentage_decrease}%")
