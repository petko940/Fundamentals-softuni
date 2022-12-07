def palindrome(number):
    if number == number[::-1]:
        print("True")
    else:
        print("False")


numbers = list(map(str, input().split(", ")))

for i in numbers:
    palindrome(i)
