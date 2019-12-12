{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 2
}

from functions import*

assert callable(is_question)
assert isinstance(is_question('str'), bool)
assert is_question('when?') == True

assert callable(remove_punctuation)
assert isinstance(remove_punctuation('abc'), str)
assert remove_punctuation('Okay! Thank you for your time.') == 'Okay Thank you for your time'

assert callable(prepare_text)
assert isinstance(prepare_text('this that and the other.'), list)
assert prepare_text('What time do you open?') == ['what', 'time', 'do', 'you', 'open']

assert callable(selector)
assert selector(['time', 'open'], ['time'], ['yes']) == 'yes'
assert selector(['time', 'open'], ['type'], ['yes']) == None

assert callable(string_concatenator)
assert isinstance(string_concatenator('thank', 'you', ' '), str)
assert string_concatenator('thank', 'you', ' ') == 'thank you'

assert callable(list_to_string)
assert isinstance(list_to_string(['a', 'b'], '|'), str)
assert list_to_string(['a', 'b'], '|') == 'a|b'

assert callable(end_chat)
assert isinstance(end_chat(['a', 'b']), bool)
assert end_chat(['quit']) == True

assert callable(check_for_greeting)
assert isinstance(('hey!'), str)
assert 'How can I help you today?' in check_for_greeting('hey')
        
assert callable(check_for_hours)
assert check_for_hours('open') == ["Here are our hours of operation"]

assert callable(menu)
assert menu('What type of food do you serve?') == ["Here are our menus"]

assert callable(reservation)
assert reservation('yes') == True
assert reservation('no') == False

assert callable(day_and_time)
assert day_and_time('Sunday at 11am') == "Sorry, we're closed on Sundays! Please make a reservation for a different day!"
assert day_and_time('Saturday at 10am') == "Great!, how many people are in your party?"
assert day_and_time('Saturday at 12pm') == "Great!, how many people are in your party?"
assert day_and_time('Monday at 4pm') == "Great!, how many people are in your party?"
assert day_and_time('Monday at 8pm') == 'Sorry, we are not open at that time, is there another time you would like to come in?, please check our hours of operation'

assert callable(number_of_people_in_party)
assert number_of_people_in_party(5) == "Sounds great! do you have a prefferance of sitting inside or outside?"
assert number_of_people_in_party(11) == "Sorry, we cannot make reservations for parties greater than 10! You can alays try walking in"
