strg="460x530"

#function to store my string in list
def string_list(string=str()):
    #list of characters which must deleted form my string
    remv_list=("'","["," ","{","\n","(",")")
    #convert the string to list
    conv_list=list()
    str_val=str()
    int_val=str()
    #print("string ','count = ",string.count(","))
    for count in string:
        
        if(count in remv_list):
            
            continue
        else:
            print(count,"\n")
            if(count ==','or count ==']' or count =='}' or count == "x" ):
                
                print(str_val,"\n")
                if(str_val.isdigit()):
                    
                    conv_list.append(int(str_val))
                else:
                    conv_list.append(str_val)
                str_val=""                
            else:
                str_val=str_val+count
                continue

    return conv_list       




print(string_list(strg))