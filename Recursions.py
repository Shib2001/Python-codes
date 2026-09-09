# Defination : when a function calls itself repeatedly , you could say it is some extend a alternate of loops 




def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)