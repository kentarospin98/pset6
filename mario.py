def main():
    while(True):
        h = int(input("Height: "))
        if(h > 0):
            break

    for i in range(h):
        for j in range(h - i - 1):
            print(" ", end="")
        for j in range(i + 1):
            print("#", end="")
        print("  ", end="")
        for j in range(i + 1):
            print("#", end="")
        for j in range(h - i - 1):
            print(" ", end="")
        print("")

if __name__ == "__main__":
    main()