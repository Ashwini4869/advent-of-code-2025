def parse_batteries_file(filename: str):
    bank_list = []
    with open(filename) as file:
        while True:
            x = file.readline()
            if x:
                x = x.strip("\n")
                bank_list.append(x)
            else:
                break
    return bank_list


def largest_possible_joltage(bank: str):
    max_possible_jolts = ""
    batteries_list = [int(i) for i in bank]
    left = 0
    for i in range(11, 0, -1):
        valid_batteries_list = batteries_list[left:-i]
        max_value = max(valid_batteries_list)
        max_possible_jolts += str(max_value)
        max_index = valid_batteries_list.index(max_value)
        left += max_index + 1

    max_possible_jolts += str(max(batteries_list[left:]))

    return int(max_possible_jolts)


def total_output_joltage(bank_list: list):
    total_output_joltage = 0
    for bank in bank_list:
        total_output_joltage += largest_possible_joltage(bank)

    return total_output_joltage


def main():
    bank_list = parse_batteries_file("input.txt")
    sum_output_joltage = total_output_joltage(bank_list)
    print(f"The total output joltage is: {sum_output_joltage}")


if __name__ == "__main__":
    main()
