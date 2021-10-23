def sudan_nomem(n: int, x: int, y: int) -> int:
    '''Count sudan recursive function without results mapping'''
    if n <= 0:
        return x + y
    elif y == 0:
        return x
    else:
        return sudan_nomem(n-1, sudan_nomem(n, x, y-1), sudan_nomem(n, x, y-1) + y)

memory = dict()
def sudan_mem(n: int, x: int, y: int) -> int:
    '''Count sudan recursive function with results mapping'''
    if (n,x,y) not in memory:
        if n == 0:
            memory[(n,x,y)] = x + y
        elif y == 0:
            memory[(n,x,y)] = x
        else:
            memory[(n,x,y)] = sudan_mem(n-1, sudan_mem(n, x, y-1), sudan_mem(n, x, y-1) + y)
    
    return memory[(n,x,y)]