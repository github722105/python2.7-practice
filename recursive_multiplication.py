def recurMul(a, b):
    """recurMul(a, b): b is an integer and greater than or equal to 1"""
    if b == 1:
        return a
    else:
        return a + recurMul(a, b-1)
      
def main():
    print "recurMul(4, 5) : ", recurMul(4, 5)
    print "recurMul(-7, 4) : ", recurMul(-7, 4)
    print "recurMul(30, 10) : ", recurMul(30, 10)
    
if __name__ == "__main__":
    main()