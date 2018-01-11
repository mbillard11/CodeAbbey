cases = int(raw_input())

for i in range(0, cases):
    linex = map(int, raw_input().split())
    line = sorted(linex)
    num1, num2 = line
    a = num1
    b = num2
    
    rem = num2 % num1
    if rem == 0:
        gcd = num1
   
    x = True
    while rem != 0:
        if x == True:
            gcd =  rem      
            rem = num1 % rem
            num2 = gcd 
            x = False
        else:
            gcd = rem           
            rem = num2 % rem    
            num1 = gcd  
            x = True
    
    lcm = (a*b)/gcd
    
    print '('  
    print gcd, lcm
    print ')',


2496 4524








Input: a, b positive integers
Output: g and d such that g is odd and gcd(a, b) = g×2d
    d := 0
    while a and b are both even do
        a := a/2
        b := b/2
        d := d + 1
    while a ≠ b do
        if a is even then a := a/2
        else if b is even then b := b/2
        else if a > b then a := (a – b)/2
        else b := (b – a)/2
    g := a
    output g, d