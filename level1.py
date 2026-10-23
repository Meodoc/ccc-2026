def main():
    def height(n):
        return n * 2 + 1

    def width(n):
        return n * 4 + 1

    def diag(n: int, row: int):
        delta = abs(n - row)
        return delta, width(n) - delta - 1

    files = ["level1/in_level-1_1-small.txt", "level1/in_level-1_2-large.txt"]

    for file in files:
        print(file)
        with open(file, 'r') as f:
            lines = f.readlines()

        out_file = file.replace(".txt", ".out")
        out = ""

        for ex in lines[1:]:
            ex = int(ex)

            for r in range(height(ex)):
                symbol = "*" if r == 0 or r == height(ex) - 1 else "O"
                dl, dr = diag(ex, r)
                row = ["-"] * width(ex)
                row[dl] = "*"
                row[dr] = "*"
                for s in range(dl + 2, dr - 1, 2):
                    row[s] = symbol
                out += "".join(row)
                out += "\n"

            out += "\n"

        with open(out_file, 'w') as f:
            f.write(out)


if __name__ == '__main__':
    main()
