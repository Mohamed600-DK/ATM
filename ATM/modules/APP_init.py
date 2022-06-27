from App.Initialize_GUI_APP.initialize_base_window import *
from App.Initialize_GUI_APP.initialize_home_window import *
from App.Initialize_GUI_APP.initialize_login_window import *
from App.Initialize_GUI_APP.initialize_message import *
from App.Initialize_GUI_APP.initialize_cash_withdraw_window import *
from App.Initialize_GUI_APP.initialize_balance_inquiry_window import *
from App.Initialize_GUI_APP.initialize_fawry_service_window import *
from App.Initialize_GUI_APP.initialize_password_change_window import *
from modules.Prog_Funs import save_clints_data

def App_initialze():
    initialize_base_window()
    initialize_login_window()
    initialize_home_window()
    initialize_cash_withdraw_window()
    initialize_fawry_service_window()
    initialize_Balance_inquiry_window()
    initialize_Password_change_window()
    initialize_message()

def App_run():
    gv.main_window.run_app()
    save_clints_data()
    print("All data is saved")    