
import modules.Global_variable as gv
from modules.GUI import CENTER

def login_masg_window():


    root=gv.main_window.creat_toplevelwindow("login_masg",title="Massage",width=250,height=150,x_location=300,y_location=300,bg="red")
    gv.main_window.options["login_masg"]["parent"]= gv.main_window.window_list["base_window"]
    #root.grid_columnconfigure(0,weight=1)
    root.grid_columnconfigure(1,weight=1)
    root.grid_rowconfigure(0,weight=1)
    root.grid_rowconfigure(1,weight=1)
    root.grid_rowconfigure(2,weight=1)
    gv.main_window.disable_window("login_masg") 

def login_masg_button():
    
    gv.main_window.Button_options["parent"]=gv.main_window.window_list["login_masg"]
    gv.main_window.Button_options["text"]="ok"
    gv.main_window.Button_options["call_function"]=__login_masg_button_event
    gv.main_window.Button_options["width"]="auto"
    gv.main_window.Button_options["height"]=1
    gv.main_window.Button_options["x_location"]=100
    gv.main_window.Button_options["y_location"]=110
    messg_font_text=messg_font_text=gv.main_window.font_init(font_size=gv.messg_font_size)
    button_obj=gv.main_window.creat_button(button_name="login_masg_button",font=messg_font_text)
    button_obj.grid(row=2,column=1)
############################################################################################################################
def login_masg_label():
    global messg_font_text
    gv.main_window.label_options["parent"]= gv.main_window.window_list["login_masg"]
    gv.main_window.label_options["x_location"]=12
    gv.main_window.label_options["y_location"]=5
    gv.main_window.label_options["width"]=26
    gv.main_window.label_options["height"]=5
    gv.main_window.label_options["justify"]=CENTER
    messg_font_text=messg_font_text=gv.main_window.font_init(font_size=gv.messg_font_size)
    label_obj=gv.main_window.creat_label("login_masg_label",font_text=messg_font_text,bg="blue")
    label_obj.grid(row=1,column=1)
####################################################################################################################################################################
def __login_masg_button_event():
    gv.main_window.disable_window("login_masg")
