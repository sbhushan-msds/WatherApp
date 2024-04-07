# DSC 510 - Winter 2021
# Week 12
# Weather Program - Final Project
# Author - Shashi Bhushan
# 03/05/2022

# Change #None

import requests  # importing requests library


def pretty_print(dictionary, unit_type):  # Printing function
    print("Current Weather Conditions For", dictionary['name'])
    print("Current Temp:", dictionary['main']['temp'], unit_type)
    print("High Temp:", dictionary['main']['temp_max'], unit_type)
    print("Low Temp:", dictionary['main']['temp_min'], unit_type)
    print("Pressure:", dictionary['main']['pressure'], "hPa")
    print("Humidity:", dictionary['main']['humidity'], "%")
    print("Cloud Cover:", dictionary['weather'][0]['main'])
    print("Description:", dictionary['weather'][0]['description'])


def metric_type(unit):  # function for selecting metric type
    if unit == "F":
        unit = "imperial"
    elif unit == "C":
        unit = "metric"
    else:
        unit = "standard"
    return unit


def lookup_city():  # function for creating dictionary from json data by city name
    city_name = input("Please enter the city name:")
    state_abb = input("Please enter the state abbreviation:")
    print("Would you like to view temps in Fahrenheit, Celsius, or Kelvin.")
    while True:
        unit_type = input("Enter 'F' for Fahrenheit, 'C' for Celsius, 'K' for Kelvin:")
        if unit_type == "F" or unit_type == "C" or unit_type == "K":
            unit_type_modified = metric_type(unit_type)
            break
        else:
            print("Incorrect Entry, try again.")
            continue
    api_url = "http://api.openweathermap.org/data/2.5/weather?appid=1ea1725143305231f8518933b1fc92f7" + "&q=" + city_name + "," + state_abb + ",us" + "&units=" + unit_type_modified  # defining url variable
    try:
        response = requests.get(api_url)  # sending request to url
        if response.status_code == 200:  # catches KeyErrors etc.
            info_weather = response.json()  # storing response as dictionary
            pretty_print(info_weather, unit_type)  # calling printing function
        else:
            print("check entries, try again!!")

    except requests.exceptions.RequestException as e:  # catches connection errors
        print("sorry, connection error, try again, Error is", e)


def lookup_zip():  # function for creating dictionary from json data by city zip, for line explanations see above
    while True:
        city_zip = input("Please enter the zip code:")
        if city_zip.isnumeric() and len(city_zip) == 5:
            break
        else:
            print("Enter zip codes in 5 digits only, try again")
            continue
    print("Would you like to view temps in Fahrenheit, Celsius, or Kelvin.")
    while True:
        unit_type = input("Enter 'F' for Fahrenheit, 'C' for Celsius, 'K' for Kelvin:")
        if unit_type == "F" or unit_type == "C" or unit_type == "K":
            unit_type_modified = metric_type(unit_type)
            break
        else:
            print("Incorrect Entry, enter F, C or K only")
            continue

    api_url = "http://api.openweathermap.org/data/2.5/weather?appid=1ea1725143305231f8518933b1fc92f7" + "&q=" + city_zip + "," + "us" + "&units=" + unit_type_modified  # defining url variable
    try:
        response = requests.get(api_url)  # sending request to url
        if response.status_code == 200:
            info_weather = response.json()  # storing response as dictionary
            pretty_print(info_weather, unit_type)
        else:
            print("check entries, try again!!")

    except requests.exceptions.RequestException as e:
        print("sorry, connection error, try again, Error is", e)


def weather_lookup():
    while True:  # Until correct values are entered, it loops
        try:
            name_zip = int(
                input("Would you like to lookup weather data by US City or zip code? Enter 1 for US City 2 for zip:"))
            if name_zip == 1:
                lookup_city()
                break
            elif name_zip == 2:
                lookup_zip()
                break
            else:
                print("Enter 1 or 2")
        except ValueError:
            print("Correct value not entered")
            continue


# Define Main


def main():
    print("Welcome to the Weather Program!!")
    weather_lookup()
    while True:  # multi call option
        continue_check = input("Would you like to perform another weather lookup? Enter Y or y: ")
        if (continue_check == "Y") or (continue_check == "y"):
            weather_lookup()
        else:
            print("Thanks for trying my program")
            break


if __name__ == "__main__":  # main method
    main()
