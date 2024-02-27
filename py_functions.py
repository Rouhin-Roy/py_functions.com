'''
Name: Python functions
Author: Rouhin Roy
Last modified on: 26/02/2024
'''
#Note: You can run this file to know the 21 functions present in this file
import os
import pyautogui
import time
list_of_functions = ["create_file(name,extension):","read_file(name,extension):","create_folder(name):","delete_file(name,extension):","delete_folder(name):","delete_all():","create_range_of_files(start,stop):", "create_range_of_folders(start,stop):", "write_file(name,extension):","append_file(name,extension):","delete_range_of_files(start,stop,name,extension):","delete_range_of_folders(start,stop,name):","search_files(name,extension):","create_new_sales_file(day,month,year):","view_sales_file(day,month,year):","write_sales_file(day,month,year):","check_database():","change_password():","add_items_of_sale():","take_picture(file_name):","authorize_user():","take_video(time)","switch_desktop(key)","create_Website(path,name,no_of_files)"] 
def create_file(name ,extension):
    a = open(f"{name}.{extension}","w")
    a.close()
def read_file(name, extension):
    a = open(f"{name}.{extension}","r")
    data = a.readlines()
    b = 0
    for i in data:
        b += 1
        print(f"Line{b}: {i}")
def create_folder(name):
    os.mkdir(f"{name}")
def delete_file(name, extension):
    a = f"{name}.{extension}"
    if a.endswith("database.txt"):  
        print(f"{name}.{extension} is an system file")
    else:
        os.remove(f"{name}.{extension}")
def delete_folder(name):
    os.removedirs(f"{name}")
def delete_all():
    a = os.listdir()
    for i in a:
        if (i.endswith(f"main.py") or (i.endswith("database.txt"))):
           print(f"{i} cannot be removed ")
        else:
            try:
               os.remove(f"{i}")
            except Exception as e:
                try:
                    os.removedirs(f"{i}")
                except Exception as e:
                    print(f"We are sorry for the error")
def create_range_of_files(start , stop, name , extension):
    try:
        for i in range(int(start),int(stop) + 1):
            a = open(f"{name}{i}.{extension}","w")
            a.close()
    except Exception as e:
        print(f"{e} is an invalid input")
def create_range_of_folders(start , stop, name):
    try:
        for i in range(int(start),int(stop) + 1):
            os.mkdir(f"{name}{i}")
    except Exception as e:
        print(f"{e} is an invalid input")
def write_file(name,extension):
    a = open(f"{name}.{extension}","w")
    lines_written = 0
    line_open = 0
    while line_open == 0:
        line = str(input("Enter the line you want to write: "))
        lines_written += 1
        a.write(str(f"{line} \n"))
        try:
            line_open_add_value = int(input("Enter 0 to add more lines(or any other value to stop): "))
        except Exception as e:
            print(f"{e} is an invalid input")
        line_open += line_open_add_value
    print(f"{lines_written} lines were written")
def append_file(name,extension):
    a = open(f"{name}.{extension}","a")
    lines_appended = 0
    line_open = 0
    while line_open == 0:
        line = str(input("Enter the line you want to apppend: "))
        lines_appended += 1
        a.write(str(f"{line} \n"))
        try:
            line_open_add_value = int(input("Enter 0 to add more lines(or any other value to stop): "))
        except Exception as e:
            print(f"{e} is an invalid input")
        line_open += line_open_add_value
    print(f"{lines_appended} lines were appended")
    a.close()
def delete_range_of_files(start,stop,name,extension):
    for i in range(start,stop + 1):
        if os.path.exists(f"{name}{i}.{extension}"):
            os.remove(f"{name}{i}.{extension}")
        else:
            print(f"{name}{i}.{extension} was not found")
    print(f"{stop - start} {name}.{extension} files were deleted")
def delete_range_of_folders(start,stop,name):
    for i in range(start,stop + 1):
        if os.path.exists(f"{name}{i}"):
            os.removedirs(f"{name}{i}")
        else:
            print(f"{name}{i} was not found")
    print(f"{stop - start} folders were deleted")
def search_files(name , extension):
    if os.path.exists(f"{name}.{extension}"):
        print(f"{name}.{extension} is there in this folder")
    else:
        print(f"{name}.{extension} does not exist")
def create_new_sales_file(day,month,year):
  a = 0
  while a == 0:
    if os.path.exists("Buisness_data"):
     if os.path.exists(f"Buisness_data/Sales of {year}"):
      if os.path.exists(f"Buisness_data/Sales of {year}/Sales of {month}"):
        if os.path.exists(f"Buisness_data/Sales of {year}/Sales of {month}/Sales of {day}.txt"):
          print(f"The file now exists")
          a = a + 1
        else:
          new_sales_file = open(f"Buisness_data/Sales of {year}/Sales of {month}/Sales of {day}.txt","w")
          new_sales_file.close()
      else:
        os.mkdir(f"Buisness_data/Sales of {year}/Sales of {month}")
     else:
      os.mkdir(f"Buisness_data/Sales of {year}")
    else:
      os.mkdir("Buisness_data")
def view_sales_file(day,month,year):
  if os.path.exists(f"Buisness_data/Sales of {year}/Sales of {month}/Sales of {day}.txt"):
    sales_file = open(f"Buisness_data/Sales of {year}/Sales of {month}/Sales of {day}.txt","r")
    data_sales_file = sales_file.readlines()
    for line in data_sales_file:
      print(line)
  else:
    print(f"No such file exists")
def write_sales_file(day,month,year):
  if os.path.exists(f"Buisness_data/Sales of {year}/Sales of {month}/Sales of {day}.txt"):
    sales_file = open(f"Buisness_data/Sales of {year}/Sales of {month}/Sales of {day}.txt","w")
    items_data = open("Owner_data/items_data.txt","r")
    items_data_lines = items_data.readlines()
    items_data_list = []
    for i in items_data_lines:
      items_data_list.append(i)
    i_plus = 0
    for i in items_data_list:
      print(f"data{i_plus} = {i}")
      i_plus += 1
    try:
      user_input = 0 
      while user_input < i_plus + 1:
        user_input = int(input("Enter your choice(in integers): "))
        if user_input < i_plus + 1:
          data = items_data_list[user_input]
          item = data.split(":")[0]
          price = int(data.split(":")[1])
          sale_of_item = int(input("Enter the no of times the item was sold: "))
          sales_file.write(f"{sale_of_item} of {item} was sold. Profits = Rupess {price * sale_of_item} \n")
    except Exception as e:
      print(f"{e} is an invalid input")
  else:
    print(f"No such file exists")
def check_database():
  database = open("app_files/database.txt","r")
  lines = database.readlines()
  for line in lines:
    print(line)
def change_password():
  file = open("Owner_data/account_details.txt","w")
  line = file.readlines()
  a = line.split(",")[0]
  b = line.split(",")[2]
  new_password = input("Create a new password: ")
  file.write(f"{a},{new_password},{b}")
def add_items_of_sale():
  file = open("Owner_data/account_details.txt","a")
  try:
    new_item = input("Enter the name of the new item: ")
    new_price = int(input("Enter the price of the item: "))
    file.write(f"{new_item}:{new_price} \n")
  except Exception as e:
    print(f"{e} is an invalid input")
def take_picture():
    # Open the camera application
    pyautogui.press('win')
    pyautogui.write('camera')
    pyautogui.press('enter')
    time.sleep(2)  # Wait for the camera app to open

    # Press the spacebar to capture a picture
    pyautogui.click(x= 1467,y= 524)
    time.sleep(1)  # Wait for the picture to be captured

    # Save the picture (Alt + F, S)
    time.sleep(1)  # Wait for the save dialog to appear

    # Type the specified file name and press Enter
    pyautogui.press('enter')
    pyautogui.hotkey("alt","f4")
def authorize_user():
 import threading
 import os
 import random as r
 import pywhatkit as p
 import time
 google_p = {
    "API" : "czim kazn fbim bihd"
 }
 login_value ={
   "authorization_value" : 0
 }
 current_date = time.strftime("%D")
 current_hour = time.strftime("%H")
 current_minute = time.strftime("%M")
 current_second = time.strftime("%S")
 if os.path.exists("database.txt"):
    file = open("database.txt","r")
    file2 = open("System_cache.txt","w")
    user_data = file.readline()
    details_sent = 0
    loop = 0
    while loop == 0:
     name = input("Enter your name: ")
     user_name = input("Enter your username: ")
     password = input("Enter your password: ")
     if user_name == user_data.split(",")[0] and password == user_data.split(",")[1]:
       print("Authorization succesful")
       file2.write(f"{current_date}: Authorized user {name} used program at {current_hour}:{current_minute}:{current_second}")
       file2.close()
       login_value["authorization_value"] = 1
       break
     else:
       if details_sent == 0:
        print("Wrong Credentials")
        x = user_data.split(",")[1]
        y = user_data.split(",")[0]
        p.send_mail(
          email_sender="programforpython@gmail.com",
          email_receiver=user_data.split(",")[2],
          password=google_p["API"],
          message=f"Your password is {x} and your username is {y}",
          subject="Account Credentials",
        )
        print("An email  has been sent to you please check the following credentials and try to login again")
        details_sent = 1
       else:
         file2.write(f"{current_date}: Unauthorized user {name} used program at {current_hour}:{current_minute}:{current_second}")
         login_value["authorization_value"] = 0
         print("Unauthorised user")
         break
 else:
     answers = ["YES","yes","Yes","yEs","yeS","YEs","YeS","yES"]
     looper_input = input("Do you want to create an account(Type yes to continue or no to stop): ")
     if looper_input in answers:        
       looper_3 = 0
     else:
       looper_3 = 1
       print("Okay an account will not be created")
     if looper_3 == 0: 
      a = input("Create an username: ")
      looper_1 = 0
      while looper_1 < 2:
       print("An OTP will be sent to your gmail account 2 times at maximum.")
       em = input("Enter a valid gmail account: ")
       if "@gmail.com" in em:
        otp_dict = {
          "otp" : "",
          "otp_2" : ""
        }
        def send_mail():
          otp = otp_dict["otp"]
          for i in range(0,6):
            add = str(r.randint(0,9))
            otp = f"{otp}{add}"
            otp_dict["otp_2"] = otp
          p.send_mail(
           email_sender="programforpython@gmail.com",
           password=google_p["API"],
           email_receiver=em,
           subject="OTP",
           message=otp,
         )
        import threading
        my_thread = threading.Thread(target=send_mail)
        my_thread.start()
        print("Sending OTP in a few seconds ")
        time.sleep(4)
        otp_input = input("Enter the OTP: ")
        if otp_input == otp_dict["otp_2"]:
           break
        else:
           print("Try again")
           looper_1 += 1 
       else:
         print("The given email is wrong try again and is missing the @gmail.com argument")
      if looper_1 == 2:
        print("You will be reported to the police soon within 10 minutes")
        print("To resolve the issue immediately send a mail to programforpython@gmail.com with an attached screenshot of the above issue")
      else:
        pass
      looper_2 = 0
      while looper_2 == 0:
       b = input("Create a password: ")
       c = input("Confirm the password: ")
       if b == c:
          file = open(f"database.txt","w")
          file.write(f"{a},{b},{em}")
          file_2 = open("System_cache.txt","w")
          file_2.close()
          break
       else:
          print("Passwords dont match" )
def take_video(time_value: int):
    # Open the camera application
    import time
    pyautogui.press('win')
    pyautogui.write('camera')
    pyautogui.press('enter')
    time.sleep(2)  # Wait for the camera app to open

    # Press the spacebar to capture a picture
    pyautogui.click(x =1466,y= 453)
    time.sleep(1)
    pyautogui.click(x= 1467,y= 524)
    time.sleep(2 + time_value)  # Wait for the picture to be captured

    # Save the picture (Alt + F, S)
    time.sleep(1)  # Wait for the save dialog to appear

    # Type the specified file name and press Enter
    pyautogui.press('enter')
    pyautogui.hotkey("alt","f4")
def switch_desktop(key):
   pyautogui.hotkey("ctrl","win",key)
def create_Website(path : str,name : str,no_of_files : int):
 import pywhatkit as py
 import pyautogui as p
 from time import sleep
 py.search("github") #Search Github
 sleep(2)
 p.click(581,433) #Open the website
 sleep(3)
 p.press("tab",presses=7) #Click on +
 p.press("enter")
 sleep(1)
 p.press("enter") #
 sleep(2)
 p.press("tab",presses=13) #Go to name input box
 p.write(name) #Enters the name
 p.press("tab",presses=4) #Select readme box
 p.press("space")#
 sleep(2)
 p.press("tab",presses=7) #Creates repository                                                                                                                                     
 p.press("space")#
 sleep(5)
 p.click(x = 1104,y = 409) #Click on add files
 p.press("down")
 p.press("enter") # Select Upload files
 sleep(2)
 p.press("tab",presses=23) #Open choose files dialog box
 p.press("space") 
 sleep(2)
 p.click(500,70)
 p.press("backspace")
 p.write(path)
 sleep(2)
 p.press("enter")
 sleep(2)
 p.click(625,178)
 sleep(1)
 p.hotkey("ctrl","a")
 sleep(1)
 p.click(x = 756, y = 567)
 files = no_of_files
 sleep(files  * 4)
 p.press("tab",presses=5)               
 p.press("enter")
 sleep(files * 4) 
 p.press("tab",21) # opens  Settings
 p.press("enter")
 sleep(5)
 p.press("tab",11) #Opens pages
 p.press("enter")
 sleep(3)
 p.press("tab",20) #Selects branch i.e. main
 p.press("enter")
 p.press("down")
 p.press("enter")
 sleep(2)
 p.click(920,730) #clicks on save button
 sleep(60)
 py.send_mail(
  email_sender="programforpython@gmail.com",
  email_receiver="rouhinroy09@gmail.com",
  password="czim kazn fbim bihd",
  message=f"Congrats, your website is deployed at rouhin-roy.github.io/{name} ",
  subject="WEBSITE DEPLOYED"
 )
 sleep(3)
 p.hotkey("alt","f4")
 p.press("win")
 p.press("tab",5)
 p.press("right")
 p.press("enter")
 p.press("down",3)
 p.press("enter")
if __name__ == "__main__":
   lines = 0
   for i in list_of_functions:
      print(i)
      lines += 1
   else:
      print(f"These are the list of functions. There are {lines} functions in total")
else:
   pass
