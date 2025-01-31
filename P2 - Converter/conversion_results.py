"""Actividad 4.2_Ejercisio 2.Conversion Results"""
import sys
import time


def to_binary(n):
    """ Algorithim for converting binary"""
    binary = ""

    if n == 0:
        return "0"
    if n < 0:
        return float('nan')
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary


def to_hexadecimal(n):
    """Same Algorithim for convertic decimals to hex"""
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""

    if n == 0:
        return "0"
    if n < 0:
        return float('nan')
    while n > 0:
        hexadecimal = hex_chars[n % 16] + hexadecimal
        n = n // 16
    return hexadecimal


def process_file(file_name):
    """Open text file and process datatypes"""
    results = []
    with open(file_name, 'r', encoding="utf-8") as file:
        for line in file:
            try:
                number = int(line.strip())
                binary = to_binary(number)
                hexadecimal = to_hexadecimal(number)
                results.append((number, binary, hexadecimal))
            except ValueError:
                print(f"Invalid data found in file {file_name}: {line.strip()}")
    return results


def main():
    """Main Call"""
    start_time = time.time()

    if len(sys.argv) < 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    all_results = []

    for file_name in sys.argv[1:]:
        results = process_file(file_name)
        all_results.extend(results)


    with open("ConvertionResults.txt", 'w', encoding="utf-8") as output_file:
        output_file.write(f"{'Number':<15}{'Binary':<35}{'Hexadecimal':<15}\n")
        output_file.write("=" * 65 + "\n")
        for number, binary, hexadecimal in all_results:
            output_file.write(f"{number:<15}{binary:<35}{hexadecimal:<15}\n")
            print(f"{number:<15}{binary:<35}{hexadecimal:<15}")

    elapsed_time = time.time() - start_time
    print(f"Time elapsed: {elapsed_time} seconds")

    with open("ConvertionResults.txt", 'a', encoding="utf-8") as output_file:
        output_file.write(f"\nTime elapsed: {elapsed_time} seconds\n")


if __name__ == "__main__":
    main()
