def create_multiplication_table():
    table_size = 12

    border = "*" * 100
    print(border.center(64, '*'))

    header_space = " " * ((64 - len("Jadual Darab") - 6) // 2)

    middle_text = header_space + " " * 22 + "Jadual Darab" + header_space
    print(middle_text.center(64, ' '))

    print(border.center(64, '*'))

    for i in range(1, table_size + 1):
        print(f"{i:^7} |", end="")
        for j in range(1, table_size + 1):
            result = i * j
            print(f" {result:^7} |", end="")  # Add spaces around the result
        print()


def main():
    create_multiplication_table()


if __name__ == "__main__":
    main()
