def fib(x):
    """assumes x an int >= 0
       returns Fibonacci of x"""
    assert type(x) == int and x >= 0
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
        
def main():
    choice = None
    while choice != 0:
        print \
        ("""
        Fibonacci
        
        0 - Quit
        1 - Calculate
        """)
        
        choice = raw_input("Choice: ")
        print ""
        
        # exit
        if (choice == "0"):
            print "Good-bye."
            break
            
        # enter the integer
        if (choice == "1"):
          integer = input("Enter an integer: ")
          print "fib(", str(integer), ") = ", fib(integer)
          
if __name__ == "__main__":
    main()