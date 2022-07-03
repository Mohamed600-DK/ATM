from modules.private_functions import back, switing_frame,title
from modules.GUI import *
import modules.Global_variable as gv
from modules.Prog_Funs import fawry_service
from App.GUI_APP.windows_colors import * 



def Fawry_Service_frame():
    gv.main_window.frame_options["parent"]= gv.main_window.window_list["base_window"]
    gv.main_window.frame_options["x_location"]=0
    gv.main_window.frame_options["y_location"]=0
    gv.main_window.frame_options["width"]=gv.main_window.options["base_window"]["width"]
    gv.main_window.frame_options["height"]=gv.main_window.options["base_window"]["height"]
    gv.main_window.frame_options["relief"]=RIDGE
    gv.main_window.frame_options["bd"]=20
    gv.main_window.frame_options["bg"]=fawry_service_bg_color
    gv.main_window.creat_frame("fawry_service_frame")
    back("fawry_service_frame","home_frame")
    title("fawry_service_frame","fawry service")
    __creat_fawry_recharge_frame()
    gv.main_window.disable_widget("fawry_service_frame")

###################################################################################################################################################################

def b_orange_recharge():
    

    screan_y=gv.main_window.options["fawry_service_frame"]["height"]
    
    button_width=15
    button_height=2
    button_x_location=0
    button_y_location=(screan_y/8)

    gv.main_window.Button_options["parent"]=gv.main_window.widged_list["fawry_service_frame"]
    gv.main_window.Button_options["text"]="Orange Recharge"
    gv.main_window.Button_options["call_function"]=__button_event_orange
    gv.main_window.Button_options["width"]=button_width
    gv.main_window.Button_options["height"]=button_height
    gv.main_window.Button_options["x_location"]=button_x_location
    gv.main_window.Button_options["y_location"]=button_y_location
    gv.main_window.creat_button("b_orange_recharge")

####################################################################################################################################################################
def b_vodafone_recharge():
 
    screan_y=gv.main_window.options["fawry_service_frame"]["height"]
  
    button_width=15
    button_height=2
    button_height_px=button_height*8
    button_x_location=0
    button_y_location=(screan_y/2)-(button_height_px/2)
    
    gv.main_window.Button_options["parent"]=gv.main_window.widged_list["fawry_service_frame"]
    gv.main_window.Button_options["text"]="Vodafone Recharge"
    gv.main_window.Button_options["call_function"]=__button_event_vodafone
    gv.main_window.Button_options["width"]=button_width
    gv.main_window.Button_options["height"]=button_height
    gv.main_window.Button_options["x_location"]=button_x_location
    gv.main_window.Button_options["y_location"]=button_y_location
    
    gv.main_window.creat_button("b_vodafone_recharge")

####################################################################################################################################################################
def b_etisalat_recharge():

    screan_x=gv.main_window.options["fawry_service_frame"]["width"]
    screan_y=gv.main_window.options["fawry_service_frame"]["height"]    
    button_width=15
    button_height=2    
    button_width_px=button_width*8+200
    button_x_location=screan_x-button_width_px
    button_y_location=(screan_y/8)   
    gv.main_window.Button_options["parent"]=gv.main_window.widged_list["fawry_service_frame"]
    gv.main_window.Button_options["text"]="Etisalat Recharge"
    gv.main_window.Button_options["call_function"]=__button_event_etisalat
    gv.main_window.Button_options["width"]=button_width
    gv.main_window.Button_options["height"]=button_height
    gv.main_window.Button_options["x_location"]=button_x_location
    gv.main_window.Button_options["y_location"]=button_y_location
    gv.main_window.creat_button("b_etisalat_recharge")

####################################################################################################################################################################
def b_we_recharge():
    
    screan_x=gv.main_window.options["fawry_service_frame"]["width"]
    screan_y=gv.main_window.options["fawry_service_frame"]["height"]
    button_width=15
    button_height=2
    button_width_px=button_width*8+200
    button_height_px=button_height*8
    button_x_location=screan_x-button_width_px
    button_y_location=(screan_y/2)-(button_height_px/2)    
    gv.main_window.Button_options["parent"]=gv.main_window.widged_list["fawry_service_frame"]
    gv.main_window.Button_options["text"]="We Recharge"
    gv.main_window.Button_options["call_function"]=__button_event_we
    gv.main_window.Button_options["width"]=button_width
    gv.main_window.Button_options["height"]=button_height
    gv.main_window.Button_options["x_location"]=button_x_location
    gv.main_window.Button_options["y_location"]=button_y_location
    gv.main_window.creat_button("b_we_recharge")
    
####################################################################################################################################################################

def __button_event_orange():
    gv.reghatfe_network="Orange"
    gv.main_window.label_text("title",str(gv.reghatfe_network)+" Recharge")
    switing_frame("fawry_service_frame","fawry_recharge_frame")
    gv.main_window.frame_bg("fawry_recharge_frame","orange")
 

def __button_event_vodafone():
    gv.reghatfe_network="Vodafone"
    gv.main_window.label_text("title",str(gv.reghatfe_network)+" Recharge")
    switing_frame("fawry_service_frame","fawry_recharge_frame")
    gv.main_window.frame_bg("fawry_recharge_frame","red") 
def __button_event_etisalat():
    gv.reghatfe_network="Etisalat"
    gv.main_window.label_text("title",str(gv.reghatfe_network)+" Recharge")
    switing_frame("fawry_service_frame","fawry_recharge_frame")       
    gv.main_window.frame_bg("fawry_recharge_frame","green")
def __button_event_we():
    gv.reghatfe_network="We"
    gv.main_window.label_text("title",str(gv.reghatfe_network)+" Recharge")
    switing_frame("fawry_service_frame","fawry_recharge_frame")
    gv.main_window.frame_bg("fawry_recharge_frame","purple")
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################    
def __creat_fawry_recharge_frame():
    __fawry_recharge_body()
    __fawry_recharge_phone_textbox()
    __fawry_recharge_amount_textbox()
    __fawry_recharge_phone_lable()
    __fawry_recharge_amount_lable()
    __fawry_recharge_amount_button()
    back("fawry_recharge_frame","fawry_service_frame")
    
    
def __fawry_recharge_body():
    gv.main_window.frame_options["parent"]= gv.main_window.window_list["base_window"]
    gv.main_window.frame_options["x_location"]=0
    gv.main_window.frame_options["y_location"]=0
    gv.main_window.frame_options["width"]=gv.main_window.options["fawry_service_frame"]["width"]
    gv.main_window.frame_options["height"]=gv.main_window.options["fawry_service_frame"]["height"]
    gv.main_window.frame_options["relief"]=RIDGE
    gv.main_window.frame_options["bd"]=20
    gv.main_window.creat_frame("fawry_recharge_frame",bg="orange")
    back("fawry_recharge_frame") 
    gv.main_window.disable_widget("fawry_recharge_frame")

def __fawry_recharge_phone_textbox():
    screan_x=gv.main_window.options["fawry_recharge_frame"]["width"]
    screan_y=gv.main_window.options["fawry_recharge_frame"]["height"]
    gv.main_window.entry_options["parent"]=gv.main_window.widged_list["fawry_recharge_frame"]
    gv.main_window.entry_options["width"]=19
    accountNumber_textbox_width_px=gv.main_window.entry_options["width"]*8
    gv.main_window.entry_options["text_lenth"]=11
    gv.main_window.entry_options["x_location"]=(screan_x-accountNumber_textbox_width_px-120)/2
    gv.main_window.entry_options["y_location"]=(screan_y)/3
    gv.main_window.creat_text_box("fawry_recharge_phone_textbox",check_text_lenth=True)    
def __fawry_recharge_amount_textbox():
    screan_x=gv.main_window.options["fawry_recharge_frame"]["width"]
    gv.main_window.entry_options["parent"]=gv.main_window.widged_list["fawry_recharge_frame"]
    gv.main_window.entry_options["width"]=19
    accountNumber_textbox_width_px=gv.main_window.entry_options["width"]*8
    gv.main_window.entry_options["text_lenth"]=10000
    gv.main_window.entry_options["x_location"]=(screan_x-accountNumber_textbox_width_px-120)/2
    y_location=gv.main_window.options["fawry_recharge_phone_textbox"]["y_location"]+80
    gv.main_window.entry_options["y_location"]=y_location
    gv.main_window.creat_text_box("fawry_recharge_amount_textbox",check_text_lenth=True)    

def __fawry_recharge_phone_lable():
    gv.main_window.label_options["parent"]= gv.main_window.widged_list["fawry_recharge_frame"]
    gv.main_window.label_options["text"]="Enter Your Phone Number:"
    gv.main_window.label_options["width"]="auto"
    gv.main_window.label_options["height"]="auto"
    gv.main_window.label_options["x_location"]=gv.main_window.options["fawry_recharge_phone_textbox"]["x_location"]-400
    gv.main_window.label_options["y_location"]=gv.main_window.options["fawry_recharge_phone_textbox"]["y_location"]
    gv.main_window.creat_label("fawry_recharge_phone_lable")    
def __fawry_recharge_amount_lable():
    gv.main_window.label_options["parent"]= gv.main_window.widged_list["fawry_recharge_frame"]
    gv.main_window.label_options["text"]="Enter The Amount of recharge:"
    gv.main_window.label_options["width"]="auto"
    gv.main_window.label_options["height"]="auto"
    gv.main_window.label_options["x_location"]=gv.main_window.options["fawry_recharge_amount_textbox"]["x_location"]-420
    gv.main_window.label_options["y_location"]=gv.main_window.options["fawry_recharge_amount_textbox"]["y_location"]
    gv.main_window.creat_label("fawry_recharge_phone_lable")    

def __fawry_recharge_amount_button():
    screan_x=gv.main_window.options["fawry_recharge_frame"]["width"]
    button_width=10
    button_height=2
    button_width_px=button_width*8
    button_x_location=(screan_x-button_width_px-60)/2
    button_y_location=gv.main_window.options["fawry_recharge_amount_textbox"]["y_location"]+80
    gv.main_window.Button_options["parent"]=gv.main_window.widged_list["fawry_recharge_frame"]
    gv.main_window.Button_options["text"]="Recharge"
    gv.main_window.Button_options["call_function"]=fawry_service
    gv.main_window.Button_options["width"]=button_width
    gv.main_window.Button_options["height"]=button_height
    gv.main_window.Button_options["x_location"]=button_x_location
    gv.main_window.Button_options["y_location"]=button_y_location
    gv.main_window.creat_button("fawry_recharge_amount_button")

