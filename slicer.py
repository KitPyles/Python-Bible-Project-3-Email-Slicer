# Ask for user email

email = input("What's your email address? ")

# Slice out username

username = email[:email.index("@")]

# Slice out domain

domain = email[email.index("@") + 1:]

# Format message

output = "Your username is {} and your domain name is {}.".format(username,domain)

# Display output message

print(output)