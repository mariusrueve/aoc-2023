def main():
    # read file line by line and print the line
    calibration_values = []

    with open('day1/part1/input.txt', 'r') as f:
        for line in f:
            first_digit = None
            last_digit = None
            for char in line:
                # if char is a digit
                if char.isdigit():
                    if first_digit is None:
                        first_digit = char
                    else:
                        last_digit = char
            if first_digit is not None and last_digit is None:
                calibration_values.append(int(first_digit + first_digit))
            elif first_digit is not None and last_digit is not None:
                calibration_values.append(int(first_digit + last_digit))
            else:
                continue
    # print sum of all calibration values
    print(sum(calibration_values))


if __name__ == '__main__':
    main()