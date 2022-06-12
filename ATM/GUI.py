from tkinter import *


class window(Tk):
    def __init__(self,window_name):
        super().__init__()
        self.title(window_name)
  
    def creat_window(self,window_width=None,window_height=None):
        if (window_width !=None and window_height!=None ):
            window_width=int(window_width)
            window_height=int(window_height)
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
        "text":"Button",
        "command":None,
        "width":"20",
        "heigh":"20",
        "bg":None,
        "fg":None,
        }
    root_window=None    
    x_offsit=0
    y_offsit=0
    def __init__(self,
                window,
                button_text=Button_option["text"],
                button_call_function=Button_option["command"],
                button_width=Button_option["width"],
                button_heigh=Button_option["heigh"],
                button_bg=Button_option["bg"],
                button_fg=Button_option["fg"],
                ):


        self.root_window=window
        self.Button_option["text"]=button_text
        self.Button_option["command"]=button_call_function
        self.Button_option["width"]=button_width
        self.Button_option["heigh"]=button_heigh
        self.Button_option["bg"]=button_bg
        self.Button_option["fg"]=button_fg

        
    def creat_button(self,window=root_window):
       super().__init__(window,self.Button_option)
       
       self.place(x=self.x_offsit,y=self.y_offsit) 
    def button_text(self,text=str()):
        self.Button_option["text"]=text
        self.creat_button(self.root_window)
    def button_bg(self,color=str()):
        self.Button_option["bg"]=color
        self.creat_button(self.root_window)
    def button_fg(self,color=str()):
        self.Button_option["fg"]=color
        self.creat_button(self.root_window)        
    def button_call_fun(self,fun):
        self.Button_option["command"]=fun
        self.creat_button(self.root_window)
    def button_size(self,width=str(),hight=str()):
        self.Button_option["width"]=width
        self.Button_option["hight"]=hight
        self.creat_button(self.root_window)
    def button_pozition(self,x=int(),y=int()):
        self.x_offsit=x
        self.y_offsit=y
        self.creat_button(self.root_window)



class text_box(Entry):
    #textvariable=StringVar()
    text_box_option={

            "relief":SUNKEN,
            "show":None,
            "width":"20",
            "text_bg":None,
            "text_fg":None,
            }
    x_offsit=0
    y_offsit=0

    def creat_text_box(self,window):
        super().__init__(window,self.text_box_option)
        self.place(x=self.x_offsit,y=self.y_offsit) 


    def text_box_relier(self,relier):
        self.text_box_option["relief"]=relier
    def text_box_bg(self,color=str()):
        self.text_box_option["bg"]=color
    def text_box_fg(self,color=str()):
        self.text_box_option["fg"]=color        
    def text_box_size(self,width=str(),hight=str()):
        self.text_box_option["width"]=width
        self.text_box_option["hight"]=hight
    def text_box_pozition(self,x=int(),y=int()):
        self.x_offsit=x
        self.y_offsit=y
    def text_style(self,style=str()):
        self.text_box_option["show"]=style
    def get_text(self):
        return self.get()    


w=window("hellow")
w.creat_window("680","600")
b=button(w)
b.button_text("b1")

b.button_pozition(100,200)

t=text_box()
t.text_box_pozition(200,300)
t.creat_text_box(w)
def call():
    print(t.get_text())
b.button_call_fun(call)

b.button_pozition(10,20)
#b.creat_button(w)


w.mainloop()   

