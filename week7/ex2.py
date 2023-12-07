def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
x  = str(input("Enter Input : "))
if(is_palindrome(x) == True):
    print(f"'{x}'","is palindrome")
else:
    print(f"'{x}'","is not palindrome")