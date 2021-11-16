from expressions import *
from instructions import *

'''All classes in expressions and instructions should implement type checking, but I'm out of time...'''

if __name__ == '__main__':
    code = While(Zmienna('x'), If(Roznica(Zmienna('x'), Stala(10)), Assign(Zmienna('x'), Roznica(Zmienna('x'), Stala(
        10))), Chain([Assign(Zmienna('y'), Stala(1)), Assign(Zmienna('x'), Suma(Zmienna('x'), Zmienna('y')))])))
    print(code)

    context = code.wykonaj({'x': 2})
    print(context)
