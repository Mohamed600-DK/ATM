from modul.Global_variable import *

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
