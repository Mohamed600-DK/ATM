import modules.Global_variable as gv

####################################################################################################################################################################
def switing_frame(disable_frame,enable_frame):
 
    try:
        try:
            gv.main_window.disable_widget(disable_frame)
        except:
            gv.main_window.disable_window(disable_frame)
        try:    
            gv.main_window.enable_widget(enable_frame)    
        except:
            gv.main_window.enable_window(enable_frame)       
    except:
        print("Frame ",disable_frame ,"or",enable_frame, "not fond")
####################################################################################################################################################################
def back(curren_frame,privise_frame=None):
    screan_x=gv.main_window.options[curren_frame]["width"]
    screan_y=gv.main_window.options[curren_frame]["height"]
    frame_obj=gv.main_window.widged_list[curren_frame]
    
    if (privise_frame ==None ):
        frame_parint_obj=gv.main_window.options[curren_frame]["parent"]
        frame_parint=None
        if(frame_parint==None):
            for frame_parint_name in gv.main_window.widged_list:
                if gv.main_window.widged_list[frame_parint_name]==frame_parint_obj:
                    frame_parint=frame_parint_name
                    break 
        if(frame_parint==None):
            for frame_parint_name in gv.main_window.window_list:
                if gv.main_window.window_list[frame_parint_name]==frame_parint_obj:
                    frame_parint=frame_parint_name
                    break     
                
        gv.main_window.Button_options["call_function"]=[switing_frame,curren_frame,frame_parint]

    else:
         gv.main_window.Button_options["call_function"]=[switing_frame,curren_frame,privise_frame]
    
    gv.main_window.creat_button("back",frame_obj,"Back")
    button_width=15
    button_height=2
    width_px=button_width*8+120
    height_px=button_height*8+130
    x_location=(screan_x-width_px)/2
    y_location=(screan_y)-(height_px)
    gv.main_window.button_size("back",width=button_width,height=button_height)
    gv.main_window.button_pozition("back",x_location=x_location,y_location=y_location)
###################################################################################################################################################################
def title(parint,title_text="hellow"):
    screan_x=gv.main_window.options[parint]["width"]
    x_location=(screan_x-len(title_text)*15)/2
    y_location=0
    try: 
        gv.main_window.label_options["parent"]= gv.main_window.window_list[parint]
    except:
        gv.main_window.label_options["parent"]= gv.main_window.widged_list[parint]
        
    gv.main_window.label_options["text"]=title_text
    gv.main_window.label_options["width"]="auto"
    gv.main_window.label_options["height"]="auto"
    gv.main_window.label_options["x_location"]=x_location
    gv.main_window.label_options["y_location"]=y_location
    gv.main_window.creat_label("title")   
     
  