from modul.Global_variable import *
from modul.Prog_Funs import *

############################################################################################################################
def login_masg_label():
    global messg_font_text
    main_window.label_options["parent"]= main_window.window_list["login_masg"]
    main_window.label_options["x_location"]=12
    main_window.label_options["y_location"]=5
    main_window.label_options["width"]=26
    main_window.label_options["height"]=5
    main_window.label_options["justify"]=CENTER
    messg_font_text=messg_font_text=main_window.font_init(font_size=messg_font_size)
    label_obj=main_window.creat_label("login_masg_label",font_text=messg_font_text,bg="blue")
    label_obj.grid(row=1,column=1)
####################################################################################################################################################################
def login_label():

    main_window.label_options["parent"]= main_window.widged_list["log_in_frame"]
    main_window.label_options["text"]="Enter Your Account Name:"
    main_window.label_options["width"]="auto"
    main_window.label_options["height"]="auto"
    main_window.label_options["x_location"]=main_window.options["accountNumber_textbox"]["x_location"]-420
    main_window.label_options["y_location"]=main_window.options["accountNumber_textbox"]["y_location"]
    main_window.creat_label("login_label")

def cash_withdraw_label():

    main_window.label_options["parent"]= main_window.widged_list["cash_withdraw_frame"]
    main_window.label_options["text"]="desired amount to withdraw:"
    main_window.label_options["width"]="auto"
    main_window.label_options["height"]="auto"
    main_window.label_options["x_location"]=main_window.options["cash_withdraw_textbox"]["x_location"]-400
    main_window.label_options["y_location"]=main_window.options["cash_withdraw_textbox"]["y_location"]
    main_window.creat_label("cash_withdraw_label")
####################################################################################################################################################################
    