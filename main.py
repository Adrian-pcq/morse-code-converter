from morse import international_morse

BAD_CHARS = {"!", "@", "#", '$', "%", "^", "&", "*", "(", ")", "-", "_", ".", ":", ";", "/", "'", '"', "+", "`", "~", "?"}

user_input = 'I am the OVERLORD!!!'
user_input = user_input.lower()
for i in BAD_CHARS:
    user_input = user_input.replace(i, "")

list_input = user_input.split()
print (list_input)