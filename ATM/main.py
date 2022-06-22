
import sys

from numpy import size

####################################################################################################################################################################
from  GUI import * 
import json
####################################################################################################################################################################
clints_data=list()
locked_accounts=list()
clint=dict()
data=dict()
check_pass=0
####################################################################################################################################################################
class masg(GUI_app):
    font_text=GUI_app().font_init(size=10)
    root_window=""

    masg_option=dict(
        name="masg",
        parent=root_window,
        masg="masg",
        title="Massage",
        bg="red",
        fg=None,
        bd=None,
        height=150,
        width=260, 
        font=None,
        x_location=None,
        y_location=None
    )

    def __init__(self,
                name,
                parent=None,
                masg=None,
                title=None,
                bg=None,
                fg=None,
                bd=None,
                height=None,
                width=None, 
                font=None,
                x_location=None,
                y_location=None):

        self.root_window=self.masg_window()
        self.masg_label()
        self.masg_button()
        GUI_app().top_level_options["parent"]=parent
        GUI_app().top_level_options["name"]=masg
        GUI_app().top_level_options["title"]=title
        GUI_app().top_level_options["bg"]=bg
        GUI_app().top_level_options["fg"]=fg
        GUI_app().top_level_options["bd"]=bd
        GUI_app().top_level_options["height"]=height
        GUI_app().top_level_options["width"]=width
        GUI_app().top_level_options["font"]=font
        GUI_app().top_level_options["x_location"]=x_location
        GUI_app().top_level_options["y_location"]=y_location



    def masg_window(self):


        root_window=GUI_app().creat_toplevelwindow("masg",title="Massage",width=260, height=150,x_location=300,y_location=300,bg="red")
        GUI_app().disable_window("masg")
        
    
    def masg_label(self):
        global font_text
        GUI_app().label_options["parent"]=self.root_window
        GUI_app().label_options["x_location"]=12
        GUI_app().label_options["y_location"]=5
        GUI_app().label_options["width"]=26
        GUI_app().label_options["height"]=5
        GUI_app().label_options["justify"]=CENTER
        obj_label=GUI_app().creat_label("login_masg_label",font_text=self.font_text,bg="blue")
        obj_label.pack(side="TOP") 
    def masg_button(self):
        
        GUI_app().Button_options["parent"]=self.root_window
        GUI_app().Button_options["text"]="ok"
        GUI_app().Button_options["call_function"]=[GUI_app().disable_window,"login_masg"]
        GUI_app().Button_options["width"]="auto"
        GUI_app().Button_options["height"]=1
        GUI_app().Button_options["x_location"]=100
        GUI_app().Button_options["y_location"]=110
        obj_button=GUI_app().creat_button(button_name="login_masg_button",font=self.font_text)
        obj_button.pack(side="BOTTOM")    



####################################################################################################################################################################
def load_clints_data():  
    global clints_data,data,locked_accounts
    with open("Data/clints_data.json","r") as file_data:
        data_read=file_data.read()
    data=json.loads(data_read)
    clints_data=data["clints_data"]
    locked_accounts=data["locked_accounts"]
####################################################################################################################################################################
def save_clints_data():
    global clints_data,data,locked_accounts
 
    with open("Data/clints_data.json","w") as file_data:
        data["clints_data"]=clints_data
        data["locked_accounts"]=locked_accounts
        clints_data=json.dumps(data,indent=2)
        file_data.write(clints_data)
####################################################################################################################################################################
def find_clint(acc_num):
    
    for clint_count in locked_accounts:
        if acc_num == clint_count["ID"]:
            #repalce in with top_level window
            text_msg=("your account is blocked"+"\n"+"please go to the branch"+
            "\n"+"or tray another Account number").capitalize()  
            main_window.label_text("login_masg_label",text_msg)
            main_window.enable_window("login_masg",True)
            main_window.button_call_fun("login_masg_button",[main_window.exit_app])
            main_window.button_text("login_masg_button","close Program")

            return "Bocked"    

    for clint_count in clints_data:
        if acc_num == clint_count["ID"]:
            return clint_count
    masg=("your account number" +"\n"+"isn't exist,please\n check your account number").capitalize()
    main_window.label_text("login_masg_label",masg)
    main_window.enable_window("login_masg",True)
    return "Not_fond"
##################################################################################################################################################################
def check_password():
    global clint,check_pass
    
    password=main_window.get_text("accountNumber_textbox")
    if (password !=""):
        if (password==clint["password"]):
            switing_frame("log_in_frame","home_frame")

        elif(check_pass==3):
            locked_accounts.append(clint)
            clints_data.remove(clint)
            text_msg=("you enter password 3 times."+"\n"+ "your account is blocked "+"\n"
                    +"please go to the branch" ).capitalize()  

            main_window.label_text("login_masg_label",text_msg)
            main_window.enable_window("login_masg",True)
            main_window.button_call_fun("login_button",[main_window.exit_app])
            main_window.button_text("login_button","close Program")

        else:           
            text_msg=(
                '''
    you have only %s trials
enter your account's password agine
                '''
    %str(3-check_pass)).capitalize()  

            main_window.label_text("login_masg_label",text_msg)
            main_window.enable_window("login_masg",True)
            main_window.enable_widget("login_masg_label")
            check_pass +=1
####################################################################################################################################################################
def log_in():
    global clint
    account_number=""
    account_number=main_window.get_text("accountNumber_textbox")
    if (account_number !=""):
        clint=find_clint(account_number)

        if (clint=="Bocked"):
            pass
            
        elif (clint=="Not_fond"):
           pass
            
        elif(type(clint)==type(dict())):
                 
            main_window.label_text("login_label","Enter your account's password:")
            main_window.button_call_fun("login_button",[check_password])
####################################################################################################################################################################
def switing_frame(disable_frame,enable_frame):
    main_window.disable_widget(disable_frame)
    main_window.enable_widget(enable_frame)        
####################################################################################################################################################################
def ATM_Actuator_Out():
    print("ATM_Actuator_Out function is run")



def base_window():
    main_window.creat_window(window_name="base_window") 

def login_masg_window():

        
        main_window.creat_toplevelwindow("login_masg",title="Massage",width=260,height=150,x_location=300,y_location=300,bg="red")
        main_window.options["login_masg"]["parent"]= main_window.window_list["base_window"]
        main_window.disable_window("login_masg") 





####################################################################################################################################################################
   

def withdraw():

    max_multiply_valu=100
    max_withdraw_valu=5000
    account_balanc=clint["Balance"]
    amout_withdraw=int(main_window.get_text("cash_withdraw_textbox"))
    print(amout_withdraw)
    print(account_balanc)
    if(amout_withdraw<=account_balanc):#condition #1
        print("pass1")
        if ((amout_withdraw%max_multiply_valu)==0):#condition #2
            print("pass2")
            if(amout_withdraw<=max_withdraw_valu):#condition #3
                print("pass3")
                ATM_Actuator_Out()
            else:#condition #3
                text_msg=("it isn't allawed to withdraw more than %s"%max_withdraw_valu+"\n"
                +"please enter the amount to withdraw again").capitalize()  
                main_window.label_text("login_masg_label",text_msg)
                main_window.enable_window("login_masg",True)
                main_window.button_text("login_masg_button","ok")
        else:#condition #2
            text_msg=("it is allawed only to withdraw %s or it's muliple"%max_multiply_valu+"\n"
            +"please enter the amount to withdraw again").capitalize()  
            main_window.label_text("login_masg_label",text_msg)
            main_window.enable_window("login_masg",True)
            #main_window.button_call_fun("login_masg_button",[withdraw])
            main_window.button_text("login_masg_button","Ok")
    else:#condition #1   

        text_msg=("there is no sufficient balance"+"\n"
                +"please check your account balance").capitalize()  
        main_window.label_text("login_masg_label",text_msg)
        main_window.enable_window("login_masg",True)
        def event():
            switing_frame("cash_withdraw_frame","home_frame")
            main_window.disable_window("login_masg")
            main_window.button_call_fun("login_masg_button",[main_window.disable_window,"login_masg"])
        
        main_window.button_call_fun("login_masg_button",[event])
        main_window.button_text("login_masg_button","return to home window")
        

   
load_clints_data()
####################################################################################################################################################################

###################################################################################################################################################################

def log_in_frame():
    main_window.frame_options["parent"]= main_window.window_list["base_window"]
    main_window.frame_options["x_location"]=0
    main_window.frame_options["y_location"]=0
    main_window.frame_options["width"]=main_window.options["base_window"]["width"]
    main_window.frame_options["height"]=main_window.options["base_window"]["height"]
    main_window.frame_options["relief"]=RIDGE
    main_window.frame_options["bd"]=20
    main_window.creat_frame("log_in_frame",bg="red")
def home_frame():
    main_window.frame_options["parent"]= main_window.window_list["base_window"]
    main_window.frame_options["x_location"]=0
    main_window.frame_options["y_location"]=0
    main_window.frame_options["width"]=main_window.options["base_window"]["width"]
    main_window.frame_options["height"]=main_window.options["base_window"]["height"]
    main_window.frame_options["relief"]=RIDGE
    main_window.frame_options["bd"]=20
    main_window.creat_frame("home_frame",bg="blue")
    main_window.disable_widget("home_frame")
def Cash_Withdraw_frame():
    main_window.frame_options["parent"]= main_window.window_list["base_window"]
    main_window.frame_options["x_location"]=0
    main_window.frame_options["y_location"]=0
    main_window.frame_options["width"]=main_window.options["base_window"]["width"]
    main_window.frame_options["height"]=main_window.options["base_window"]["height"]
    main_window.frame_options["relief"]=RIDGE
    main_window.frame_options["bd"]=20
    main_window.creat_frame("cash_withdraw_frame",bg="orange")
def Balance_Inquiry_frame():
    main_window.frame_options["parent"]= main_window.window_list["base_window"]
    main_window.frame_options["x_location"]=0
    main_window.frame_options["y_location"]=0
    main_window.frame_options["width"]=main_window.options["base_window"]["width"]
    main_window.frame_options["height"]=main_window.options["base_window"]["height"]
    main_window.frame_options["relief"]=RIDGE
    main_window.frame_options["bd"]=20
    main_window.creat_frame("balance_inquiry_frame",bg="orange")
def Password_Change_frame():
    main_window.frame_options["parent"]= main_window.window_list["base_window"]
    main_window.frame_options["x_location"]=0
    main_window.frame_options["y_location"]=0
    main_window.frame_options["width"]=main_window.options["base_window"]["width"]
    main_window.frame_options["height"]=main_window.options["base_window"]["height"]
    main_window.frame_options["relief"]=RIDGE
    main_window.frame_options["bd"]=20
    main_window.creat_frame("Password_Change_frame",bg="orange")
def Fawry_Service_frame():
    main_window.frame_options["parent"]= main_window.window_list["base_window"]
    main_window.frame_options["x_location"]=0
    main_window.frame_options["y_location"]=0
    main_window.frame_options["width"]=main_window.options["base_window"]["width"]
    main_window.frame_options["height"]=main_window.options["base_window"]["height"]
    main_window.frame_options["relief"]=RIDGE
    main_window.frame_options["bd"]=20
    main_window.creat_frame("fawry_service_frame",bg="orange")
    
    



#############################################################################################################################
def login_masg_label():
    global font_text
    main_window.label_options["parent"]= main_window.window_list["login_masg"]
    main_window.label_options["x_location"]=12
    main_window.label_options["y_location"]=5
    main_window.label_options["width"]=26
    main_window.label_options["height"]=5
    main_window.label_options["justify"]=CENTER
    main_window.creat_label("login_masg_label",font_text=font_text,bg="blue")
####################################################################################################################################################################
def login_label():

    main_window.label_options["parent"]= main_window.widged_list["log_in_frame"]
    main_window.label_options["text"]="Enter Your Account Name:"
    main_window.label_options["width"]="auto"
    main_window.label_options["height"]="auto"
    main_window.label_options["x_location"]=230
    main_window.label_options["y_location"]=main_window.options["accountNumber_textbox"]["y_location"]
    main_window.creat_label("login_label")

def login_masg_button():
    global font_text
    main_window.Button_options["parent"]=main_window.window_list["login_masg"]
    main_window.Button_options["text"]="ok"
    main_window.Button_options["call_function"]=[main_window.disable_window,"login_masg"]
    main_window.Button_options["width"]="auto"
    main_window.Button_options["height"]=1
    main_window.Button_options["x_location"]=100
    main_window.Button_options["y_location"]=110
    main_window.creat_button(button_name="login_masg_button",font=font_text)

####################################################################################################################################################################
def login_button():

    screan_x=main_window.options["log_in_frame"]["width"]
    screan_y=main_window.options["log_in_frame"]["height"]
    button_width=10
    button_height=2
    button_width_px=button_width*8
    button_height_px=button_height*8
    button_x_location=(screan_x-button_width_px-60)/2
    button_y_location=(screan_y-button_height_px)*2/4
    
    main_window.Button_options["parent"]=main_window.widged_list["log_in_frame"]
    main_window.Button_options["text"]="ENTER"
    main_window.Button_options["call_function"]=[log_in]
    main_window.Button_options["width"]=button_width
    main_window.Button_options["height"]=button_height
    main_window.Button_options["x_location"]=button_x_location
    main_window.Button_options["y_location"]=button_y_location
    main_window.creat_button("login_button")
###################################################################################################################################################################
def b_Cash_Withdraw():
   
    screan_x=main_window.options["home_frame"]["width"]
    screan_y=main_window.options["home_frame"]["height"]
    
    button_width=15
    button_height=2
    button_x_location=0
    button_y_location=(screan_y/8)

    main_window.Button_options["parent"]=main_window.widged_list["home_frame"]
    main_window.Button_options["text"]="Cash Withdraw"
    main_window.Button_options["call_function"]=[switing_frame,"home_frame","cash_withdraw_frame"]
    main_window.Button_options["width"]=button_width
    main_window.Button_options["height"]=button_height
    main_window.Button_options["x_location"]=button_x_location
    main_window.Button_options["y_location"]=button_y_location
    main_window.creat_button("b_Cash_Withdraw")
    back("cash_withdraw_frame")
####################################################################################################################################################################
def b_Balance_Inquiry():
    
    screan_x=main_window.options["home_frame"]["width"]
    screan_y=main_window.options["home_frame"]["height"]
  
    button_width=15
    button_height=2
    button_height_px=button_height*8
    button_x_location=0
    button_y_location=(screan_y/2)-(button_height_px/2)
    
    main_window.Button_options["parent"]=main_window.widged_list["home_frame"]
    main_window.Button_options["text"]="Balance Inquiry"
    main_window.Button_options["call_function"]=[switing_frame,"home_frame","balance_inquiry_frame"]
    main_window.Button_options["width"]=button_width
    main_window.Button_options["height"]=button_height
    main_window.Button_options["x_location"]=button_x_location
    main_window.Button_options["y_location"]=button_y_location
    
    main_window.creat_button("b_Balance_Inquiry")
    back("balance_inquiry_frame")
####################################################################################################################################################################
def b_Password_Change():
    screan_x=main_window.options["home_frame"]["width"]
    screan_y=main_window.options["home_frame"]["height"]    
    button_width=15
    button_height=2
    button_width_px=button_width*8+200
    button_x_location=screan_x-button_width_px
    button_y_location=(screan_y/8)   
    main_window.Button_options["parent"]=main_window.widged_list["home_frame"]
    main_window.Button_options["text"]="Password Change"
    main_window.Button_options["call_function"]=[switing_frame,"home_frame","Password_Change_frame"]
    main_window.Button_options["width"]=button_width
    main_window.Button_options["height"]=button_height
    main_window.Button_options["x_location"]=button_x_location
    main_window.Button_options["y_location"]=button_y_location
    main_window.creat_button("b_Password_Change")
    back("Password_Change_frame")
####################################################################################################################################################################
def b_Fawry_Service():
    screan_x=main_window.options["home_frame"]["width"]
    screan_y=main_window.options["home_frame"]["height"]
    button_width=15
    button_height=2
    button_width_px=button_width*8+200
    button_height_px=button_height*8
    button_x_location=screan_x-button_width_px
    button_y_location=(screan_y/2)-(button_height_px/2)    
    main_window.Button_options["parent"]=main_window.widged_list["home_frame"]
    main_window.Button_options["text"]="Balance Inquiry"
    main_window.Button_options["call_function"]=[switing_frame,"home_frame","fawry_service_frame"]
    main_window.Button_options["width"]=button_width
    main_window.Button_options["height"]=button_height
    main_window.Button_options["x_location"]=button_x_location
    main_window.Button_options["y_location"]=button_y_location
    main_window.creat_button("b_Fawry_Service")
    back("fawry_service_frame")
####################################################################################################################################################################
def b_Exit():

    screan_x=main_window.options["home_frame"]["width"]
    screan_y=main_window.options["home_frame"]["height"]
  
    button_width=15
    button_height=2
    width_px=button_width*8+120
    height_px=button_height*8+130
    button_x_location=(screan_x-width_px)/2
    button_y_location=(screan_y)-(height_px)


    main_window.Button_options["parent"]=main_window.widged_list["home_frame"]
    main_window.Button_options["text"]="Exit"
    main_window.Button_options["call_function"]=[main_window.exit_app]
    main_window.Button_options["width"]=button_width
    main_window.Button_options["height"]=button_height
    main_window.Button_options["x_location"]=button_x_location
    main_window.Button_options["y_location"]=button_y_location
    main_window.creat_button("b_exit")
####################################################################################################################################################################
def back(curren_frame):
    screan_x=main_window.options[curren_frame]["width"]
    screan_y=main_window.options[curren_frame]["height"]
    frame_obj=main_window.widged_list[curren_frame]
    main_window.creat_button("back",frame_obj,"Back",[switing_frame,curren_frame,"home_frame"])
    button_width=15
    button_height=2
    width_px=button_width*8+120
    height_px=button_height*8+130
    x_location=(screan_x-width_px)/2
    y_location=(screan_y)-(height_px)
    main_window.button_size("back",width=button_width,height=button_height)
    main_window.button_pozition("back",x_location=x_location,y_location=y_location)
####################################################################################################################################################################
def accountNumber_textbox():

    screan_x=main_window.options["log_in_frame"]["width"]
    screan_y=main_window.options["log_in_frame"]["height"]
    main_window.entry_options["parent"]=main_window.widged_list["log_in_frame"]
    #don't forget to change the shape of the input to *
    main_window.entry_options["width"]=19
    accountNumber_textbox_width_px=main_window.entry_options["width"]*8
    main_window.entry_options["text_lenth"]=10
    main_window.entry_options["x_location"]=(screan_x-accountNumber_textbox_width_px-120)/2
    main_window.entry_options["y_location"]=(screan_y)/3
    main_window.creat_text_box("accountNumber_textbox",check_text_lenth=True)
####################################################################################################################################################################
def cash_withdraw_textbox():

    screan_x=main_window.options["cash_withdraw_frame"]["width"]
    screan_y=main_window.options["cash_withdraw_frame"]["height"]
    main_window.entry_options["parent"]=main_window.widged_list["cash_withdraw_frame"]
    #don't forget to change the shape of the input to *
    main_window.entry_options["width"]=19
    accountNumber_textbox_width_px=main_window.entry_options["width"]*8
    main_window.entry_options["text_lenth"]=10
    main_window.entry_options["x_location"]=(screan_x-accountNumber_textbox_width_px-120)/2
    main_window.entry_options["y_location"]=(screan_y)/3
    main_window.creat_text_box("cash_withdraw_textbox",check_text_lenth=True)
####################################################################################################################################################################
def cash_withdraw_button():

    screan_x=main_window.options["cash_withdraw_frame"]["width"]
    screan_y=main_window.options["cash_withdraw_frame"]["height"]
    button_width=10
    button_height=2
    button_width_px=button_width*8
    button_height_px=button_height*8
    button_x_location=(screan_x-button_width_px-60)/2
    button_y_location=(screan_y-button_height_px)*2/4
    
    main_window.Button_options["parent"]=main_window.widged_list["cash_withdraw_frame"]
    main_window.Button_options["text"]="ENTER"
    main_window.Button_options["call_function"]=[withdraw]
    main_window.Button_options["width"]=button_width
    main_window.Button_options["height"]=button_height
    main_window.Button_options["x_location"]=button_x_location
    main_window.Button_options["y_location"]=button_y_location
    main_window.creat_button("cash_withdraw_button")
def cash_withdraw_label():

    main_window.label_options["parent"]= main_window.widged_list["cash_withdraw_frame"]
    main_window.label_options["text"]="desired amount to withdraw:"
    main_window.label_options["width"]="auto"
    main_window.label_options["height"]="auto"
    main_window.label_options["x_location"]=230
    main_window.label_options["y_location"]=main_window.options["cash_withdraw_textbox"]["y_location"]
    main_window.creat_label("cash_withdraw_label")
####################################################################################################################################################################

def app_window():
    global font_text 
    base_window()
    login_masg_window()
    font_text=main_window.font_init(font_size=13)

def app_frames():
   
    ####################################################################################################################################################################
    log_in_frame()
    home_frame()
    Cash_Withdraw_frame()
    Balance_Inquiry_frame()
    Password_Change_frame()
    Fawry_Service_frame()
    ####################################################################################################################################################################
    #main_window.disable_widget("log_in_frame") 
    ####################################################################################################################################################################
    main_window.disable_widget("cash_withdraw_frame") 
    ####################################################################################################################################################################
    main_window.disable_widget("balance_inquiry_frame") 
    ####################################################################################################################################################################
    main_window.disable_widget("Password_Change_frame")
    ####################################################################################################################################################################
    main_window.disable_widget("fawry_service_frame")
####################################################################################################################################################################
    print("all frames is created")
####################################################################################################################################################################
def app_lables():
    login_label()
    login_masg_label()
    cash_withdraw_label()
    print("all lables is created")
####################################################################################################################################################################
def app_textbox():
    accountNumber_textbox()
    cash_withdraw_textbox()
    print("all textbox is created")
####################################################################################################################################################################
def app_buttons():
    login_button()
    login_masg_button()
    b_Cash_Withdraw()
    b_Balance_Inquiry()
    b_Password_Change()
    b_Fawry_Service()
    b_Exit()
    cash_withdraw_button()
    print("all buttuns is created")
####################################################################################################################################################################
main_window=GUI_app()
####################################################################################################################################################################




app_window()
app_frames()
app_buttons()
app_textbox()
app_lables()




####################################################################################################################################################################
main_window.run_app()






############################################################### #####################################################################################################
save_clints_data()
print("f")







