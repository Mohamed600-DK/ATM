#import GUI 

import json


clints_data=list()
locked_accounts=list()
clint=dict()
data=dict()
#function to find the clint from my data_file
def find_clint(acc_num):
    dict_value=dict()
    flag=0

    for clint_count in locked_accounts:
        if acc_num == clint_count["ID"]:
            print(
        '''
        your account is blocked 
        please go to the branch
        '''
            )
            return "Bocked" 
  #loop to make sure a right account number is entered      
    while(True):
            for clint_count in clints_data:
                if acc_num == clint_count["ID"]:
                    return clint_count
            print("Id is  not exist")
            acc_num=input("Pleas Enter Your account number again:")


def load_clints_data():  
    global clints_data,data,locked_accounts
    with open("Data/clints_data.json","r") as file_data:
        data_read=file_data.read()
    data=json.loads(data_read)
    clints_data=data["clints_data"]
    locked_accounts=data["locked_accounts"]



def save_clints_data():
    global clints_data,data,locked_accounts
    with open("Data/clints_data.json","w") as file_data:
        data["clints_data"]=clints_data
    data["locked_accounts"]=locked_accounts
    clints_data=json.dumps(data,indent=2)
    file_data.write(clints_data)


load_clints_data()
print(clints_data)
#while(True):#main loop for the program
account_number=""
account_number=input("Pleas Enter Your account number:")
clint=find_clint(account_number)
if (clint=="Bocked"):
    pass
else:
    password=input("Enter your account's password:")
    for check_pass in range(0,4):
        if (password==clint["password"]):
            #call option window
            pass
        elif(check_pass==3):
            locked_accounts.append(clint)
            clints_data.remove(clint)
            print(
            '''
            your account is blocked 
            please go to the branch
            '''
                )    
        else:
            password=input("you have only  "+str(3-check_pass)+" trials"
            +"\n"+"Enter your account's password agine:")
    
    #exite form program

save_clints_data()

#break 




        







