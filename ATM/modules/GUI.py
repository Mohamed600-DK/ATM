from tkinter import *

from tkinter.font import Font

#all uints are in pix unit

class GUI_app(Tk,Button,Entry,Label,Font,Frame,Toplevel):
###################################
################### Variables_Section #####################################    
    root_window=None

    widged_list=dict()
    window_list=dict()
    options=dict()

    window_options={
        "window_name":"main window",
        "title":"main window",
        "width":None,
        "height":None,
        "shift_x":None,
        "shift_y":None,
        "gemotry_value":None
    }
  
    Button_options={
        "parent":root_window,
        "widges_name":"Button",
        "text":"Button",
        "call_function":None,
        "width":20,#its unit is letter
        "height":5,
        "bg":None,
        "fg":None,
        "x_location":20,
        "y_location":20,
        "font":None 
    }
    
    entry_options={
        "parent":"root_window",
        "widges_name":"TextBox",
        "relief":SUNKEN,
        "text_style":None,
        "width":10,#its unit is charater
        "text_bg":None,
        "text_fg":None,
        "bg":None,
        "fg":None,
        "bd":None,
        "x_location":30,#its unit is Pix
        "y_location":30,#its unit is Pix
        "text_valu":"",
        "text_lenth":10,
        "font":None
        }
    
    label_options={
        "parent":root_window,
        "widges_name":"Label",
        "text":"Label",
        "relief":SUNKEN,
        "width":"auto",#its unit is charater
        "height":"auto",#its unit is Lins 
        "bg":None,
        "fg":None,
        "bd":None,
        "x_location":30,#its unit is Pix
        "y_location":30,#its unit is Pix
        "justify":LEFT,
        "font":None
        }

    frame_options={
            "parent":root_window,
            "Frame_name":"frame",
            "bg":None,
            "bd":None,
            "height":20,
            "width":20,
            "padx":None,
            "pady":None,
            "relief":SUNKEN,
            "takefocus":0,
            "x_location":20,
            "y_location":20,
            "font":None
        }    
 
    top_level_options={
    "parent":root_window,
    "name":"Top_level",
    "title":"Toplevel",
    "bg":None,
    "fg" :None,
    "bd" :None,
    "height" :180,
    "width" :180,
    "font" :None,
    "x_location":30,
    "y_location":30,
    "gemotry_value":None
}
    
  
######################################################################
################### Window_Section #####################################
    def __init__(self):
        pass
        
      
    def enable_widget(self,widged_name):
        obj=self.widged_list[widged_name]

        x_location= self.options[widged_name]["x_location"]
        y_location=self.options[widged_name]["y_location"]
        obj.place(x=x_location,y=y_location)
      
   
    def disable_widget(self,widged_name):
        obj=self.widged_list[str(widged_name)]
        obj.place_forget()

    def enable_window(self,window_name,enable_always_top=False):
            window_obj=self.window_list[window_name]
            gemotry=self.options[window_name]["gemotry_value"]
            title=self.options[window_name]["title"]           
            self.root_window.wm_manage(window_obj)
            window_obj.title(title)
            window_obj.geometry(gemotry)
            if(enable_always_top==True):
                window_obj.wm_attributes("-topmost",enable_always_top)

    def disable_window(self,window_name):
        window_obj=self.window_list[window_name]
        self.root_window.forget(window_obj)
        #self.root_window.wm_attributes("-toolwindo")
   
   
    def font_init(self,font_size=10,font_family="Times",font_weight="normal",font_slant="roman",font_underline=0,font_overstrike=0):
        font=Font(family=font_family,size=font_size,weight=font_weight,slant=font_slant,underline=font_underline,overstrike=font_overstrike)
        return font

             
   
   
######################################################################
################### Window_Section #####################################
   




    def creat_toplevelwindow(self,
                            name,
                            parent=None,
                            title=None,
                            bg=None,
                            fg=None,
                            bd=None,
                            height=None,
                            width=None, 
                            font=None,
                            x_location=None,
                            y_location=None):

        top_level_options=self.top_level_options.copy()
        

        if(parent==None):parent=self.top_level_options["parent"]
        else:top_level_options["parent"]=parent
        
        
        if(name==None):name=self.top_level_options["name"] 
        else:top_level_options["name"]=name
        
        if(title==None):title=self.top_level_options["title"]
        else:top_level_options["title"]=title
        
        if(width==None):width=self.top_level_options["width"]  
        else:top_level_options["width"]=width
        
        if(height==None):height=self.top_level_options["height"]
        else:top_level_options["height"]=height
        
        if(bg==None):bg=self.top_level_options["bg"]
        else:top_level_options["bg"]=bg
        
        if(fg==None):fg=self.top_level_options["fg"]
        else:top_level_options["fg"]=fg
        
        if(bd==None):bd=self.top_level_options["bd"]
        else:top_level_options["bd"]=bd
        
        if(font==None):font=self.top_level_options["font"]
        else:top_level_options["font"]=font
        
        if(x_location==None):x_location=self.top_level_options["x_location"]  
        else:top_level_options["x_location"]=x_location
        
        if(y_location==None):y_location=self.top_level_options["y_location"]  
        else:top_level_options["y_location"]=y_location
        



        toplevel_obj=Toplevel(parent,font=font)
        
        self.options[name]=top_level_options.copy()
        self.window_list[name]=toplevel_obj

        self.toplevelwindow_title(name,title)
        self.toplevelwindow_bg(name,bg)  
        self.toplevelwindow_fg(name,fg) 
        self.toplevelwindow_fg(name,bd)   
        self.toplevelwindow_size(name,width,height,x_location,y_location)  
        
       
        
       
        return toplevel_obj



    def toplevelwindow_title(self,name,title):
        
        toplevel_obj=self.window_list[name]
        self.options[name]["title"]=title
        toplevel_obj.title(title)


    def toplevelwindow_bg(self,name,bg):
        
        toplevel_obj=self.window_list[name]
        self.options[name]["bg"]=bg
        toplevel_obj.config(bg=bg)

    def toplevelwindow_fg(self,name,fg):
        
        toplevel_obj=self.window_list[name]
        self.options[name]["fg"]=fg
        toplevel_obj.config(bg=fg)

    def toplevelwindow_fg(self,name,bd):
        toplevel_obj=self.window_list[name]
        self.options[name]["bd"]=bd
        toplevel_obj.config(bd=bd)


    def toplevelwindow_size(self,name,width,height,x_location,y_location):
        toplevel_obj=self.window_list[name]
        self.options[name]["width"]=width
        self.options[name]["height"]=height
        toplevel_obj.wm_attributes("-topmost",True)
        screen_width_x = self.root_window.winfo_screenwidth()
        screen_height_y = self.root_window.winfo_screenheight()
        window_width_x=width
        window_height_y=height
        shift_x=int((screen_width_x-window_width_x)/2)
        shift_y=int((screen_height_y-window_height_y)/2)
        gemotry_value=str(window_width_x)+"x"+str(window_height_y)+"+"+str(shift_x)+"+"+str(shift_y)
        toplevel_obj.geometry(gemotry_value)
        self.options[name]["gemotry_value"]=gemotry_value



  
    def creat_window(self,window_name="main_window",title="main window",width=None,height=None):
        
        window=Tk()
        
        
        if( self.root_window == None):
           
            self.root_window=window
           # print("the root window is creaded")
        
        self.root_window.title(title)
        if (width !=None and height!=None ):
            width=int(width)
            height=int(height)
            screen_width_x = self.root_window.winfo_screenwidth()
            screen_height_y = self.root_window.winfo_screenheight()
            window_width_x=width
            window_height_y=height
            shift_x=int((screen_width_x-window_width_x)/2)
            shift_y=int((screen_height_y-window_height_y)/2)
            gemotry_value=str(window_width_x)+"x"+str(window_height_y)+"+"+str(shift_x)+"+"+str(shift_y)
            self.root_window.geometry(gemotry_value)
            self.window_options["title"]=title
            self.window_options["width"]=window_width_x
            self.window_options["height"]=window_height_y
            self.window_options["shift_x"]=shift_x
            self.window_options["shift_y"]=shift_y
            self.window_options["gemotry_value"]=gemotry_value


        elif((width ==None and height==None )):
            window.wm_attributes("-fullscreen","True")
            #window.wm_attributes("-topmost","True")
            window_width_x = window.winfo_screenwidth()
            window_height_y = window.winfo_screenheight()
            self.window_options["title"]=title
            self.window_options["width"]=window_width_x
            self.window_options["height"]=window_height_y
            self.window_options["shift_x"]=0
            self.window_options["shift_y"]=0
            geometry_value=str(window_width_x)+"x"+str(window_height_y)+"+"+str(0)+"+"+str(0)
            self.window_options["geometry_value"]=geometry_value

        
        self.options[window_name]=self.window_options.copy()
        self.window_list[window_name]=window
        
        return self.window_options["width"],self.window_options["height"],window
           
        
    def run_app(self):
     self.root_window.mainloop()    

    def exit_app(self):

        self.root_window.quit()
######################################################################
################### BUTTON_Section #####################################







    
    def creat_button(self,
                    button_name,
                    parent=None,
                    text=None,
                    call_function=None,
                    width=None,
                    heigh=None,
                    bg=None,
                    fg=None,
                    x_location=None,
                    y_location=None,
                    font=None
                     ):

        

        Button_options=self.Button_options.copy()

        if(font==None):

            font=self.font_init(font_size=24)
        

        if(parent==None):parent=Button_options["parent"]
        else:Button_options["parent"]=parent

        if(text==None):text=Button_options["text"]
        else:Button_options["text"]=text

        if(call_function==None):call_function=Button_options["call_function"]
        else:Button_options["call_function"]=call_function

        if(width==None):width=Button_options["width"]  
        else:Button_options["width"]=width

        if(heigh==None):heigh=Button_options["height"]
        else:Button_options["height"]=heigh

        if(bg==None):bg=Button_options["bg"]
        else:Button_options["bg"]=bg

        if(fg==None):fg=Button_options["fg"]
        else:Button_options["fg"]=fg

        if(x_location==None):x_location=Button_options["x_location"]  
        else:Button_options["x_location"]=x_location

        if(y_location==None):y_location=Button_options["y_location"]  
        else:Button_options["y_location"]=y_location
        
        Button_obj=Button(parent,font=font)   
        self.widged_list[button_name]=Button_obj     
        self.options[button_name]=Button_options.copy()     
        self.button_text(button_name,text)    
        self.button_bg(button_name,bg)  
        self.button_fg(button_name,fg)  
        self.button_call_fun(button_name,call_function)  
        self.button_size(button_name,width,heigh) 
        if(x_location !=None and y_location != None): 
            self.button_pozition(button_name,x_location,y_location)  

        return Button_obj
    
    def button_text(self,button_name,text=str()):

        Button_obj=self.widged_list[button_name]
        self.options[button_name]["text"]=text
        Button_obj.config(text=text)
        self.button_size(button_name,"auto","auto")

    def button_bg(self,button_name,color=str()):

        Button_obj=self.widged_list[button_name]
        self.options[button_name]["bg"]=color
        self.Button_options["bg"]=color
        Button_obj.config(bg=color)
    def button_fg(self,button_name,color=str()):
        
        Button_obj=self.widged_list[button_name]
        self.options[button_name]["fg"]=color
        Button_obj.config(fg=color)
       
    def button_call_fun(self,button_name,*arg):
        
        Button_obj=self.widged_list[button_name]
        try:
            if(None not in  arg and len(arg)!=0):
                if(arg[0]==[]):
                    def call_fun():
                        Button_obj.config(command=None)
                        print("No arguments")   
                elif(len(arg)>0):
                    arg=list(*arg)  
                    fun=arg.pop(0)
                    def call_fun():
                        fun(*arg)
                
                self.options[button_name]["call_function"]=call_fun
                Button_obj.config(command=call_fun)
            else:
                Button_obj.config(command=[])
        except: 
                fun=list(arg).pop(0) 
                self.options[button_name]["call_function"]=fun
                Button_obj.config(command=fun)


    def button_size(self,button_name,width,height):
        Button_obj=self.widged_list[button_name]
        if (width=="auto" or width==None):
            width=len(self.options[button_name]["text"]+"00000")
            self.options[button_name]["width"]="auto_Calulat=%s"%width
            Button_obj.config(width=width)
        else:
            width=int(width)
            self.options[button_name]["width"]=width
            Button_obj.config(width=width)
         
        
        if (height=="auto" or height==None):
            height=self.options[button_name]["height"]
            Button_obj.config(height=height)
        else:    
            height=int(height)
            self.options[button_name]["height"]=height
            Button_obj.config(height=height)
        
        


    def button_pozition(self,button_name,x_location=int(),y_location=int()):
        x_location =int(x_location)
        y_location =int(y_location)
        Button_obj=self.widged_list[button_name]
        self.options[button_name]["x_location"]=x_location 
        self.options[button_name]["y_location"]=y_location 
        Button_obj.place(x=x_location,y=y_location) 
######################################################################
################### Entry_Section #####################################
 



    def creat_text_box(self,
                    textbox_name,
                    parent=None,
                    relief=None,
                    text_style=None,
                    width=None,
                    text_bg=None,
                    text_fg=None,
                    bg=None,
                    fg=None,
                    bd=None,
                    font=None,
                    x_location=None,
                    y_location=None,
                    check_text_lenth=False ,  
                    text_lenth=None                   
                     ):

        entry_options=self.entry_options.copy()

        if(parent==None):parent=entry_options["parent"]
        else:entry_options["parent"]=parent
        if(relief==None):relief=entry_options["relief"]
        else:entry_options["relief"]=relief
        if(text_style==None):text_style=entry_options["text_style"]
        else:entry_options["text_style"]=text_style
        if(text_bg==None):text_bg=entry_options["text_bg"]
        else:entry_options["text_bg"]=text_bg
        if(text_fg==None):text_fg=entry_options["text_fg"] 
        else:entry_options["text_fg"]=text_fg
        if(width==None):width=entry_options["width"]
        else:entry_options["width"]=width
        if(bg==None):bg=entry_options["bg"]
        else:entry_options["bg"]=bg
        if(fg==None):fg=entry_options["fg"]
        else:entry_options["fg"]=fg
        if(bd==None):bd=entry_options["bd"] 
        else:entry_options["bd"]=bd
        if(x_location==None):x_location=entry_options["x_location"]
        else:entry_options["x_location"]=x_location
        if(y_location==None):y_location=entry_options["y_location"]
        else:entry_options["y_location"]=y_location
        if (font==None):font=self.font_init(font_size=24)
        else:entry_options["y_location"]=y_location
        
        if(text_lenth==None):text_lenth=entry_options["text_lenth"]
        else:entry_options["text_lenth"]=text_lenth
        
        textbox_obj=Entry(parent,font=font)
        entry_options["text_valu"] =StringVar()

        self.options[textbox_name]=entry_options.copy()
        self.widged_list[textbox_name]=textbox_obj
        if(check_text_lenth==True):
            call_check_fun=parent.register(self.textbox_check_text)
            textbox_obj.config(validate="key",validatecommand=(call_check_fun,text_lenth,"%P"))
        
        self.textbox_relier(textbox_name,relief)
        self.text_style(textbox_name,text_style)
        self.textbox_size(textbox_name,width)
        self.textbox_bg(textbox_name,bg)
        self.textbox_fg(textbox_name,fg)
        self.textbox_boardwidth(textbox_name,bd)
        if(x_location !=None and y_location != None):
            self.textbox_pozition(textbox_name,x_location,y_location)



        return textbox_obj

    def textbox_check_text(self,text_lenth,text):
        #check if the entered text out of the range of the entry width
        #check if the entered number is digit or it is string
        text_lenth=int(text_lenth)
        if(len(text)==0 ):
            return True
            
        elif(len(text)<=text_lenth and text.isdigit()==True): 
            return True
        else:
            return False
    
    def textbox_relier(self,textbox_name,relief):

        textbox_obj=self.widged_list[textbox_name]
        self.options[textbox_name]["relief"]=relief
        textbox_obj.config(relief=relief)

    def text_style(self,textbox_name,style=str()):

        textbox_obj=self.widged_list[textbox_name]
        self.options[textbox_name]["text_style"]=style
        textbox_obj.config(show=style)      

    def textbox_size(self,textbox_name,width):
        width=int(width)
        textbox_obj=self.widged_list[textbox_name]
        self.options[textbox_name]["width"]=width

        textbox_obj.config(width=width)

    def textbox_bg(self,textbox_name,color=str()):

        textbox_obj=self.widged_list[textbox_name]
        self.options[textbox_name]["text_bg"]=color
        textbox_obj.config(bg=color)
     

    def textbox_fg(self,textbox_name,color=str()):

        textbox_obj=self.widged_list[textbox_name]
        self.options[textbox_name]["fg"]=color 
        textbox_obj.config(fg=color)       

    def textbox_boardwidth(self,textbox_name,width=str()):

        textbox_obj=self.widged_list[textbox_name]
        self.options[textbox_name]["bd"]=width
        textbox_obj.config(bd=width)   


    def textbox_pozition(self,textbox_name,x_location=int(),y_location=int()):
        x_location =int(x_location)
        y_location =int(y_location)
        textbox_obj=self.widged_list[textbox_name]
        self.options[textbox_name]["x_location"]=x_location
        self.options[textbox_name]["y_location"] =y_location
        
        textbox_obj.place(x=x_location,y=y_location)



    def delete_textbox(self,textbox_name):
        textbox_obj=self.widged_list[textbox_name]
        text=textbox_obj.get() 
        textbox_obj.delete(0,len(text))
        


    def get_text(self,textbox_name):
        
        textbox_obj=self.widged_list[textbox_name]
        text=textbox_obj.get() 
        textbox_obj.delete(0,len(text))
        return  text   

######################################################################
################### Label_Section #####################################


    

    def creat_label(self,
                Label_name,
                parent=None,
                Label_text=None,
                relief=None,
                width=None,
                height=None,
                bg=None,
                fg=None,
                bd=None,
                x_location=None,
                y_location=None,
                justify=None,
                font_text=None
                    ):


        label_options=dict()
        label_options=self.label_options.copy()

        if(parent==None):parent=label_options["parent"]
        else:label_options["parent"]=parent

        if(Label_text==None):Label_text=label_options["text"]
        else: label_options["text"]=Label_text

        if(relief==None):relief=label_options["relief"]
        else: label_options["relief"]=relief

        if(width==None):width=label_options["width"]
        else: label_options["width"]=width

        if(height==None):height=label_options["height"] 
        else: label_options["height"]=height

        if(bg==None):bg=label_options["bg"]
        else: label_options["bg"]=bg

        if(fg==None):fg=label_options["fg"]
        else:label_options["fg"]=fg

        if(bd==None):bd=label_options["bd"] 
        else:label_options["bd"]=bd

        if(x_location==None):x_location=label_options["x_location"]
        else:label_options["x_location"]=x_location

        if(y_location==None):y_location=label_options["y_location"]
        else:label_options["y_location"]=y_location

        if(justify==None):justify=label_options["justify"]
        else:label_options["justify"]=justify

        if(font_text==None):font_text=self.font_init(font_size=24);label_options["font"]=font_text
        else:label_options["font"]=font_text

        font=font_text





        label_obj=Label(parent,font=font)
        label_obj.config(justify=justify)
        self.options[Label_name]=label_options.copy()
        self.widged_list[Label_name]=label_obj

        self.label_relier(Label_name,relief)
        self.label_text(Label_name,Label_text)
        self.label_size(Label_name,width,height)
        self.label_bg(Label_name,bg)
        self.label_fg(Label_name,fg)
        self.label_boardwidth(Label_name,bd)
        
        if(x_location !=None and y_location != None):
            self.label_pozition(Label_name,x_location,y_location)

        


        return label_obj



    def label_relier(self,Label_name,relief):

        label_obj=self.widged_list[Label_name]
        self.options[Label_name]["relief"]=relief
        label_obj.config(relief=relief)

    def label_text(self,Label_name,Label_text):

        label_obj=self.widged_list[Label_name]
        self.options[Label_name]["text"]=Label_text
        label_obj.config(text=Label_text)        

    def label_size(self,Label_name,width,height):

      
        label_obj=self.widged_list[Label_name]
        if (width=="auto" or width==None):

            self.options[Label_name]["width"]="Auto_calculat"
            label_obj.config(width=None)

        else:
            width=int(width)
            self.options[Label_name]["width"]=width
            label_obj.config(width=width)
        
        
        if (height=="auto" or height==None):

            self.options[Label_name]["height"]="Auto_calculat"
            label_obj.config(height=None)

        else:
            height=int(height)
            self.options[Label_name]["height"]=height
            label_obj.config(height=height)

    def label_bg(self,Label_name,bg):

        label_obj=self.widged_list[Label_name]
        self.options[Label_name]["bg"]=bg
        label_obj.config(bg=bg)
    
    def label_fg(self,Label_name,fg):
        
        label_obj=self.widged_list[Label_name]
        self.options[Label_name]["fg"]=fg
        label_obj.config(fg=fg)
             
    def label_boardwidth(self,Label_name,bd):
        
        label_obj=self.widged_list[Label_name]
        self.options[Label_name]["bd"]=bd
        label_obj.config(bd=bd)
    
    def label_pozition(self,Label_name,x_location,y_location):
        
        x_location =int(x_location)
        y_location =int(y_location)
        label_obj=self.widged_list[Label_name]
        self.options[Label_name]["x_location"]=x_location
        self.options[Label_name]["y_location"] =y_location
        
        label_obj.place(x=x_location,y=y_location)
######################################################################
################### fram_Section #####################################


    def creat_frame(self,
                Frame_name,
                parent=None,
                relief=None,
                width=None,
                height=None,
                bg=None,
                bd=None,
                padx=None,
                pady=None,
                x_location=None,
                y_location=None
                    ):
        
        frame_options=self.frame_options.copy()

        if(parent==None):parent=frame_options["parent"]
        else:parent=frame_options["parent"]

        if(relief==None):relief=frame_options["relief"]
        else:relief=frame_options["relief"]

        if(width==None):width=frame_options["width"]
        else:width=frame_options["width"]

        if(height==None):height=frame_options["height"] 
        else:height=frame_options["height"]

        if(bg==None):bg=frame_options["bg"]
        else:frame_options["bg"]=bg

        if(bd==None):bd=frame_options["bd"]
        else:bd=frame_options["bd"]

        if(padx==None):padx=frame_options["padx"] 
        else:padx=frame_options["padx"]

        if(pady==None):pady=frame_options["pady"]
        else:pady=frame_options["pady"]

        if(x_location==None):x_location=frame_options["x_location"]
        else:x_location=frame_options["x_location"]

        if(y_location==None):y_location=frame_options["y_location"]
        else:y_location=frame_options["y_location"]

        
        frame_obj=Frame(parent)

        self.options[Frame_name]=frame_options.copy()
        self.widged_list[Frame_name]=frame_obj
       
       
        self.frame_relier(Frame_name,relief)
        self.frame_size(Frame_name,width,height)
        self.frame_bg(Frame_name,bg)
        self.frame_boardwidth(Frame_name,bd)
        self.frame_padx(Frame_name,padx)
        self.frame_pady(Frame_name,pady)
        if(x_location !=None and y_location != None):
            self.frame_pozition(Frame_name,x_location,x_location)
        
        return frame_obj

        
    def frame_relier(self,frame_name,relief):

        frame_obj=self.widged_list[frame_name]
        self.options[frame_name]["relief"]=relief
        frame_obj.config(relief=relief)

    def frame_size(self,frame_name,width,height):

        width=int(width)
        height=int(height)
        frame_obj=self.widged_list[frame_name]
        self.options[frame_name]["width"]=width
        frame_obj.config(width=width)    
        self.options[frame_name]["height"]=height
        frame_obj.config(height=height)


    def frame_bg(self,frame_name,bg):

        frame_obj=self.widged_list[frame_name]
        self.options[frame_name]["bg"]=bg
        frame_obj.config(bg=bg)
    
             
    def frame_boardwidth(self,frame_name,bd):
        
        frame_obj=self.widged_list[frame_name]
        self.options[frame_name]["bd"]=bd
        frame_obj.config(bd=bd)

    def frame_padx(self,frame_name,padx):
        
        frame_obj=self.widged_list[frame_name]
        self.options[frame_name]["padx"]=padx
        frame_obj.config(padx=padx)
   
    def frame_pady(self,frame_name,pady):
        
        frame_obj=self.widged_list[frame_name]
        self.options[frame_name]["pady"]=pady
        frame_obj.config(padx=pady)
    
    def frame_pozition(self,frame_name,x_location,y_location):
        
        x_location =int(x_location)
        y_location =int(y_location)
        frame_obj=self.widged_list[frame_name]
        self.options[frame_name]["x_location"]=x_location
        self.options[frame_name]["y_location"] =y_location
        
        frame_obj.place(x=x_location,y=y_location)

##################################################################################################################
class masg(GUI_app):
    font_text=""
    root_window=""

    masg_option=dict(
        name="masg",
        parent=root_window,
        masg="masg",
        title="Massage",
        bg="red",
        fg=None,
        bd=None,
        height=150,
        width=260, 
        font=None,
        x_location=None,
        y_location=None
    )

    def __init__(self,
                name,
                parent_obj,
                parent_class,
                masg=None,
                title=None,
                bg=None,
                fg=None,
                bd=None,
                height=None,
                width=None, 
                font=None,
                x_location=None,
                y_location=None):

        
        
        

        parent_class.top_level_options["parent"]=parent_obj
        parent_class.top_level_options["name"]=masg
        parent_class.top_level_options["title"]=title
        parent_class.top_level_options["bg"]=bg
        parent_class.top_level_options["fg"]=fg
        parent_class.top_level_options["bd"]=bd
        parent_class.top_level_options["height"]=height
        parent_class.top_level_options["width"]=width
        parent_class.top_level_options["font"]=font
        parent_class.top_level_options["x_location"]=x_location
        parent_class.top_level_options["y_location"]=y_location
        self.root_window=parent_class.creat_toplevelwindow(name="masg",title="Massage",width=260, height=150,x_location=300,y_location=300,bg="red")
        #GUI_app().disable_window("masg")
        self.font_text=GUI_app().font_init( font_size=10)
        self.masg_label()
        self.masg_button()
    def masg_label(self):
        
        GUI_app().label_options["parent"]=self.root_window
        GUI_app().label_options["x_location"]=12
        GUI_app().label_options["y_location"]=5
        GUI_app().label_options["width"]="auto"
        GUI_app().label_options["height"]="auto"
        GUI_app().label_options["justify"]=CENTER
        obj_label=GUI_app().creat_label("login_masg_label",font_text=self.font_text,bg="blue")
        obj_label.pack(side="top") 
    def masg_button(self):
        
        GUI_app().Button_options["parent"]=self.root_window
        GUI_app().Button_options["text"]="ok"
        GUI_app().Button_options["call_function"]=[GUI_app().disable_window,"login_masg"]
        GUI_app().Button_options["width"]="auto"
        GUI_app().Button_options["height"]=1
        GUI_app().Button_options["x_location"]=100
        GUI_app().Button_options["y_location"]=110
        obj_button=GUI_app().creat_button(button_name="login_masg_button",font=self.font_text)
        obj_button.pack(side="bottom",padx=3)    

##################################################################################################################
##################################################################################################################
##################################################################################################################
"""
main_window=GUI_app()

screan_x,screan_y,base_window=main_window.creat_window(window_name="main_window")
t=masg(name="m",parent_class=main_window,masg="hellow",x_location=screan_x/2,y_location=screan_y/2,parent_obj=base_window)

 
 

def switing_frame(disable_frame,enable_frame):
    main_window.disable_widget(disable_frame)
    main_window.enable_widget(enable_frame)        
###########################################
main_window=GUI_app()

screan_x,screan_y,base_window=main_window.creat_window(window_name="main_window")

main_window.frame_options["parent"]=base_window
main_window.frame_options["x_location"]=0
main_window.frame_options["y_location"]=0
main_window.frame_options["width"]=screan_x
main_window.frame_options["height"]=screan_y
main_window.frame_options["relief"]=RIDGE
main_window.frame_options["bd"]=20

#option_choise=main_window.creat_frame("option_choise",bg="blue")
####################################################################################################################################################################
main_window.creat_frame("cash_withdraw_frame",base_window,bg="yellow")
#main_window.disable_widget("cash_withdraw_frame") 
####################################################################################################################################################################
main_window.creat_frame("f_Balance_Inquiry",base_window,bg="yellow")
main_window.disable_widget("f_Balance_Inquiry") 
####################################################################################################################################################################
main_window.creat_frame("f_Password_Change",base_window,bg="yellow")
main_window.disable_widget("f_Password_Change") 
####################################################################################################################################################################
main_window.creat_frame("f_Fawry_Service",base_window,bg="yellow")
main_window.disable_widget("f_Fawry_Service") 
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
    main_window.Button_options["text"]="ENTERENTERENTERENTER"
    main_window.Button_options["call_function"]=None
    main_window.Button_options["width"]="auto"
    main_window.Button_options["height"]=button_height
    main_window.Button_options["x_location"]=button_x_location
    main_window.Button_options["y_location"]=button_y_location
    main_window.creat_button("cash_withdraw_button")
    
def cash_withdraw_label():

    main_window.label_options["parent"]= main_window.widged_list["cash_withdraw_frame"]
    main_window.label_options["text"]="desired amount to withdraw:"
    main_window.label_options["width"]="auto"
    main_window.label_options["x_location"]=230
    main_window.label_options["y_location"]=main_window.options["cash_withdraw_textbox"]["y_location"]
    main_window.creat_label("cash_withdraw_label")

def back(curren_frame):
    frame_obj=main_window.widged_list[curren_frame]
    main_window.creat_button("back",frame_obj,"Back",[switing_frame,curren_frame,"option_choise"])
    button_width=15
    button_height=2
    width_px=button_width*8+120
    height_px=button_height*8+130
    x_location=(screan_x-width_px)/2
    y_location=(screan_y)-(height_px)
    main_window.button_size("back",width="auto",height=button_height)
    main_window.button_pozition("back",x_location=x_location,y_location=y_location)



####################################################################################################################################################################
cash_withdraw_textbox()
cash_withdraw_button()
cash_withdraw_label()
print(main_window.options["cash_withdraw_button"]["height"])
print(main_window.options["cash_withdraw_button"]["width"])


####################################################################################################################################################################
main_window.run_app()
 """