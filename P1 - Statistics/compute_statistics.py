"""Actividad 4.2_Ejercisio 1.Compute Statistics"""
import sys
import time


def read_numbers_from_file(file_path):
    """Import text files"""
    numbers = []
    with open(file_path, 'r', encoding="utf-8") as file:
        for line in file:
            try:
                number = float(line.strip())
                numbers.append(number)
            except ValueError:
                print(f"Invalid data found and skipped: {line.strip()}")
    return numbers


def compute_statistics(numbers):
    """Math under the hood"""
    n = len(numbers)
    mean = sum(numbers) / n
    sorted_numbers = sorted(numbers)

    if n % 2 == 0:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        median = sorted_numbers[n // 2]

    # Mode calculation without using libraries
    frequency = {}
    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    mode = max(frequency, key=frequency.get)

    variance = sum((x - mean) ** 2 for x in numbers) / n
    std_dev = variance ** 0.5

    return {
        "COUNT": n,
        "MEAN": mean,
        "MEDIAN": median,
        "MODE": mode,
        "SD": std_dev,
        "VARIANCE": variance,
    }


def write_statistics_to_file(statistics_list, elapsed_time):
    """Write result summary file"""
    with open('StatisticsResults.txt', 'w', encoding="utf-8") as file:
        file.write("File\tCOUNT\tMEAN\tMEDIAN\tMODE\tSD\tVARIANCE\n")
        for stats in statistics_list:
            file.write(
                f"{stats['file']}"
                f"\t{stats['COUNT']}"
                f"\t{stats['MEAN']}"
                f"\t{stats['MEDIAN']}"
                f"\t{stats['MODE']}"
                f"\t{stats['SD']}"
                f"\t{stats['VARIANCE']}\n")
        file.write(f"Elapsed time: {elapsed_time} seconds\n")


def main():
    """Main Call"""
    if len(sys.argv) < 2:
        print("Usage: python compute_statistics.py fileWithData1.txt fileWithData2.txt ...")
        sys.exit(1)

    files = sys.argv[1:]

    statistics_list = []

    start_time = time.time()

    for file_path in files:
        numbers = read_numbers_from_file(file_path)

        if not numbers:
            print(f"No valid numbers found in the file: {file_path}")
            continue

        statistics = compute_statistics(numbers)
        statistics['file'] = file_path
        statistics_list.append(statistics)

        print(f"\n\nProcessed file: {file_path}")
        for key, value in statistics.items():
            if key != 'file':
                print(f"{key}: {value}")



    elapsed_time = time.time() - start_time

    print(f"Elapsed time: {elapsed_time} seconds")

    write_statistics_to_file(statistics_list, elapsed_time)


if __name__ == "__main__":
    main()
