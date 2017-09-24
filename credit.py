def main():
    cardn = input("Number: ")
    if cardn[:2] == "34" or cardn[:2] == "37":
        cardt = "AMEX"
    elif cardn[:2] in ("5" + str(x) for x in range(1, 6)):
        cardt = "MASTERCARD"
    elif cardn[1] == "4":
        cardt = "VISA"
    else:
        cardt == "INVALID"
        
    altsum = 0
    for x in range(1, len(cardn), 2):
        for n in str(int(cardn[x])*2):
            altsum += n
    for x in range(0, len(cardn), 2):
        altsum += int(cardn[x])
    
    if(altsum % 10 != 0):
        cardt = "INVALID"
        
    print(cardt)
    exit(0)

if __name__ == "__main__":
    main()