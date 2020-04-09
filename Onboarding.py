import random
import string

#user data
def get_details():
    first_name = input("Enter your First Name:  ")
    last_name = input("Enter your Last Name: ")
    email_address = input("Enter your Email address: ")

    user_details = [first_name,last_name,email_address]
    return user_details

#generating password 
def gen_password(user_details):
    letters = string.ascii_lowercase
    password_length = 5
    random_password=''.join(random.choice(letters)for i in range(password_length))
    user_password = str(user_details[0][0:2] + user_details[1][-2:] + random_password)
    return user_password

#adding employee details
status = True
employees = []
user = 1
while status:
       
    user_details = get_details()
    user_password = gen_password(user_details)
    print("Your password is: " + str(user_password))
    password_preference = input("Do you like your generated passsword? If yes, enter 'Yes'. If no enter 'No' and supply your preferred password: ")
       
    password_loop = True
    
    while password_loop:
        if password_preference == 'Yes':
            user_details.append(user_password)
            employees.append(user_details)

            password_loop = False
        else:
           user_password = input(str("Enter password longer than or equals to 7: "))
           password_length = True
           while password_length:
               if len(user_password) >= 7 :
                   user_details.append(user_password)
                   employees.append(user_details)
                   password_length = False
                   password_loop = False
               else:
                        print("Your password is less than 7.")

                        user_password = input("\nEnter password that is longer than or equals to 7: ")

                        new_user = input("Would you like to enter a new user? ") 
                
                        if(new_user== "No"):
                            status=False
for item in employees:
    print(item)
                        
                            

     







