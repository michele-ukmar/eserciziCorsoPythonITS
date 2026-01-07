def next_generation(current_generation):
    pass

def test_next_generation():
    current_generation = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ]
    expected_next_generation = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]
    assert next_generation(current_generation) == expected_next_generation

# test_next_generation()

def next_generation(current_generation):
    next_generation = []
    for i in range(len(current_generation)):
        row = []
        for j in range(len(current_generation[i])):
            cell = current_generation[i][j]
            # implementare le regole del gioco della vita qui
            row.append(cell)
        next_generation.append(row)
    return next_generation

# test_next_generation()


def next_generation(current_generation):
    next_generation = []
    for i in range(len(current_generation)):
        row = []
        for j in range(len(current_generation)):
            cell = current_generation[i][j]
            # implementare le regole del gioco della vita qui
            row.append(cell)
        next_generation.append(row)

test_next_generation()