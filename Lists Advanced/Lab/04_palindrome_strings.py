words = input().split()
palindrome = input()

palindrome_list = [x for x in words if x == x[::-1]]

print(palindrome_list)
print(f"Found palindrome {palindrome_list.count(palindrome)} times")
