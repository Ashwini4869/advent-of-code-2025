def parse_rotations_file(filename: str):
    rotations_list = []
    with open(filename) as file:
        while True:
            x = file.readline()
            if x:
                x = x.strip("\n")
                rotations_list.append(x)
            else:
                break
    return rotations_list


def rotate(rotations_list, initial_state):
    state = initial_state
    prev_state = state
    zero_click_count = 0
    zero_state_count = 0

    for rotation in rotations_list:
        prev_state = state
        if rotation.startswith("L"):
            rotation_value = rotation.strip("L")
            if len(rotation_value) > 2:
                total_rounds = int(rotation_value[:-2])
                zero_click_count += total_rounds
            state_change_rotation = int(rotation_value[-2:])
            state -= state_change_rotation

            if state < 0:
                state += 100
                if state != 0 and prev_state != 0:
                    zero_click_count += 1

        elif rotation.startswith("R"):
            rotation_value = rotation.strip("R")
            if len(rotation_value) > 2:
                total_rounds = int(rotation_value[:-2])
                zero_click_count += total_rounds
            state_change_rotation = int(rotation_value[-2:])
            state += state_change_rotation

            if state > 99:
                state -= 100
                if state != 0 and prev_state != 0:
                    zero_click_count += 1

        if state == 0:
            zero_state_count += 1

    return zero_click_count + zero_state_count


if __name__ == "__main__":
    initial_state = 50

    rotations_list = parse_rotations_file(filename="input.txt")

    password = rotate(rotations_list, initial_state)

    print(f"The password to unlock the door is {password}")
