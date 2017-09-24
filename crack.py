from crypt import crypt
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage : crack.py [hash]")
        exit(1)
    else:
        crack(sys.argv[1], sys.argv[1][:2])
    

def crack(chash, csalt):
    for l in range(1, 5):
        cpass = []
        last = []
        for x in range(l): cpass.append("a")
        for x in range(l): last.append("Z")
        #print(cpass)
        while cpass != last:
            if test(cpass, csalt, chash):
                print("Password is " + ''.join(cpass))
                exit(0)
            else:
                for n in range(l):
                    if cpass[n] == 'z':
                        cpass[n] = 'A'
                        break
                    elif cpass[n] == 'Z':
                        cpass[n] = 'a'
                    else:
                        cpass[n] = chr(ord(cpass[n]) + 1)
                        break
                test(''.join(cpass), csalt, chash)
    print("Password doesn't exist")

def test(cp, cs, ch):
    return ch == crypt(''.join(cp), cs)

if __name__ == "__main__":
    main()