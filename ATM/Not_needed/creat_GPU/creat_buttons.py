from    modul.Global_variable  import *
from    modul.Prog_Funs        import *
def login_masg_button():
    
    main_window.Button_options["parent"]=main_window.window_list["login_masg"]
    main_window.Button_options["text"]="ok"
    main_window.Button_options["call_function"]=[main_window.disable_window,"login_masg"]
    main_window.Button_options["width"]="auto"
    main_window.Button_options["height"]=1
    main_window.Button_options["x_location"]=100
    main_window.Button_options["y_location"]=110
    messg_font_text=messg_font_text=main_window.font_init(font_size=messg_font_size)
    button_obj=main_window.creat_button(button_name="login_masg_button",font=messg_font_text)
    button_obj.grid(row=2,column=1)
####################################################################################################################################################################
def login_button():

    screan_x=main_window.options["log_in_frame"]["width"]
    screan_y=main_window.options["log_in_frame"]["height"]
    button_width=10
    button_height=2
    button_width_px=button_width*8
    button_height_px=button_height*8
    button_x_location=(screan_x-button_width_px-60)/2
    button_y_location=(screan_y-button_height_px)*2/4
    
    main_window.Button_options["parent"]=main_window.widged_list["log_in_frame"]
    main_window.Button_options["text"]="ENTER"
    main_window.Button_options["call_function"]=[log_in]
    main_window.Button_options["width"]=button_width
    main_window.Button_options["height"]=button_height
    main_window.Button_options["x_location"]=button_x_location
    main_window.Button_options["y_location"]=button_y_location
    main_window.creat_button("login_button")
###################################################################################################################################################################
def b_Cash_Withdraw():
   
    screan_x=main_window.options["home_frame"]["width"]
    screan_y=main_window.options["home_frame"]["height"]
    
    button_width=15
    button_height=2
    button_x_location=0
    button_y_location=(screan_y/8)

    main_window.Button_options["parent"]=main_window.widged_list["home_frame"]
    main_window.Button_options["text"]="Cash Withdraw"
    main_window.Button_options["call_function"]=[switing_frame,"home_frame","cash_withdraw_frame"]
    main_window.Button_options["width"]=button_width
    main_window.Button_options["height"]=button_height
    main_window.Button_options["x_location"]=button_x_location
    main_window.Button_options["y_location"]=button_y_location
    main_window.creat_button("b_Cash_Withdraw")
    #back("cash_withdraw_frame")
####################################################################################################################################################################
def b_Balance_Inquiry():
    
    screan_x=main_window.options["home_frame"]["width"]
    screan_y=main_window.options["home_frame"]["height"]
  
    button_width=15
    button_height=2
    button_height_px=button_height*8
    button_x_location=0
    button_y_location=(screan_y/2)-(button_height_px/2)
    
    main_window.Button_options["parent"]=main_window.widged_list["home_frame"]
    main_window.Button_options["text"]="Balance Inquiry"
    main_window.Button_options["call_function"]=[switing_frame,"home_frame","balance_inquiry_frame"]
    main_window.Button_options["width"]=button_width
    main_window.Button_options["height"]=button_height
    main_window.Button_options["x_location"]=button_x_location
    main_window.Button_options["y_location"]=button_y_location
    
    main_window.creat_button("b_Balance_Inquiry")
    #back("balance_inquiry_frame")
####################################################################################################################################################################
def b_Password_Change():
    screan_x=main_window.options["home_frame"]["width"]
    screan_y=main_window.options["home_frame"]["height"]    
    button_width=15
    button_height=2
    button_width_px=button_width*8+200
    button_x_location=screan_x-button_width_px
    button_y_location=(screan_y/8)   
    main_window.Button_options["parent"]=main_window.widged_list["home_frame"]
    main_window.Button_options["text"]="Password Change"
    main_window.Button_options["call_function"]=[switing_frame,"home_frame","Password_Change_frame"]
    main_window.Button_options["width"]=button_width
    main_window.Button_options["height"]=button_height
    main_window.Button_options["x_location"]=button_x_location
    main_window.Button_options["y_location"]=button_y_location
    main_window.creat_button("b_Password_Change")
    #back("Password_Change_frame")
####################################################################################################################################################################
def b_Fawry_Service():
    screan_x=main_window.options["home_frame"]["width"]
    screan_y=main_window.options["home_frame"]["height"]
    button_width=15
    button_height=2
    button_width_px=button_width*8+200
    button_height_px=button_height*8
    button_x_location=screan_x-button_width_px
    button_y_location=(screan_y/2)-(button_height_px/2)    
    main_window.Button_options["parent"]=main_window.widged_list["home_frame"]
    main_window.Button_options["text"]="Fawry Service"
    main_window.Button_options["call_function"]=[switing_frame,"home_frame","fawry_service_frame"]
    main_window.Button_options["width"]=button_width
    main_window.Button_options["height"]=button_height
    main_window.Button_options["x_location"]=button_x_location
    main_window.Button_options["y_location"]=button_y_location
    main_window.creat_button("b_Fawry_Service")
    #back("fawry_service_frame")
####################################################################################################################################################################
def b_Exit():

    screan_x=main_window.options["home_frame"]["width"]
    screan_y=main_window.options["home_frame"]["height"]
  
    button_width=15
    button_height=2
    width_px=button_width*8+120
    height_px=button_height*8+130
    button_x_location=(screan_x-width_px)/2
    button_y_location=(screan_y)-(height_px)


    main_window.Button_options["parent"]=main_window.widged_list["home_frame"]
    main_window.Button_options["text"]="Exit"
    main_window.Button_options["call_function"]=[main_window.exit_app]
    main_window.Button_options["width"]=button_width
    main_window.Button_options["height"]=button_height
    main_window.Button_options["x_location"]=button_x_location
    main_window.Button_options["y_location"]=button_y_location
    main_window.creat_button("b_exit")
####################################################################################################################################################################
def back(curren_frame):
    screan_x=main_window.options[curren_frame]["width"]
    screan_y=main_window.options[curren_frame]["height"]
    frame_obj=main_window.widged_list[curren_frame]
    main_window.creat_button("back",frame_obj,"Back",[switing_frame,curren_frame,"home_frame"])
    button_width=15
    button_height=2
    width_px=button_width*8+120
    height_px=button_height*8+130
    x_location=(screan_x-width_px)/2
    y_location=(screan_y)-(height_px)
    main_window.button_size("back",width=button_width,height=button_height)
    main_window.button_pozition("back",x_location=x_location,y_location=y_location)
####################################################################################################################################################################
def cash_withdraw_button():

    screan_x=main_window.options["cash_withdraw_frame"]["width"]
    screan_y=main_window.options["cash_withdraw_frame"]["height"]
    button_width=10
    button_height=2
    button_width_px=button_width*8
    button_height_px=button_height*8
    button_x_location=(screan_x-button_width_px-60)/2
    button_y_location=(screan_y-button_height_px)*2/4
    
    main_window.Button_options["parent"]=main_window.widged_list["cash_withdraw_frame"]
    main_window.Button_options["text"]="ENTER"
    main_window.Button_options["call_function"]=[withdraw]
    main_window.Button_options["width"]=button_width
    main_window.Button_options["height"]=button_height
    main_window.Button_options["x_location"]=button_x_location
    main_window.Button_options["y_location"]=button_y_location
    main_window.creat_button("cash_withdraw_button")