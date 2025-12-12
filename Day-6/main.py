def parse_problem_file(filename: str):
    operands_list = [[]]
    operator_list = []
    lines = []

    with open(filename, "r") as file:
        lines = file.readlines()

    operator_list = (lines[-1]).strip("\n").split(" ")
    lines.pop()

    for i in range(len(lines)):
        lines[i] = lines[i].strip("\n ").split(" ")

    for i in range(len(lines)):
        lines[i] = [item for item in lines[i] if item]

    operands_list = [list(row) for row in zip(*lines)]
    operator_list = [item for item in operator_list if item]
    return (operands_list, operator_list)


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
