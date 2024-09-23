a=633
b=73
c=9


def greatest(x,y,z):
    if(z>y and z>x):
        return z
    elif(x>y and x>z):
        return x
    else:
        return y

ans=greatest(a,b,c)
print(ans)

