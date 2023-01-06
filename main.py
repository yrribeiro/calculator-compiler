from lexical import lexical_analyzer

def main():
    f = open("./example.txt", "r")
    lexical_analyzer(f)
    

if __name__ == '__main__':
    main()