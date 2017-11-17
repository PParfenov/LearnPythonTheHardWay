from sys import argv

script, filename = argv

txt = open(filename)
txt2 = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())
txt.close()
print(txt2.read())



print("Type the filename again:")
file_again = input("> ")

# turns a string into a file object
txt_again = open(file_again)

# now that it's an object, read its contents
print(txt_again.read())

txt_again.close()
