import numpy as np

EMITTER_POSITIONS = [str(c) for c in range(1, 7)]
OFFSETS = {
    1: (1, 0),
    2: (1, 1),
    3: (-1, 1),
    4: (-1, 0),
    5: (-1, -1),
    6: (1, -1)
}


def find_emitter_pos(hexagon: np.ndarray):
    a = [candidate for candidate in [np.where(hexagon == pos) for pos in EMITTER_POSITIONS] if candidate[0].size > 0]
    return [(int(pair[0][0]), int(pair[1][0])) for pair in a]


def process_beam(dx, dy, ex, ey, hexagon: np.ndarray, results: np.ndarray):
    x, y = ex, ey
    while True:
        x += dx
        y += dy

        if hexagon[y,x] == "*" or hexagon[y,x] in EMITTER_POSITIONS:
            return
        elif hexagon[y,x] == "-":
            continue
        else:
            results[y,x] += 1


def process_hexagon(radius: int, rows: int, cols: int, hexagon: np.ndarray):
    results = np.zeros((rows, cols)).astype(int)
    emitter_positions = find_emitter_pos(hexagon)

    for ey, ex in emitter_positions:
        e = int(hexagon[ey,ex])
        dx, dy = OFFSETS[e]

        process_beam(dx, dy, ex, ey, hexagon, results)

    for row in results:
        print("".join(list(row.astype(str))))

    c_matter_positions = np.where(results == 2)
    d_matter_positions = np.where(results > 2)

    print("c matter pos: ", c_matter_positions)
    print("d matter pos: ", d_matter_positions)

    hexagon[c_matter_positions] = "M"
    hexagon[d_matter_positions] = "O"

    for row in hexagon:
        print("".join(row))


def main():
    level_num = 3
    level_dir = f"./level{level_num}"
    stages = [level_dir + "/" + l for l in [
        # f"in_level-{level_num}_0-example.txt",
        f"in_level-{level_num}_1-small.txt",
        f"in_level-{level_num}_2-large.txt"
    ]]

    for stage in stages[1:2]:
        print(stage)
        with open(stage, 'r') as f:
            input_ = f.read()
            input_ = input_[4:-1]  # skip line number header

        out = ""
        for example in input_.split("\n\n"):
            example = example.splitlines()
            for row in example:
                print(row)
            radius, rows, cols = map(int, example[0].split(" "))
            hexagon = np.array([list(row) for row in example[1:]])
            process_hexagon(radius, rows, cols, hexagon)
            out += "\n".join(["".join(row) for row in hexagon])
            out += "\n\n"

        out_file = stage.replace(".txt", ".out")
        with open(out_file, 'w') as f:
            f.write(out)


if __name__ == '__main__':
    main()
