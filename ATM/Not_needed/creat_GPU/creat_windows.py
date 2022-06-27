from modul.Global_variable import *
from modul.Prog_Funs import *

def base_window():
    global font_text
    main_window.creat_window(window_name="base_window") 
    font_text=main_window.font_init(font_size=13)

def login_masg_window():


        root=main_window.creat_toplevelwindow("login_masg",title="Massage",width=250,height=150,x_location=300,y_location=300,bg="red")
        main_window.options["login_masg"]["parent"]= main_window.window_list["base_window"]
        #root.grid_columnconfigure(0,weight=1)
        root.grid_columnconfigure(1,weight=1)
        root.grid_rowconfigure(0,weight=1)
        root.grid_rowconfigure(1,weight=1)
        root.grid_rowconfigure(2,weight=1)
        main_window.disable_window("login_masg") 
