from modul.Global_variable import *
from modul.Prog_Funs import *

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
