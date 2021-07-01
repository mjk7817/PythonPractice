email = input("Please enter an email address: ").strip()
username = email[:email.index("@")]
domainName = email[email.index("@")+1:]
format_ = f"Your username is '{username}' and your domain name is '{domainName}'"
print(format_)