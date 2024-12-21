string="Hello"
# string[start:end:-1] -1 is for reverse
print(string[::-1])

#by using loop

#In python Empty String is use to reverse a String
text="madam"
reverse_string=""

for char in text :
    reverse_string=char+reverse_string
print("Reverse String for madam is ",reverse_string)

if(text==reverse_string):
    print("Its Palidrome")
else:
    print("Its Not Palindrome")

    # reverse_string= ""
    # reverse_string= S +""---> S
    # reverse_string= o + S ---> oS
    # reverse_string= u+ oS ---> uoS
    # reverse_string= p + uoS ---> puoS
