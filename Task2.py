import requests
from pyfiglet import Figlet
import os, time

# Help! I'm trying to make this cool bot but my code is too messy :( Please help me organise it into reusable components.

# Define your reusable functions here:


import requests
from pyfiglet import Figlet
import time

def display_greeting():
    f = Figlet(font="slant")
    print(f.renderText("HEY!"))
    print("Welcome to the weird weather bot :)")
    print("-----------------------------------\n")


def get_name():
    return input("May I take your first name please? ")


def guess_gender(name):
    gender_resp = requests.get(f"https://api.genderize.io/?name={name}").json()
    gender = gender_resp["gender"]
    prob_percent = gender_resp["probability"] * 100
    return gender, prob_percent


def confirm_gender(gender, prob_percent):
    print(f"\nHmmm, I'm {prob_percent}% sure you are a {gender}.")
    response = input("Am I right? :) (Y/n)")
    if response.lower() in ["", "yes", "y", "ye"]:
        print("Wooooooh! Computer 1, Human 0.")
    else:
        print("Ahhhh, sorry! :(")

def get_postcode():
    while True:  
        postcode_raw = input("\nSo, what's your postcode? ")
        postcode_resp = requests.get(f"https://api.postcodes.io/postcodes/{postcode_raw}").json()
        
        if postcode_resp.get("status") == 200:  
            return postcode_resp['result']  
        else:
            print("Invalid postcode, please try again.") 


def get_location(postcode_data):
    postcode_resp = requests.get(f"https://api.postcodes.io/postcodes/{postcode}").json()
    area = postcode_resp['result']['admin_ward']
    longitude = postcode_resp['result']['longitude']
    latitude = postcode_resp['result']['latitude']
    return area, longitude, latitude


def show_waiting_dots(seconds=3):
    for _ in range(seconds):
        time.sleep(1)
        print("...")


def display_cat_fact():
    input("\nWould you like a cat fact while you wait? ")
    print("Doesn't matter what you think, I'm going to give you one anyway :)")
    time.sleep(3)
    joke_resp = requests.get("https://catfact.ninja/fact").json()
    joke = joke_resp['fact']
    print("\n###########################")
    print("CAT FACT:")
    print(f"\n{joke}\n")
    print("So interesting isn't it!")
    print("###########################")


def get_weather(longitude, latitude):
    api_key = "4d30afa58f6f935d861edecad3639cda" 
    weather_resp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}").json()
    return weather_resp

def kelvin_to_celsius(kelvin_temp):
    return int(kelvin_temp - 273.15)


def display_weather(weather_resp, area):
    weather_kelvin = weather_resp["main"]["temp"]
    weather_degrees = kelvin_to_celsius(weather_kelvin)
    main_weather_desc = weather_resp["weather"][0]["main"]
    second_weather_desc = weather_resp["weather"][0]["description"]
    
    print(f"\nThe weather in {area}:\n")
    print(str(weather_degrees) + "℃")
    print(f"{main_weather_desc} - {second_weather_desc}")


def weird_weather_bot():
    display_greeting()
    
    name = get_name()
    gender, prob_percent = guess_gender(name)
    confirm_gender(gender, prob_percent)
    
   
    postcode = get_postcode()
    area, longitude, latitude = get_location(postcode)
    print(f"Nice! so you live in {area}.\n")
    
  
    print("Let me just check the weather there today...\n")
    show_waiting_dots()
    display_cat_fact()
    
 
    print("\nWaiting 5 seconds for you to read the fact...")
    time.sleep(5)
    print("\nNow, back to getting the weather...")
    show_waiting_dots()
    
    weather_resp = get_weather(longitude, latitude)
    display_weather(weather_resp, area)
    
    print("\nThank you! Bye.")

weird_weather_bot()

# Make sure each function only does ONE thing!!!!!!!!!!!


###########################################

def weird_weather_bot():
    
    f = Figlet(font="slant")
    print(f.renderText("HEY!"))

    print("Welcome to the weird weather bot :)")
    print("-----------------------------------\n")
    name = input("May I take your first name please? ")
    gender_result = guess_gender(name)
    gender = gender_result[0]
    prob_percent = gender_result[1]
    print(f"\nHmmm, I'm {prob_percent}% sure you are a {gender}.")
    
    gender_correct = input("Am I right? :) (Y/n)")
    if gender_correct.lower() in ["", "yes", "y", "ye"]:
        print("Wooooooh! Computer 1, Human 0.")
    else:
        print("Ahhhh, sorry! :(")

    postcode_raw = input("\nSo, what's your postcode? ")
    postcode_resp = requests.get(f"https://api.postcodes.io/postcodes/{postcode_raw}").json()

    area = postcode_resp['result']['admin_ward']
    longitude = postcode_resp['result']['longitude']
    latitude = postcode_resp['result']['latitude']
    print(f"Nice! so you live in {area}.\n")

    print("Let me just check the weather there today...\n")
    
    for i in range(3):
        time.sleep(1)
        print("...")
    
    input("\nWould you like a cat fact while you wait? ")
    print("Doesn't matter what you think, I'm going to give you one anyway :)")
    time.sleep(3)
    joke_resp = requests.get("https://catfact.ninja/fact").json()
    joke = joke_resp['fact']
    print("\n###########################")
    print("CAT FACT:")
    print(f"\n{joke}\n")
    print("So interesting isn't it!")
    print("###########################")

    print("\nWaiting 5 seconds for you to read the fact...")
    time.sleep(5)
    print("\nNow, back to getting the weather...")

    for i in range(3):
        time.sleep(1)
        print("...")

    weather_resp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=4d30afa58f6f935d861edecad3639cda").json()
    # print(weather_resp)
    weather_kelvin = weather_resp["main"]["temp"]
    # convert to degrees
    weather_degrees = int(weather_kelvin - 273.15)
    main_weather_desc = weather_resp["weather"][0]["main"]
    second_weather_desc = weather_resp["weather"][0]["description"]
    print(f"\nThe weather in {area}:\n")
    print(str(weather_degrees) + "℃")
    print(f"{main_weather_desc} - {second_weather_desc}")
    print("\nThank you! Bye.")

weird_weather_bot()


# After you have written the reusable functions, answer the following:
# Questions:
# 1. What are the preconditions for your code not to break?
# the user must input valid data, e.g for the post code in order to get the location data
# 2. Validate the user's input based on your preconditions.
# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise.

# Further Tasks:
# 1. Put your functions def guess_gender(name):
    gender_resp = requests.get(f"https://api.genderize.io/?name={name}").json()
    gender = gender_resp["gender"]
    prob_percent = gender_resp["probability"] * 100
    return [gender, prob_percent]
in seperate appropriate files and import them in.
# 2. Make sure all of your functions (except the main one) only do ONE thing or process.
# 3. Add your own twist to the code.

# Extension:
# Add the following apis as reusable components and use them in your code:
# https://www.exchangerate-api.com/docs/overview
