# # from tkinter import *


# # # Create a root window
# # root = Tk()
# # root.configure(bg='black')
# # root.geometry("500x500")

# # # Create a StringVar to store the user input
# # name = StringVar()

# # # Create a Label widget to display the user input
# # l = Label(root, textvariable=name,fg='white', bg='black')
# # l.pack()


# # def update():
# #     input_data = input("You- ")
# #     text = input_data
# #     user_input = text
# #     animate_text(user_input,100)
# #     # Schedule the update function to run again after 1 second
# #     # root.after(1000, update)
# # def animate_text(text, delta):
# #     # Get the current text of the Label widget
# #     current_text = name.get()
# #     # Check if there are more characters to add
# #     if len(current_text) < len(text):
# #         # Add one more character to the current text
# #         current_text += text[len(current_text)]
# #         # Update the text of the Label widget
# #         name.set(current_text)
# #         # Schedule the animate_text function to run again after delta milliseconds
# #         root.after(delta, animate_text, text, delta)
# # # Define a function that will get the user input fro

# # # Run the update function for the first time
# # update()

# # # Start the main loop
# # root.mainloop()

# second.py
import requests
import threading



from tkinter import *

# import requests
# url = "https://http://127.0.0.1:5000/data"
# text = requests.get(url).text


# from . import recognais
import NLP


# from . import cam


# Create a root window
root = Tk()
# sp = recognais.speak

# Change the size of the app
root.geometry("800x600")################################

# Change the background color of the app
root.config(background="black")################################

# Create a StringVar to store the user input
name = StringVar()
# response = requests.post('http://localhost:5000/send_data', data={'input': 'some data'})
# print(response.text)





# response = requests.get('http://localhost:5000/send_get_data')
# print(response.text)


# Create a Label widget to display the user input
l = Label(root, textvariable=name, font=("Times New Roman", 20), background="black", anchor="center")
l.pack(fill="both", expand=True)
# Define a function that will get the user input from the terminal and set it as the text of the Label widget
# def update():
#     response1 = requests.get('http://localhost:5000/send_sent_data')
#     print(response1.text)
#     input_data = response1.text
#     user_input = NLP.response(input_data)
#     print("User input:", user_input) # print the user input
#     # sp(user_input)
#     name.set(user_input) # clear the name variable
#     # input1.set(user_input)
#     # animate_text(user_input, 100)
#     response2 = requests.post('http://localhost:5000/get_data', data={'output': user_input})
#     print(response2.text)

#     animate_text(user_input,100)
#     if user_input == input_data:
#         time.sleep(0.5)
#     else:
#      print(user_input)
#      time.sleep(0.5)
#      root.mainloop()
def update():
    response1 = requests.get('http://localhost:5000/send_sent_data')
    print(response1.text)
    input_data = response1.text
    user_input = NLP.response(input_data)
    response2 = requests.post('http://localhost:5000/get_data', data={'output': user_input})
    print("User input:", user_input) # print the user input
    # sp(user_input)
    name.set(user_input) # clear the name variable
    # input1.set(user_input)
    # animate_text(user_input, 100)
    
    

    animate_text(user_input,100)
    
    if user_input == input_data:
        event = threading.Event()
        event.wait(0.1) # wait for 0.1 seconds before continuing with your code
    else:
        
        print(response2.text)
        print(user_input)
        root.mainloop()
     

 




# Define a function that will animate the text character by character with a delay
def animate_text(text, delta):
    # Get the current text of the Label widget
    current_text = name.get()
    # Check if there are more characters to add
    if len(current_text) < len(text):
        # Add one more character to the current text
        current_text += text[len(current_text)]
        # Update the text of the Label widget
        name.set(current_text)
        # Check if the current character is a space or not
        if current_text[-1] == " ":
            # If it is a space, make it normal and dark gray
            l.config(font=("Times New Roman", 20, "normal"), foreground="dark gray")
        else:
            # If it is not a space, make it bold and yellow
            l.config(font=("Times New Roman", 20, "bold"), foreground="yellow")
            # Play a typing sound effect
        # Schedule the animate_text function to run again after delta milliseconds
        root.after(delta, animate_text, text, delta)
    else:
        print("Text length:", len(text)) # print the text length
        
        
        # Play a ding sound effect
        update() # call the update function again

# Run the update function for the first time

 


 


update()
# Start the main loop


