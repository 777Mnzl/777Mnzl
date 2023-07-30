email = input('Enter your E-mail: ')  # g@g.in <- minimum condition
k = 0
j = 0
d = 0
if len(email) >= 6:  # 1
    if email[0].isalpha():  # 2
        if ('@' in email) and (email.count('@') == 1):  # 3
            if (email[-4] == '.') ^ (email[-3] == '.'):  # 4
                for i in email:
                    if i == i.isspace():  # 5
                        k = 1
                    elif i.isalpha():  # 5
                        if i == i.upper():
                            j = 1
                    elif i.isdigit():  # 5
                        continue
                    elif i == '_' or i == '.' or i == '@':
                        continue
                    else:
                        d = 1

                if k == 1 or j == 1 or d == 1:
                    print('Invalid Email:  Space condition 5')
                else:
                    print('Correct Email!')
            else:
                print('Invalid email: wrong position of character 4')
        else:
            print('Invalid email: Wrong attributes placed 3')
    else:
        print('Invalid Email: No alphabet positioned at first 2')
else:
    print('Invalid Email 1')
