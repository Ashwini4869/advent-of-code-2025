def parse_id_file(filename: str):
    ids_collection = []
    with open(filename) as file:
        ids = file.readline()
        ids_list = ids.split(",")
        for ids in ids_list:
            splits = ids.split("-")
            start_id, end_id = splits[0], splits[1]
            ids_collection.append((start_id, end_id))

    return ids_collection


def is_invalid(id: str):
    repeating_sequence_length = 1
    pattern_matched_list = []

    while repeating_sequence_length <= int(len(id) / 2):
        # print(f"Repeating sequence length: {repeating_sequence_length}")
        pattern_matched_list.append(True)
        repeating_sequence = id[:repeating_sequence_length]
        # print(f"Repeating Sequence: {repeating_sequence}")
        repeat_count = int(len(id) / repeating_sequence_length)

        if repeating_sequence * repeat_count == id:
            pattern_matched_list[-1] = True
        else:
            pattern_matched_list[-1] = False

        repeating_sequence_length += 1

    # print(f"Pattern Matched List:{pattern_matched_list}")
    return any(pattern_matched_list)


def main():
    ids_collection = parse_id_file("input.txt")
    sum_invalid = 0

    for start_id, end_id in ids_collection:
        start_id, end_id = int(start_id), int(end_id)
        for id in range(start_id, end_id + 1, 1):
            if is_invalid(str(id)):
                sum_invalid += int(id)

    return sum_invalid


if __name__ == "__main__":
    invalid_sum = main()

    print(f"The sum of invalid ids is {invalid_sum}.")
