num2words = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}


def main():
    # read file line by line and print the line
    calibration_values = []

    with open("day1/part2/input.txt", "r") as f:
    #with open("day1/part2/example_input.txt", "r") as f:
        for line in f:
            print(line)
            first_digit_index, first_digit = get_first_digit(line)
            last_digit_index, last_digit = get_last_digit(line)

            
            calibration_values.append(int(first_digit + last_digit))
    # print sum of all calibration values
    print(calibration_values)
    print(sum(calibration_values))


def get_first_digit(line):
    # Find the first digit in the line. It can be a number from 0 to 9 or a string "zero" to "nine".
    # Return the first digit as an integer.
    first_digit = None
    first_digit_index = None
    for index, char in enumerate(line):
        # if char is a digit
        if char.isdigit():
            if first_digit_index is None:
                first_digit = int(char)
                first_digit_index = index
            elif index < first_digit_index:
                first_digit = int(char)
                first_digit_index = index

    for key, value in num2words.items():
        position = line.find(value)
        if position == -1:
            continue
        if first_digit_index is None:
            first_digit = key
            first_digit_index = position
        elif position < first_digit_index:
            first_digit = key
            first_digit_index = position

    return first_digit_index, str(first_digit)


def get_last_digit(line):
    # Find the last digit in the line. It can be a number from 0 to 9 or a string "zero" to "nine".
    # Return the last digit as an integer.
    last_digit = None
    last_digit_index = None
    for index, char in enumerate(line):
        # if char is a digit
        if char.isdigit():
            if last_digit_index is None:
                last_digit = int(char)
                last_digit_index = index
            elif index > last_digit_index:
                last_digit = int(char)
                last_digit_index = index

    for key, value in num2words.items():
        position = line.find(value)
        if position == -1:
            continue
        if last_digit_index is None:
            last_digit = key
            last_digit_index = position
        elif position > last_digit_index:
            last_digit = key
            last_digit_index = position
    return last_digit_index, str(last_digit)


if __name__ == "__main__":
    main()
