
user_input = str(input("Please enter a phrase: \n")) #prompt user
text = user_input.split()#apply split to the input
a = " "
for i in text: #iterate over text
    a = a + str(i[0]).upper() #concatenate string onto upper portion
print(a)