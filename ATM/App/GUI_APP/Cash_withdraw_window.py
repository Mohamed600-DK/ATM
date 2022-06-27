from modules.GUI import *
import modules.Global_variable as gv
from modules.Prog_Funs import withdraw
from modules.private_functions import back,title
def Cash_Withdraw_frame():
    gv.main_window.frame_options["parent"]= gv.main_window.window_list["base_window"]
    gv.main_window.frame_options["x_location"]=0
    gv.main_window.frame_options["y_location"]=0
    gv.main_window.frame_options["width"]=gv.main_window.options["base_window"]["width"]
    gv.main_window.frame_options["height"]=gv.main_window.options["base_window"]["height"]
    gv.main_window.frame_options["relief"]=RIDGE
    gv.main_window.frame_options["bd"]=20
    gv.main_window.creat_frame("cash_withdraw_frame",bg="orange")
    back("cash_withdraw_frame","home_frame")
    title("cash_withdraw_frame","Cash Withdraw")

    
    gv.main_window.disable_widget("cash_withdraw_frame")
####################################################################################################################################################################
def cash_withdraw_button():

    screan_x=gv.main_window.options["cash_withdraw_frame"]["width"]
    screan_y=gv.main_window.options["cash_withdraw_frame"]["height"]
    button_width=10
    button_height=2
    button_width_px=button_width*8
    button_height_px=button_height*8
    button_x_location=(screan_x-button_width_px-60)/2
    button_y_location=(screan_y-button_height_px)*2/4
    
    gv.main_window.Button_options["parent"]=gv.main_window.widged_list["cash_withdraw_frame"]
    gv.main_window.Button_options["text"]="ENTER"
    gv.main_window.Button_options["call_function"]=withdraw
    gv.main_window.Button_options["width"]=button_width
    gv.main_window.Button_options["height"]=button_height
    gv.main_window.Button_options["x_location"]=button_x_location
    gv.main_window.Button_options["y_location"]=button_y_location
    gv.main_window.creat_button("cash_withdraw_button")
####################################################################################################################################################################   
def cash_withdraw_label():

    gv.main_window.label_options["parent"]= gv.main_window.widged_list["cash_withdraw_frame"]
    gv.main_window.label_options["text"]="desired amount to withdraw:"
    gv.main_window.label_options["width"]="auto"
    gv.main_window.label_options["height"]="auto"
    gv.main_window.label_options["x_location"]=gv.main_window.options["cash_withdraw_textbox"]["x_location"]-400
    gv.main_window.label_options["y_location"]=gv.main_window.options["cash_withdraw_textbox"]["y_location"]
    gv.main_window.creat_label("cash_withdraw_label")
####################################################################################################################################################################   
def cash_withdraw_textbox():

    screan_x=gv.main_window.options["cash_withdraw_frame"]["width"]
    screan_y=gv.main_window.options["cash_withdraw_frame"]["height"]
    gv.main_window.entry_options["parent"]=gv.main_window.widged_list["cash_withdraw_frame"]
    gv.main_window.entry_options["width"]=19
    accountNumber_textbox_width_px=gv.main_window.entry_options["width"]*8
    gv.main_window.entry_options["text_lenth"]=10
    gv.main_window.entry_options["x_location"]=(screan_x-accountNumber_textbox_width_px-120)/2
    gv.main_window.entry_options["y_location"]=(screan_y)/3
    gv.main_window.creat_text_box("cash_withdraw_textbox",check_text_lenth=True)
####################################################################################################################################################################
    