
from modules.GUI import RIDGE
import modules.Global_variable as gv
from modules.private_functions import back,title


def Balance_Inquiry_frame():
    gv.main_window.frame_options["parent"]= gv.main_window.window_list["base_window"]
    gv.main_window.frame_options["x_location"]=0
    gv.main_window.frame_options["y_location"]=0
    gv.main_window.frame_options["width"]=gv.main_window.options["base_window"]["width"]
    gv.main_window.frame_options["height"]=gv.main_window.options["base_window"]["height"]
    gv.main_window.frame_options["relief"]=RIDGE
    gv.main_window.frame_options["bd"]=20
    gv.main_window.creat_frame("balance_inquiry_frame",bg="orange") 
    title("balance_inquiry_frame","Balance Inquiry")
    back("balance_inquiry_frame","home_frame")
    gv.main_window.button_text("back","Ok")
    b_x_loation=gv.main_window.options["balance_inquiry_frame"]["width"]
    b_x_loation=(b_x_loation/2)-60
    b_y_loation=gv.main_window.options["balance_inquiry_frame"]["height"]*3/5
    gv.main_window.button_pozition("back",b_x_loation,b_y_loation)
    gv.main_window.button_size("back",5,1)
    gv.main_window.disable_widget("balance_inquiry_frame")

def display_name():
    screan_x=gv.main_window.options["balance_inquiry_frame"]["width"]
    screan_y=gv.main_window.options["balance_inquiry_frame"]["height"]
    gv.main_window.label_options["parent"]= gv.main_window.widged_list["balance_inquiry_frame"]
    gv.main_window.label_options["width"]="auto"
    gv.main_window.label_options["height"]="auto"
    gv.main_window.label_options["x_location"]=(screan_x/2)
    gv.main_window.label_options["y_location"]=(screan_y)/3
    gv.main_window.creat_label("display_name")

def display_balance():
    positive_y_shift=80
    gv.main_window.label_options["parent"]= gv.main_window.widged_list["balance_inquiry_frame"]
    gv.main_window.label_options["width"]="auto"
    gv.main_window.label_options["height"]="auto"
    gv.main_window.label_options["x_location"]=gv.main_window.options["display_name"]["x_location"]
    gv.main_window.label_options["y_location"]=gv.main_window.options["display_name"]["y_location"]+positive_y_shift
    gv.main_window.creat_label("display_balance")

def display_name_lable():
    nigative_x_shift=230
    gv.main_window.label_options["parent"]= gv.main_window.widged_list["balance_inquiry_frame"]
    gv.main_window.label_options["text"]="Your Name: "
    gv.main_window.label_options["width"]="auto"
    gv.main_window.label_options["height"]="auto"
    gv.main_window.label_options["x_location"]=gv.main_window.options["display_name"]["x_location"]-nigative_x_shift
    gv.main_window.label_options["y_location"]=gv.main_window.options["display_name"]["y_location"]
    gv.main_window.creat_label("display_name_lable")
    

def display_balance_lable():
    gv.main_window.label_options["parent"]= gv.main_window.widged_list["balance_inquiry_frame"]
    gv.main_window.label_options["text"]="Your Balance: "
    gv.main_window.label_options["width"]="auto"
    gv.main_window.label_options["height"]="auto"
    gv.main_window.label_options["x_location"]=gv.main_window.options["display_name_lable"]["x_location"]
    gv.main_window.label_options["y_location"]=gv.main_window.options["display_balance"]["y_location"]
    gv.main_window.creat_label("display_balance_lable")
 
 