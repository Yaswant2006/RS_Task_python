#Write a function to check if a string is a palindrome without using slicing or Python built-ins that reverse strings.
str=input("Enter a String:")
palin=True
for i in range(len(str)//2):
    if str[i]!=str[len(str)-i-1]:
        palin=False
        break
print("Palindrome" if palin==True else "Not Palindrome")