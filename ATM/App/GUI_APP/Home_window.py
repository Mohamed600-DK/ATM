
import modules.Global_variable as gv
from modules.private_functions import *
from modules.GUI import RIDGE
from App.GUI_APP.windows_colors import * 

def home_frame():
    gv.main_window.frame_options["parent"]= gv.main_window.window_list["base_window"]
    gv.main_window.frame_options["x_location"]=0
    gv.main_window.frame_options["y_location"]=0
    gv.main_window.frame_options["width"]=gv.main_window.options["base_window"]["width"]
    gv.main_window.frame_options["height"]=gv.main_window.options["base_window"]["height"]
    gv.main_window.frame_options["relief"]=RIDGE
    gv.main_window.frame_options["bd"]=20
    gv.main_window.frame_options["bg"]=home_bg_color
    gv.main_window.creat_frame("home_frame")
    title("home_frame","Home")
    
    gv.main_window.disable_widget("home_frame")
###################################################################################################################################################################
def b_Cash_Withdraw():
   
    screan_x=gv.main_window.options["home_frame"]["width"]
    screan_y=gv.main_window.options["home_frame"]["height"]
    
    button_width=15
    button_height=2
    button_x_location=0
    button_y_location=(screan_y/8)

    gv.main_window.Button_options["parent"]=gv.main_window.widged_list["home_frame"]
    gv.main_window.Button_options["text"]="Cash Withdraw"
    gv.main_window.Button_options["call_function"]=b_Cash_Withdraw_event
    gv.main_window.Button_options["width"]=button_width
    gv.main_window.Button_options["height"]=button_height
    gv.main_window.Button_options["x_location"]=button_x_location
    gv.main_window.Button_options["y_location"]=button_y_location
    gv.main_window.creat_button("b_Cash_Withdraw")
    #back("cash_withdraw_frame")
####################################################################################################################################################################
def b_Balance_Inquiry():
    
    screan_x=gv.main_window.options["home_frame"]["width"]
    screan_y=gv.main_window.options["home_frame"]["height"]
  
    button_width=15
    button_height=2
    button_height_px=button_height*8
    button_x_location=0
    button_y_location=(screan_y/2)-(button_height_px/2)
    
    gv.main_window.Button_options["parent"]=gv.main_window.widged_list["home_frame"]
    gv.main_window.Button_options["text"]="Balance Inquiry"
    gv.main_window.Button_options["call_function"]=b_Balance_Inquiry_event
    gv.main_window.Button_options["width"]=button_width
    gv.main_window.Button_options["height"]=button_height
    gv.main_window.Button_options["x_location"]=button_x_location
    gv.main_window.Button_options["y_location"]=button_y_location
    
    gv.main_window.creat_button("b_Balance_Inquiry")
    #back("balance_inquiry_frame")
####################################################################################################################################################################
def b_Password_Change():
    screan_x=gv.main_window.options["home_frame"]["width"]
    screan_y=gv.main_window.options["home_frame"]["height"]    
    button_width=15
    button_height=2
    button_width_px=button_width*8+200
    button_x_location=screan_x-button_width_px
    button_y_location=(screan_y/8)   
    gv.main_window.Button_options["parent"]=gv.main_window.widged_list["home_frame"]
    gv.main_window.Button_options["text"]="Password Change"
    gv.main_window.Button_options["call_function"]=b_Password_Change_event
    gv.main_window.Button_options["width"]=button_width
    gv.main_window.Button_options["height"]=button_height
    gv.main_window.Button_options["x_location"]=button_x_location
    gv.main_window.Button_options["y_location"]=button_y_location
    gv.main_window.creat_button("b_Password_Change")
    #back("Password_Change_frame")
####################################################################################################################################################################
def b_Fawry_Service():
    screan_x=gv.main_window.options["home_frame"]["width"]
    screan_y=gv.main_window.options["home_frame"]["height"]
    button_width=15
    button_height=2
    button_width_px=button_width*8+200
    button_height_px=button_height*8
    button_x_location=screan_x-button_width_px
    button_y_location=(screan_y/2)-(button_height_px/2)    
    gv.main_window.Button_options["parent"]=gv.main_window.widged_list["home_frame"]
    gv.main_window.Button_options["text"]="Fawry Service"
    gv.main_window.Button_options["call_function"]=b_Fawry_Service_event
    gv.main_window.Button_options["width"]=button_width
    gv.main_window.Button_options["height"]=button_height
    gv.main_window.Button_options["x_location"]=button_x_location
    gv.main_window.Button_options["y_location"]=button_y_location
    gv.main_window.creat_button("b_Fawry_Service")
    
####################################################################################################################################################################
def b_Exit():

    screan_x=gv.main_window.options["home_frame"]["width"]
    screan_y=gv.main_window.options["home_frame"]["height"]
  
    button_width=15
    button_height=2
    width_px=button_width*8+120
    height_px=button_height*8+130
    button_x_location=(screan_x-width_px)/2
    button_y_location=(screan_y)-(height_px)


    gv.main_window.Button_options["parent"]=gv.main_window.widged_list["home_frame"]
    gv.main_window.Button_options["text"]="Exit"
    gv.main_window.Button_options["call_function"]=b_Exit_event
    gv.main_window.Button_options["width"]=button_width
    gv.main_window.Button_options["height"]=button_height
    gv.main_window.Button_options["x_location"]=button_x_location
    gv.main_window.Button_options["y_location"]=button_y_location
    gv.main_window.creat_button("b_exit")
####################################################################################################################################################################
def b_Cash_Withdraw_event():
    try:
        switing_frame("home_frame","cash_withdraw_frame")
    except:
        print("no define cash_withdraw_frame ")
        gv.main_window.enable_widget("home_frame") 

    

def b_Balance_Inquiry_event():
    
    
    try:
        switing_frame("home_frame","balance_inquiry_frame")
    except:
        print("no define Balance_Inquiry_frame")
        gv.main_window.enable_widget("home_frame")   
    try:
        gv.main_window.label_text("display_name",gv.clint["name"])
        gv.main_window.label_text("display_balance",str(gv.clint["Balance"])+" EGP" )
    except:
        print("error") 
     


def b_Fawry_Service_event():
    try:
        switing_frame("home_frame","fawry_service_frame")
    except:
        print("no define Fawry_Service_frame ")
        gv.main_window.enable_widget("home_frame") 
        
        
def b_Password_Change_event():
    try:
        switing_frame("home_frame","password_change_frame")
    except:
        print("no define Password_Change_frame ")
        gv.main_window.enable_widget("home_frame") 
def b_Exit_event():
    gv.main_window.exit_app()


