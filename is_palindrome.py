def is_palindrome(item):
    item = str(item)
    return item == item[::-1]

# 1) Write an `is_palindrome` function to check if a string is a palindrome (reads the same from left-to-right and right-to-left)
assert is_palindrome("radar") == True, f"Expected True but got {is_palindrome('radar')}"
assert is_palindrome("stop") == False, f"Expected False but got {is_palindrome('stop')}"

# 2) Make `is_palindrome` work with numbers
assert is_palindrome(101) == True, f"Expected True but got {is_palindrome(101)}"
assert is_palindrome(10) == False, f"Expected False but got {is_palindrome(10)}"

