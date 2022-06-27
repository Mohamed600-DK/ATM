import modules.Global_variable as gv
from modules.private_functions import *
import json


####################################################################################################################################################################
####################################################################################################################################################################
def load_clints_data():  
    #global data,clints_data,locked_accounts
    with open("./Data/clints_data.json","r") as file_data:
        data_read=file_data.read()
    gv.data=json.loads(data_read)
    gv.clints_data=gv.data["clints_data"]
    gv.locked_accounts=gv.data["locked_accounts"]
####################################################################################################################################################################

def save_clints_data():
   # global clints_data,data,locked_accounts
 
    with open("./Data/clints_data.json","w") as file_data:
        gv.data["clints_data"]=gv.clints_data
        gv.data["locked_accounts"]=gv.locked_accounts
        gv.clints_data=json.dumps(gv.data,indent=2)
        file_data.write(gv.clints_data)
####################################################################################################################################################################
def find_clint(acc_num):
      
    
    for clint_count in gv.locked_accounts:
        if acc_num == clint_count["ID"]:
            #repalce in with top_level window
            text_msg=("your account is blocked"+"\n"+"please go to the branch"+
            "\n"+"or tray another Account number").capitalize()  
            gv.main_window.label_text("login_masg_label",text_msg)
            gv.main_window.enable_window("login_masg",True)
            gv.main_window.button_call_fun("login_masg_button",gv.main_window.exit_app)
            gv.main_window.button_text("login_masg_button","close Program")

            return "Bocked"    

    for clint_count in gv.clints_data:
        if acc_num == clint_count["ID"]:
            return clint_count
    masg=("your account number" +"\n"+"isn't exist,please\n check your account number").capitalize()
    gv.main_window.label_text("login_masg_label",masg)
    gv.main_window.enable_window("login_masg",True)
    return "Not_fond"
##################################################################################################################################################################
def check_password():
   
    
    password=gv.main_window.get_text("accountNumber_textbox")
    if (password !=""):
        if (password==gv.clint["password"]):
            switing_frame("log_in_frame","home_frame")

        elif(gv.check_pass==3):
            gv.locked_accounts.append(gv.clint)
            gv.clints_data.remove(gv.clint)
            text_msg=("you enter password 3 times."+"\n"+ "your account is blocked "+"\n"
                    +"please go to the branch" ).capitalize()  

            gv.main_window.label_text("login_masg_label",text_msg)
            gv.main_window.enable_window("login_masg",True)
            gv.main_window.button_call_fun("login_button",gv.main_window.exit_app)
            gv.main_window.button_text("login_button","close Program")

        else:           
            text_msg=("you have only %s trials"%str(3-gv.check_pass)+"\n"+
                      "enter your account's password"+"\n"+" agine").capitalize()  

            gv.main_window.label_text("login_masg_label",text_msg)
            gv.main_window.enable_window("login_masg",True)
            gv.check_pass +=1
####################################################################################################################################################################
def log_in():
    
   
    account_number=""
    account_number=gv.main_window.get_text("accountNumber_textbox")
    if (account_number !=""):
        gv.clint=find_clint(account_number)
        if (gv.clint=="Bocked"):
            pass
            
        elif (gv.clint=="Not_fond"):
           pass
            
        elif(type(gv.clint)==type(dict())):
 
            gv.main_window.label_text("login_label","Enter your account's password:")
            gv.main_window.button_call_fun("login_button",check_password)
    
####################################################################################################################################################################
def withdraw():

    max_multiply_valu=100
    max_withdraw_valu=5000
    account_balanc=gv.clint["Balance"]
    amout_withdraw=int(gv.main_window.get_text("cash_withdraw_textbox"))
    ####################################################################################################################################################################
    def __login_masg_button_event_true_condition_3():
        switing_frame("cash_withdraw_frame","home_frame")
        gv.main_window.disable_window("login_masg")
        gv.main_window.button_call_fun("login_masg_button",[gv.main_window.disable_window,"login_masg"])
    ####################################################################################################################################################################
    def __login_masg_button_event_false_condition_1():
        switing_frame("cash_withdraw_frame","home_frame")
        gv.main_window.disable_window("login_masg")
        gv.main_window.button_call_fun("login_masg_button",[gv.main_window.disable_window,"login_masg"])
    ####################################################################################################################################################################

    if(amout_withdraw<=account_balanc):#condition #1

        if ((amout_withdraw%max_multiply_valu)==0):#condition #2

            if(amout_withdraw<=max_withdraw_valu):#condition #3
                ATM_Actuator_Out()
                text_msg=("Thank you,\nyou will get your Money now\n please be patient").capitalize()  
                gv.main_window.label_text("login_masg_label",text_msg)
                gv.main_window.enable_window("login_masg",True)
                gv.main_window.button_call_fun("login_masg_button",__login_masg_button_event_true_condition_3)
                gv.main_window.button_text("login_masg_button","Ok")
                gv.clint["Balance"]=account_balanc-amout_withdraw
                
            else:#condition #3
                text_msg=("it isn't allawed to withdraw more than %s"%max_withdraw_valu+"\n"
                +"please enter the"+"\n"+" amount to withdraw again").capitalize()  
                gv.main_window.label_text("login_masg_label",text_msg)
                gv.main_window.enable_window("login_masg",True)
                gv.main_window.button_text("login_masg_button","ok")
        else:#condition #2
            text_msg=("it is allawed only to"+"\n"+"withdraw %s or it's muliple"%max_multiply_valu+"\n"
            +"please enter "+"\n"+" the amount to withdraw again").capitalize()  
            gv.main_window.label_text("login_masg_label",text_msg)
            gv.main_window.enable_window("login_masg",True)
            gv.main_window.button_text("login_masg_button","Ok")
    else:#condition #1   

        text_msg=("there is no sufficient balance"+"\n"
                +"please check "+"\n"+"your account balance").capitalize()  
        gv.main_window.label_text("login_masg_label",text_msg)
        gv.main_window.enable_window("login_masg",True)

        gv.main_window.button_call_fun("login_masg_button",__login_masg_button_event_false_condition_1)
        gv.main_window.button_text("login_masg_button","return to home window")
####################################################################################################################################################################
def ATM_Actuator_Out():
    print("ATM_Actuator_Out function is run")
####################################################################################################################################################################
def fawry_service():

    clint_phone=gv.main_window.get_text("fawry_recharge_phone_textbox")
    recharge_amount=int(gv.main_window.get_text("fawry_recharge_amount_textbox"))
    clint_balance=gv.clint["Balance"]
    def __login_masg_button_event_false_condition():
        #switing_frame("fawry_recharge_frame","fawry_service_frame")
        switing_frame("fawry_recharge_frame","home_frame")
        gv.main_window.disable_window("login_masg")
        gv.main_window.button_call_fun("login_masg_button",[gv.main_window.disable_window,"login_masg"])
   
    def __login_masg_button_event_true_condition():
        #switing_frame("fawry_recharge_frame","fawry_service_frame")
        switing_frame("fawry_recharge_frame","home_frame")
        gv.main_window.disable_window("login_masg")
        gv.main_window.button_call_fun("login_masg_button",[gv.main_window.disable_window,"login_masg"])
    
    if(len(clint_phone)==11):
        if(recharge_amount <=clint_balance):
            gv.clint["Balance"]=clint_balance-recharge_amount
            
            text_msg=("succesful operation"+"\n"
                    +"you will Back "+"\n"+" to your home Page").capitalize()  
            gv.main_window.label_text("login_masg_label",text_msg)
            gv.main_window.enable_window("login_masg",True)
            gv.main_window.button_call_fun("login_masg_button",__login_masg_button_event_true_condition)
            gv.main_window.button_text("login_masg_button","Ok")  
            
            fawry_service_call(clint_phone)
        else:
            text_msg=("there is no sufficient balance"+"\n"
                    +"please check "+"\n"+"your account balance").capitalize()  
            gv.main_window.label_text("login_masg_label",text_msg)
            gv.main_window.enable_window("login_masg",True)
            gv.main_window.button_call_fun("login_masg_button",__login_masg_button_event_false_condition)
            gv.main_window.button_text("login_masg_button","return to home window")     
    else:
            text_msg=("you enter wrong phone number"+"\n"
            +"please check "+"\n"+"your phone number").capitalize()  
            gv.main_window.label_text("login_masg_label",text_msg)
            gv.main_window.enable_window("login_masg",True)
            gv.main_window.button_text("login_masg_button","Ok") 
       
def fawry_service_call(clint_phone_number=None):
   
    print("the operation is done")      
    print(clint_phone_number)
    print("Network is ",gv.reghatfe_network) 
    
    