{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 2
}

import string
import random 
import nltk


hours = {
    'Monday' : '8am - 8pm', 
    'Tuesday' : '8am - 8pm', 
    'Wednesday' : '8am - 8pm', 
    'Thursday' : '8am - 8pm', 
    'Friday' : '8am - 8pm', 
    'Saturday' : '10am - 4pm', 
    'Sunday' : 'CLOSED'
}
print(hours)

Breakfast_Menu = {
    'Pancakes': '$5', 
    'Waffles': '$4', 
    'French Toast': '$6', 
    'Eggs Benedict': '$9', 
    'Omelette': '$7', 
    'Protein Bowl': '$8', 
    'Hash Browns': '$2', 
    'Boiled egg': '$1', 
    'Toast': '$1'
}
print(Breakfast_Menu)

Lunch_Menu = {
    'Garlic Bread': '$4', 
    'Chicken Noodle Soup': '$3', 
    'Ceasar Salad': '$5',
    'Grilled Chicken': '$9', 
    'Salmon': '$12', 
    'Poke Bowl': '$13', 
    'Chicken Alfredo Pasta': '$11', 
    'Lasagna': '$10', 
    'BLT Sandwich': '$7'
}
print(Lunch_Menu)

Dinner_Menu = {
    'Calamari': '$6', 
    'Sliders': '$5', 
    'Mashed Potatoes': '$4', 
    'Crispy Brussel Sprouts': '$8', 
    'Shrimp Linguini': '$15', 
    'Steak': '$17', 
    'Burger': '$14', 
    'Impossible Burger': '$16'
}
print(Dinner_Menu)


# This cell defines a collection of input and output things this chatbot can say and respond to
GREETINGS_IN = ["hello", "hi", "hey", "hola", "welcome", "bonjour", "greetings"]
GREETINGS_OUT = ["Hiya!", "Hey!", "Hello!", "Hey there!", "How can I help you today?"]

HOURS_IN = ["hours", "open", "time", "close"]
HOURS_OUT = ["Here are our hours of operation"] 


MENU_IN = ["cuisine", "menu", "serve", "type"] 
MENU_OUT = ["Here are our menus"]

RESERVATION_IN = ["yes", "no"]
RESERVATION_OUT = ["When would you like the reservation for? We only reserve tables at each hour"]

DAY_IN = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
TIME_IN = ["8am", "9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm", "5pm", "6pm", "7pm"]
TIME_SAT_IN = ["10am", '11am', "12pm", "1pm", "2pm", "3pm", "4pm"]
DAY_AND_TIME_OUT = ["Great, how many people are in your party?", "Sorry, we are not open at that time"]

PEOPLE_IN_PARTY_OUT = ["Sounds great! do you have a prefferance of sitting inside or outside?", 
                       "I'm sorry, we cannot book a table for so many people, you can always try a walk in"]

PREFERENCE_IN = ["inside", "outside", "either",]
PREFERENCE_OUT = ["Fantastic!", "Great!", "Sounds good!"]

NOPE_IN = ["drinks", "a bar", "alcohol", "catering"]
NOPE_OUT = ["We do not provide"]

UKNOWN = ["Thank you for your time!",
         "Okay!"]


def is_question(input_string):
    """Checks if the input is a question"""
    
    output = False
    if '?' in input_string:
        output = True
    else:
        output = False
    return output


def remove_punctuation(input_string):
    """Removes the punctuation from the input"""
    
    out_string = ''
    for char in input_string:
        if char not in string.punctuation:
            out_string += char
    return out_string


def prepare_text(input_string):
    """Prepares the input to match the output lists to be able to respond appropriately """
    
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    return out_list


def selector(input_list, check_list, return_list):
    """Selects an output from a list based on the key words in the input list"""
    
    output = None
    for element in input_list:
        if element in check_list:
            output = random.choice(return_list)
            break
    return output


def string_concatenator(string1, string2, separator):
    """Combines strings"""
    
    result = string1 + separator + string2
    return result


def list_to_string(input_list, separator):
    """Changes inputs in a list and combines them to make a string"""
    
    output = ''
    output = input_list[0]
    for element in input_list[1:]:
        output = string_concatenator(output, element, separator)
    return output


def end_chat(input_list):
    """When the user inputs 'quit', the chat ends"""
    
    if 'quit' in input_list:
        return True
    else:
        return False
    
    
def is_in_list(list_one, list_two):
    """Check if any element of list_one is in list_two."""
    
    for element in list_one:
        if element in list_two:
            return True
    return False

def find_in_list(list_one, list_two):
    """Find and return an element from list_one that is in list_two, or None otherwise."""
    
    for element in list_one:
        if element in list_two:
            return element
    return None


def check_for_greeting(msg):
    """Checks if any of the words used in the user's sentence are greetings, in order to respond in a greeting"""
    
    output = None
    for word in msg.split():
        if word.lower() in GREETINGS_IN:
            return 'Would you like to make a reservation'
        
        
def check_for_hours(question):
    """Checks if the question is related to the hours of operation"""
    
    output = None
    for word in question.split():
        if word.lower() in HOURS_IN:
            for keys, values in hours.items():
                print(keys)
                print(values)
        return HOURS_OUT
    
    
def menu(question):
    """Checks if the input is asking a question about the type of food"""
    
    output = None
    for word in question.split():
        if word.lower in MENU_IN:
            for keys, values in Breakfast_Menu.items():
                print(keys)
                print(values)
                
            for keys, values in Lunch_Menu.items():
                print(keys)
                print(values)
                
            for keys, values in Dinner_Menu.items():
                print(keys)
                print(values)
           
            print("Would you like to make a reservation?")
    return MENU_OUT


def reservation(msg):
    """Checks if the user would like to make a reservation"""
    
    if 'yes' == msg.lower():
        print(RESERVATION_OUT)
        return True
    elif 'no' == msg.lower():
        return False
    
    
def day_and_time(msg):
    """Checks if the day and time are within the hours of operations and outputs whether they are closed or if that day and time is possible"""
    msg = msg.lower()
    message = msg.split()
    if message[0] in DAY_IN[-1]:
        if message[-1] in TIME_SAT_IN:
            return "Great!, how many people are in your party?"
        else:
            return "Sorry, we are not open at that time, is there another time you would like to come in?, please check our hours of operation"

    if message[0] in DAY_IN[0:5]:
        if message[-1] in TIME_IN:
            return "Great!, how many people are in your party?"
        else:
            return "Sorry, we are not open at that time, is there another time you would like to come in?, please check our hours of operation"
    
    else:
        return "Sorry, we're closed on Sundays! Please make a reservation for a different day!"
    
    
def number_of_people_in_party(number):
    """Checks the number of people in the party"""
    
    if number > 0 and number <= 10:
        return ("Sounds great! do you have a prefferance of sitting inside or outside?")
    else:
        return ("Sorry, we cannot make reservations for parties greater than 10! You can alays try walking in")
    
    
def inside_outside(msg):
    """Checks whether the user would like to be seated inside or outside"""
    output = None
    for word in msg.split():
        if word.lower() in PREFERENCE_IN:
            return random.choice(PREFERENCE_OUT)
