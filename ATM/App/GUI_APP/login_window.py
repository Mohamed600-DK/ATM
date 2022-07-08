from modules.GUI import *
import modules.Global_variable  as gv
from App.GUI_APP.windows_colors import * 
from modules.Prog_Funs import log_in
from modules.private_functions import back, switing_frame,title
####################################################################################################################################################################

def log_in_frame():
    gv.main_window.frame_options["parent"]= gv.main_window.window_list["base_window"]
    gv.main_window.frame_options["x_location"]=0
    gv.main_window.frame_options["y_location"]=0
    gv.main_window.frame_options["width"]=gv.main_window.options["base_window"]["width"]
    gv.main_window.frame_options["height"]=gv.main_window.options["base_window"]["height"]
    gv.main_window.frame_options["relief"]=RIDGE
    gv.main_window.frame_options["bd"]=20
    gv.main_window.frame_options["bg"]=login_bg_color
    gv.main_window.creat_frame("log_in_frame")
    title("log_in_frame","Log In")
    
####################################################################################################################################################################
def accountNumber_textbox():

    screan_x=gv.main_window.options["log_in_frame"]["width"]
    screan_y=gv.main_window.options["log_in_frame"]["height"]
    gv.main_window.entry_options["parent"]=gv.main_window.widged_list["log_in_frame"]
    #don't forget to change the shape of the input to *
    gv.main_window.entry_options["width"]=19
    accountNumber_textbox_width_px=gv.main_window.entry_options["width"]*8
    gv.main_window.entry_options["text_lenth"]=gv.account_number_len
    gv.main_window.entry_options["x_location"]=(screan_x-accountNumber_textbox_width_px-120)/2
    gv.main_window.entry_options["y_location"]=(screan_y)/3
    gv.main_window.creat_text_box("accountNumber_textbox",check_text_lenth=True)
####################################################################################################################################################################

def accountPassword_textbox():

    screan_x=gv.main_window.options["log_in_frame"]["width"]
    screan_y=gv.main_window.options["log_in_frame"]["height"]
    gv.main_window.entry_options["parent"]=gv.main_window.widged_list["log_in_frame"]
    gv.main_window.entry_options["width"]=19
    accountNumber_textbox_width_px=gv.main_window.entry_options["width"]*8
    gv.main_window.entry_options["text_lenth"]=gv.account_password_len
    gv.main_window.entry_options["x_location"]=(screan_x-accountNumber_textbox_width_px-120)/2
    gv.main_window.entry_options["y_location"]=(screan_y)/3
    gv.main_window.creat_text_box("accountPassword_textbox",check_text_lenth=True,text_style="*")
    gv.main_window.disable_widget("accountPassword_textbox")
####################################################################################################################################################################

def login_label():

    gv.main_window.label_options["parent"]= gv.main_window.widged_list["log_in_frame"]
    gv.main_window.label_options["text"]="Enter Your Account Name:"
    gv.main_window.label_options["width"]="auto"
    gv.main_window.label_options["height"]="auto"
    gv.main_window.label_options["x_location"]=gv.main_window.options["accountNumber_textbox"]["x_location"]-420
    gv.main_window.label_options["y_location"]=gv.main_window.options["accountNumber_textbox"]["y_location"]
    gv.main_window.creat_label("login_label")

####################################################################################################################################################################
def login_button():

    screan_x=gv.main_window.options["log_in_frame"]["width"]
    screan_y=gv.main_window.options["log_in_frame"]["height"]
    button_width=10
    button_height=2
    button_width_px=button_width*8
    button_height_px=button_height*8
    button_x_location=(screan_x-button_width_px-60)/2
    button_y_location=(screan_y-button_height_px)*2/4
    
    gv.main_window.Button_options["parent"]=gv.main_window.widged_list["log_in_frame"]
    gv.main_window.Button_options["text"]="ENTER"
    gv.main_window.Button_options["call_function"]=[log_in]
    gv.main_window.Button_options["width"]=button_width
    gv.main_window.Button_options["height"]=button_height
    gv.main_window.Button_options["x_location"]=button_x_location
    gv.main_window.Button_options["y_location"]=button_y_location
    gv.main_window.creat_button("login_button")
###################################################################################################################################################################
