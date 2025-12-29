def parse_problem_file(filename: str):
    operands_list = [[]]
    operator_list = []
    lines = []

    with open(filename, "r") as file:
        lines = file.readlines()

    operator_list = (lines[-1]).strip("\n").split(" ")
    lines.pop()

    for i in range(len(lines)):
        lines[i] = list(lines[i].strip("\n"))

    for i in range(len(lines)):
        lines[i] = [item for item in lines[i] if item]

    operands_list = [list(row) for row in zip(*lines)]
    operator_list = [item for item in operator_list if item]

    operands_list_vertical = []

    for item in operands_list:
        max_length = len(max(item, key=len))

        # Append zeros to make all the strings of same size
        for i, sub_item in enumerate(item):
            current_element_length = len(sub_item)
            if current_element_length != max_length:
                num_zeros_to_append = max_length - current_element_length
                item[i] = "0" * num_zeros_to_append + sub_item

        temp_list = []
        for i in range(max_length - 1, -1, -1):
            column_number = ""
            for sub_item in item:
                try:
                    if sub_item[i] is not None:
                        column_number += sub_item[i]
                except IndexError:
                    pass
            temp_list.append(column_number)
        operands_list_vertical.append(temp_list)

    # Final Operands List
    operands_vertical_filtered = []

    temp_list = []
    for i, item in enumerate(operands_list_vertical):
        if len(item[0].strip()) == 0:
            operands_vertical_filtered.append(temp_list)
            temp_list = []
        elif i == len(operands_list_vertical) - 1:
            temp_list.append(item[0].strip())
            operands_vertical_filtered.append(temp_list)
        else:
            temp_list.append(item[0].strip())

    return (operands_vertical_filtered, operator_list)


def perform_operation(operand_list, operator) -> int:
    if operator == "*":
        final_value = 1
        for operand in operand_list:
            final_value *= int(operand)
        return final_value
    elif operator == "+":
        final_value = 0
        for operand in operand_list:
            final_value += int(operand)
        return final_value
    else:
        print("Provide valid operator")
        return 0


def calculate_grand_total(operands_list, operator_list) -> int:
    loop_count = len(operator_list)
    grand_total = 0

    for i in range(loop_count):
        value = perform_operation(operands_list[i], operator_list[i])
        grand_total += value
    return grand_total


if __name__ == "__main__":
    operands_list, operator_list = parse_problem_file("input.txt")
    grand_total = calculate_grand_total(operands_list, operator_list)
    print(f"The grand total value is: {grand_total}")
