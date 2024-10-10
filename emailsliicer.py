#email slicer

email = input('Enter the Email Address')

index = email.index('@')

if not index:
    print('error invalid email')

username = email[:index]
domain = email[index+1:]

print(f'Your Username is {username} and your domain is {domain}')