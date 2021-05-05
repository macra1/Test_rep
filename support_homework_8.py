black = "\u2B1B"
white = "\u2B1C"


num_storage = {
    0: {
        0: [black, white, white, black],
        1: [white, black, black, white],
        2: [white, black, black, white],
        3: [white, black, black, white],
        4: [white, black, black, white],
        5: [white, black, black, white],
        6: [black, white, white, black]
    },
    1: {
        0: [black, black, black, white],
        1: [black, black, black, white],
        2: [black, black, black, white],
        3: [black, black, black, white],
        4: [black, black, black, white],
        5: [black, black, black, white],
        6: [black, black, black, white]
    },
    2: {
        0: [white, white, white, white],
        1: [black, black, black, white],
        2: [black, black, black, white],
        3: [white, white, white, white],
        4: [white, black, black, black],
        5: [white, black, black, black],
        6: [white, white, white, white]
    },
    3: {
        0: [white, white, white, white],
        1: [black, black, black, white],
        2: [black, black, black, white],
        3: [white, white, white, white],
        4: [black, black, black, white],
        5: [black, black, black, white],
        6: [white, white, white, white]
    },
    4: {
        0: [white, black, black, white],
        1: [white, black, black, white],
        2: [white, black, black, white],
        3: [white, white, white, white],
        4: [black, black, black, white],
        5: [black, black, black, white],
        6: [black, black, black, white]
    },
    5: {
        0: [white, white, white, white],
        1: [white, black, black, black],
        2: [white, black, black, black],
        3: [white, white, white, white],
        4: [black, black, black, white],
        5: [black, black, black, white],
        6: [white, white, white, white]
    },
    6: {
        0: [white, white, white, white],
        1: [white, black, black, black],
        2: [white, black, black, black],
        3: [white, white, white, white],
        4: [white, black, black, white],
        5: [white, black, black, white],
        6: [white, white, white, white]
    },
    7: {
        0: [white, white, white, white],
        1: [black, black, black, white],
        2: [black, black, black, white],
        3: [black, black, black, white],
        4: [black, black, black, white],
        5: [black, black, black, white],
        6: [black, black, black, white]
    },
    8: {
        0: [black, white, white, black],
        1: [white, black, black, white],
        2: [white, black, black, white],
        3: [white, white, white, white],
        4: [white, black, black, white],
        5: [white, black, black, white],
        6: [black, white, white, black]
    },
    9: {
        0: [white, white, white, white],
        1: [white, black, black, white],
        2: [white, black, black, white],
        3: [white, white, white, white],
        4: [black, black, black, white],
        5: [black, black, black, white],
        6: [white, white, white, white]
    }
}


if __name__ == "__main__":
    for elem in num_storage:
        for i in num_storage[elem]:
            answer = ""
            for a in num_storage[elem][i]:
                answer += a
            print(answer)
        print()