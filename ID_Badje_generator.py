# Practice formatting strings.

print("Please enter the following information:")
print()
first_name = input('First name: ')
Last_name = input('Last name: ')
Email = input('Email address: ')
phone = input('Phone number: ')
job = input('Job title: ')
id = input('ID Number: ')

print('The ID Card is:')
print('------------------------------------------')
print(f'{Last_name.upper()}, {first_name}')
print(f'{job}')
print()
print(f'{Email.lower()}')
print(f'{phone}')
print('------------------------------------------')