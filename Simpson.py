
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
    input('Holas')
    stopValue='23.596'
    decimalResult=''
    n=0
    while decimalResult!=stopValue:
        n+=1
        decimalResult=simpson(n,5,0)[:6]
        print(n,"   ", decimalResult)
    print("Final")


if __name__=='__main__':
    main()