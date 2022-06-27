from  modules.GUI  import GUI_app 

def init():
    global clints_data,locked_accounts,clint,data
    global check_pass,main_window,messg_font_size,reghatfe_network
    clints_data=list()
    locked_accounts=list()
    clint=dict()
    data=dict()
    check_pass=0    
    messg_font_size=12    
    main_window=GUI_app()
    reghatfe_network=""