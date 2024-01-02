import logging
logging.basicConfig(filename = "error.log" , level = logging.ERROR)
try:
    10/0
except ZeroDivisionError as e:
    logging.error("I am trying to handle a zerodivision error {}".format(e) )


import logging
logging.basicConfig(filename = "error.log" , level = logging.ERROR)
try:
    10/0
except FileNotFoundError as e:
    logginng.error("I am handling FileNotFoundError {}".format(e) )
except AttributeError as e:
    
    logging.error("I am handling AttributeError {}".format(e) )
except ZeroDivisionError as e:
    logging.error("I am trying to handle a zerodivision error {}".format(e) )


try:
    with open("test11.txt" , 'w') as f:
        f.write("this is my dfatygjgfyhyygta to file")
except FileNotFoundError as e:
    logginng.error("I am handluyikyuhgjghjing FileNotFoundError {}".format(e) )
finally:
    f.close()