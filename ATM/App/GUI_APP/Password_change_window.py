from modules.GUI import *
import modules.Global_variable as gv
from modules.private_functions import back, switing_frame,title


def Password_Change_frame():
    gv.main_window.frame_options["parent"]= gv.main_window.window_list["base_window"]
    gv.main_window.frame_options["x_location"]=0
    gv.main_window.frame_options["y_location"]=0
    gv.main_window.frame_options["width"]=gv.main_window.options["base_window"]["width"]
    gv.main_window.frame_options["height"]=gv.main_window.options["base_window"]["height"]
    gv.main_window.frame_options["relief"]=RIDGE
    gv.main_window.frame_options["bd"]=20
    gv.main_window.creat_frame("password_change_frame",bg="orange")
    title("password_change_frame","Password Change")
    back("password_change_frame","home_frame")
    gv.main_window.disable_widget("password_change_frame")