def check_pyth_trip(a, b, c):
    if(a**2 + b**2 == c**2):
        return True
    else:
        return False

def main():
    for c in range(1, 1001):
        for b in range(1, c):
            for a in range(1, b):
                if check_pyth_trip(a,b,c):
                    if a+b+c == 1000:
                        print a*b*c
                        return True

    return False
    
if __name__ == '__main__':
    main()
