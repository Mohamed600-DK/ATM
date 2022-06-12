import json

global clints_data
global locked_accounts
global clint


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
    global data    
    with open("Data/clints_data.json","r") as file_data:
        data_read=file_data.read()
    data=json.loads(data_read)
    clints_data=data["clints_data"]
    locked_accounts=data["locked_accounts"]



def save_clints_data():
    global data    
    with open("Data/clints_data.json","w") as file_data:
        data["clints_data"]=clints_data
    data["locked_accounts"]=locked_accounts
    clints_data=json.dumps(data,indent=2)
    file_data.write(clints_data)

