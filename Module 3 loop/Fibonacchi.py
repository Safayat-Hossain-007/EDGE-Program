def fibonacchi(n):
    a = 0;
    b = 1;
    while(a < n):
     a,b = b,a +b;
     print(a)

fibonacchi(10);