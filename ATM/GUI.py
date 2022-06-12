from tkinter import *


class window(Tk):
    def __init__(self,window_name):
        super().__init__()
        self.title(window_name)
  
    def creat_window(self,window_width=None,window_height=None):
        if (window_width !=None and window_height!=None ):
           
            screen_width_x = self.winfo_screenwidth()
            screen_height_y = self.winfo_screenheight()
            window_width_x=window_width
            window_height_y=window_height-30
            shift_x=int((screen_width_x-window_width_x)/2)
            shift_y=int((screen_height_y-window_height_y)/2)
            geometry_value=str(window_width_x)+"x"+str(window_height_y)+"+"+str(shift_x)+"+"+str(shift_y)
            self.geometry(geometry_value)
       
        elif((window_width ==None and window_height==None )):
            self.wm_attributes("-fullscreen","True")
            screen_width_x = self.winfo_screenwidth()
            screen_height_y = self.winfo_screenheight()



class button(Button):
    Button_option={
        "text":"mohamed",
        "command":None,
        "width":"20",
        "heigh":"20",
        "bg":None,
        "fg":None,
        }
    x_offsit=0
    y_offsit=0
    def creat_button(self,window):
       super().__init__(window,self.Button_option)
       
       self.place(x=self.x_offsit,y=self.y_offsit) 
    def button_text(self,text=str()):
        self.Button_option["text"]=text
    def button_bg(self,color=str()):
        self.Button_option["bg"]=color
    def button_fg(self,color=str()):
        self.Button_option["fg"]=color        
    def button_call_fun(self,fun):
        self.Button_option["command"]=fun
    def button_size(self,width=str(),hight=str()):
        self.Button_option["width"]=width
        self.Button_option["hight"]=hight
    def button_pozition(self,x=int(),y=int()):
        self.x_offsit=x
        self.y_offsit=y

w=window("hellow")
w.creat_window()
b=button()
b.button_text("hellow")
b.button_pozition(100,200)
b.creat_button(w)
w.mainloop()   

