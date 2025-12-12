def parse_ingredients_file(filename: str):
    ingredient_id_ranges = []
    available_ingredients = []

    with open(filename, "r") as file:
        lines = file.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].strip("\n")

    blank_line_index = lines.index("")
    ingredient_id_ranges = lines[:blank_line_index]
    # Change the min-max format range to (min,max)
    for i, item in enumerate(ingredient_id_ranges):
        item_tuple_list = item.split("-")
        item_tuple = (item_tuple_list[0], item_tuple_list[1])
        ingredient_id_ranges[i] = item_tuple

    available_ingredients = lines[blank_line_index + 1 :]

    return (ingredient_id_ranges, available_ingredients)


def count_fresh_available_ingredients(ingredients_data):
    total_fresh_available_ingredients = 0
    ingredient_id_ranges, available_ingredients = ingredients_data

    for ingredient_id in available_ingredients:
        for range in ingredient_id_ranges:
            min, max = range
            if int(min) <= int(ingredient_id) <= int(max):
                total_fresh_available_ingredients += 1
                break

    return total_fresh_available_ingredients


def print_info(ingredients_data):
    ingredients_id_ranges, _ = ingredients_data
    normal_data = 0
    data_with_single_element = 0
    abnormal_data = 0

    for id_range in ingredients_id_ranges:
        i_min, i_max = int(id_range[0]), int(id_range[1])
        if i_min < i_max:
            normal_data += 1
        elif i_min > i_max:
            abnormal_data += 1
        else:
            data_with_single_element += 1

    print("Normal Data: ", normal_data)
    print("Abnormal Data: ", abnormal_data)
    print("Data with single element: ", data_with_single_element)


def count_all_fresh_ingredients(ingredients_data):
    ingredients_id_ranges, _ = ingredients_data
    total_fresh_ingredients = 0

    ingredients_id_ranges.sort(key=lambda x: int(x[0]))

    loop_count = 0

    while True:
        overlap_flag = False
        loop_count += 1
        i, j = 0, 0

        while True:
            if i < len(ingredients_id_ranges) - 1:
                j = i + 1
                first_range = ingredients_id_ranges[i]
                second_range = ingredients_id_ranges[j]
                min_i, max_i = int(first_range[0]), int(first_range[1])
                min_j, max_j = int(second_range[0]), int(second_range[1])
                if (
                    (min_i <= min_j <= max_i)
                    or (min_i <= max_j <= max_i)
                    or (min_j <= min_i <= max_j)
                    or (min_j <= max_i <= max_j)
                ):
                    union_i, union_j = str(min(min_i, min_j)), str(max(max_i, max_j))
                    union_range = (union_i, union_j)
                    ingredients_id_ranges.remove(first_range)
                    ingredients_id_ranges.remove(second_range)
                    ingredients_id_ranges.append(union_range)
                    ingredients_id_ranges.sort(key=lambda x: int(x[0]))
                    overlap_flag = True
                else:
                    pass
                i += 1

            else:
                break

        loop_count += 1
        if overlap_flag is False:
            break

    for item in ingredients_id_ranges:
        total_fresh_ingredients += int(item[1]) - int(item[0]) + 1

    return total_fresh_ingredients


if __name__ == "__main__":
    ingredients_data = parse_ingredients_file("input.txt")
    print("Total fresh ingredients:", count_all_fresh_ingredients(ingredients_data))
