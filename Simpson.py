
def function(value):
    return (value**3+1)**(0.5)


def simpson(intervals,suplim, inflim):
    width=(suplim-inflim)/intervals
    
    termns=function(inflim)+function(suplim)
    for i in range(1,intervals):
        if i%2==0:
            termns+=2*function(inflim+width*i)
        else:
            termns+=4*function(inflim+width*i)
    return str(termns*width/3)


def main():
    stopValue=input('Digit the stop value: ')
    sup=float(input('Set the limit superior: '))
    inf=float(input('Set the limit inferior: '))
    # stopValue='23.596'
    decimalResult=''
    intervals=0
    while decimalResult!=stopValue:
        intervals+=1
        decimalResult=simpson(intervals,sup,inf)[:len(stopValue)]
        print(intervals,"   ", decimalResult)
    print("Requiered number of intervals is: n = ", intervals)


if __name__=='__main__':
    main()