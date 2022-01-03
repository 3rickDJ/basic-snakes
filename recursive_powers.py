def main(num, rept):
    if num <= rept:
        print(str(2 ** num))
        main(num+1, rept)
    else:
        print("Fin!")

if __name__=='__main__':
    main(0,10)