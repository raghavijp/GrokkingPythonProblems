def binary_watch(position, hours, minutes, enabled, result):
    if enabled == 0:
        if hours <= 11 and minutes <=59:
            time = f"{hours}:{'0' if minutes < 10 else ''}{minutes}"
            result.append(time)
        return

    for i in range(position, 10):
        h , m = hours, minutes

        if i <=3:
            hours += int(pow(2, i))
        else:
            minutes += int(pow(2, i - 4))

        binary_watch(i+1, hours, minutes, enabled - 1, result)

        hours , minutes = h, m


def read_binary_watch(enabled):
    result = []
    binary_watch(0, 0, 0, enabled, result)
    return result


def main():
    inputs = [1, 2, 0, 3, 10]

    for i , value in enumerate(inputs):
        print(f"{i + 1}.\tenabled: {value}\n")
        result = read_binary_watch(value)
        print("\tPossible times: [", end="")
        print(", ".join(f'"{time}"' for time in result), end="")
        print("]\n")
        print("-" * 100)



if __name__ == "__main__":
    main()