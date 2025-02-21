"""
File: stats.py
Computes the mean, median, and mode of a set of numbers or words.
"""

def mean(numbers):
    """Computes the mean of a list of numbers."""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    """Computes the median of a list of numbers."""
    if len(numbers) == 0:
        return 0
    numbers.sort()
    midpoint = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return numbers[midpoint]
    else:
        return (numbers[midpoint] + numbers[midpoint - 1]) / 2

def mode(items):
    """Computes the mode of a list of numbers or words."""
    if len(items) == 0:
        return 0
    theDictionary = {}
    for item in items:
        theDictionary[item] = theDictionary.get(item, 0) + 1
    
    max_count = max(theDictionary.values())
    mode = [key for key, value in theDictionary.items() if value == max_count]

    if max_count > 1:
        return mode
    else:
        return "No mode"

def main():
    """Main function to test mean, median, and mode."""
    user_input = input("Enter numbers or words separated by spaces: ")
    items = user_input.split()

    # Check if input is all numbers
    try:
        numbers = [float(item) for item in items]
        print("Numbers:", numbers)
        print("Mean:", mean(numbers))
        print("Median:", median(numbers))
        print("Mode:", mode(numbers))
    except ValueError:
        print("Words:", items)
        print("Mode:", mode(items))

if __name__ == "__main__":
    main()
