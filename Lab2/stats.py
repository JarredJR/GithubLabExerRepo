fileName = input("Enter the file name: ")

try:
    with open(fileName, 'r') as f:
        content = f.read().split()

    if not content:
        print("The file is empty.")
    else:
        try:
            numbers = [float(item) for item in content]
            print("Numbers:", numbers)

            mean = sum(numbers) / len(numbers) if numbers else 0
            print("Mean:", mean)

            numbers.sort()
            midpoint = len(numbers) // 2
            if len(numbers) % 2 == 1:
                median = numbers[midpoint]
            else:
                median = (numbers[midpoint] + numbers[midpoint - 1]) / 2
            print("Median:", median)

            frequency = {}
            for number in numbers:
                frequency[number] = frequency.get(number, 0) + 1
            max_count = max(frequency.values())
            mode = [key for key, value in frequency.items() if value == max_count]
            if len(mode) == len(numbers):
                print("Mode: No mode")
            else:
                print("Mode:", mode)

        except ValueError:
            words = [item.lower() for item in content]
            print("Words:", words)

            frequency = {}
            for word in words:
                frequency[word] = frequency.get(word, 0) + 1
            max_count = max(frequency.values())
            mode = [key for key, value in frequency.items() if value == max_count]
            if len(mode) == len(words):
                print("Mode: No mode")
            else:
                print("Mode:", mode)

except FileNotFoundError:
    print("File not found. Please check the filename and try again.")

