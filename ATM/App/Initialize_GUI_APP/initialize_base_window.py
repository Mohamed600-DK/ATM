import modules.Global_variable as gv
from App.GUI_APP.Base_window import *
from modules.Prog_Funs import save_clints_data,load_clints_data





def initialize_base_window():
    gv.init()
    load_clints_data()
    base_window()
   
def run_app():
 
    gv.main_window.run_app()
    save_clints_data()
    print("All data is saved")    