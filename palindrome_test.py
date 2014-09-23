def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))
    
def main():
    print 'isPalindrome("Able	was	I	ere	I	saw	Elba")', isPalindrome("Able	was	I	ere	I	saw	Elba")
    print 'isPalindrome("Are we not drawn onward, we few, drawn onward to new era?")', isPalindrome("Are we not drawn onward, we few, drawn onward to new era?")
    print 'isPalindrome("not a palindrome")', isPalindrome("not a palindrome")

if __name__ == "__main__":
    main()
  