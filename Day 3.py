# convert from binary to numeric
def convert_binary(binary_string):
    print(binary_string)
    return int(binary_string, 2)


def generate_binary(is_gamma):
    # Open diagnostic report. If is_Gamma is true, find the most common integer.
    # If it is false we will find the least common.
    with open("resources/diagnostic report", 'r') as f:
        report = f.readlines()
        binary_list = []
        # Iterate through the report assuming all entries have the same length
        for i in range(len(report[0].strip())):
            # Add the binary for each column to a new list
            column_data = []
            for line in report:
                column_data.append(int(line[i]))

            # Sum the number of ones and zeroes in the previously created list
            number_of_ones = 0
            number_of_zeros = 0
            for x in column_data:

                if x == 1:
                    number_of_ones += 1

                if x == 0:
                    number_of_zeros += 1
                # Produce binary for Gamma function
            if is_gamma is True:

                if number_of_zeros > number_of_ones:
                    binary_list.insert(i, 0)

                else:
                    binary_list.insert(i, 1)

            if is_gamma is False:

                if number_of_zeros > number_of_ones:
                    binary_list.insert(i, 1)

                else:
                    binary_list.insert(i, 0)

        return "".join(map(str, binary_list))


gamma_rate = convert_binary(generate_binary(True))

print(f"The Gamma rate is: {gamma_rate}\n")

epsilon_rate = convert_binary(generate_binary(False))

print(f"The Gamma rate is: {epsilon_rate}\n")

print(f"The power consumption of the submarine is: {gamma_rate * epsilon_rate}")

