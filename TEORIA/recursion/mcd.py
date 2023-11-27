def mcd(a,b):
    # O( log(min(a, b)) )
    if a % b == 0:
        return b
    else : return mcd(b, a % b)

print(mcd(12,6))