from modules.GUI import *
import modules.Global_variable as gv
from modules.private_functions import back,title
from modules.Prog_Funs import change_password
from App.GUI_APP.windows_colors import * 
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################

def password_change_frame():
    gv.main_window.frame_options["parent"]= gv.main_window.window_list["base_window"]
    gv.main_window.frame_options["x_location"]=0
    gv.main_window.frame_options["y_location"]=0
    gv.main_window.frame_options["width"]=gv.main_window.options["base_window"]["width"]
    gv.main_window.frame_options["height"]=gv.main_window.options["base_window"]["height"]
    gv.main_window.frame_options["relief"]=RIDGE
    gv.main_window.frame_options["bd"]=20
    gv.main_window.frame_options["bg"]=password_change_bg_color
    gv.main_window.creat_frame("password_change_frame")
    title("password_change_frame","Change Password")
    back("password_change_frame","home_frame")
    gv.main_window.disable_widget("password_change_frame")
#####################################################################################################################
def password_change_textbox():
    screan_x=gv.main_window.options["password_change_frame"]["width"]
    screan_y=gv.main_window.options["password_change_frame"]["height"]
    gv.main_window.entry_options["parent"]=gv.main_window.widged_list["password_change_frame"]
    gv.main_window.entry_options["width"]=19
    accountNumber_textbox_width_px=gv.main_window.entry_options["width"]*8
    gv.main_window.entry_options["text_lenth"]=4
    gv.main_window.entry_options["x_location"]=(screan_x-accountNumber_textbox_width_px-120)/2
    gv.main_window.entry_options["y_location"]=(screan_y)/3
    gv.main_window.creat_text_box("password_change_textbox",check_text_lenth=True)    
#####################################################################################################################
def comfirm_password_change_textbox():
    screan_x=gv.main_window.options["password_change_frame"]["width"]
    gv.main_window.entry_options["parent"]=gv.main_window.widged_list["password_change_frame"]
    gv.main_window.entry_options["width"]=19
    accountNumber_textbox_width_px=gv.main_window.entry_options["width"]*8
    gv.main_window.entry_options["text_lenth"]=4
    gv.main_window.entry_options["x_location"]=(screan_x-accountNumber_textbox_width_px-120)/2
    y_location=gv.main_window.options["password_change_textbox"]["y_location"]+80
    gv.main_window.entry_options["y_location"]=y_location
    gv.main_window.creat_text_box("comfirm_password_change_textbox",check_text_lenth=True)    
#####################################################################################################################
def password_change_lable():
    gv.main_window.label_options["parent"]= gv.main_window.widged_list["password_change_frame"]
    gv.main_window.label_options["text"]="Enter Your New Password:"
    gv.main_window.label_options["width"]="auto"
    gv.main_window.label_options["height"]="auto"
    gv.main_window.label_options["x_location"]=gv.main_window.options["password_change_textbox"]["x_location"]-400
    gv.main_window.label_options["y_location"]=gv.main_window.options["password_change_textbox"]["y_location"]
    gv.main_window.creat_label("password_change_lable")    
#####################################################################################################################
def comfirm_password_change_lable():
    gv.main_window.label_options["parent"]= gv.main_window.widged_list["password_change_frame"]
    gv.main_window.label_options["text"]="Comferm Your Password: "
    gv.main_window.label_options["width"]="auto"
    gv.main_window.label_options["height"]="auto"
    gv.main_window.label_options["x_location"]=gv.main_window.options["password_change_lable"]["x_location"]
    gv.main_window.label_options["y_location"]=gv.main_window.options["comfirm_password_change_textbox"]["y_location"]
    gv.main_window.creat_label("comfirm_password_change_lable")    
#####################################################################################################################
def password_change_button():
    screan_x=gv.main_window.options["password_change_frame"]["width"]
    button_width=10
    button_height=2
    button_width_px=button_width*8
    button_x_location=(screan_x-button_width_px+200)/3
    button_y_location=gv.main_window.options["comfirm_password_change_textbox"]["y_location"]+100
    gv.main_window.Button_options["parent"]=gv.main_window.widged_list["password_change_frame"]
    gv.main_window.Button_options["text"]="Change Password"
    gv.main_window.Button_options["call_function"]=change_password
    gv.main_window.Button_options["width"]="auto"
    gv.main_window.Button_options["height"]=button_height
    gv.main_window.Button_options["x_location"]=button_x_location
    gv.main_window.Button_options["y_location"]=button_y_location
    gv.main_window.creat_button("password_change_button")

    