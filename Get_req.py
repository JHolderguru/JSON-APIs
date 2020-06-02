#1st we need a way to talk HTTP

#we'll use the requests package that is very stable and widely used


# this is a standar py library no need to install:
#
# import time
#
# time.sleep()

#requests is not a standard library and must be installed with a package manager

    #installs and manages these packages

    #python, ruby, javascript, java, c# almost all languages have a package

import requests

# I want to make a get request to get more info on my postcode
# I need to check my API documentation
# then build the target url with path and arguments
#  then I need to use the package request to make the request
# I wil, receive a JSON that I need to parse into a dictionary

path = 'http://api.postcodes.io/postcodes/'
arguments = 'rm41pb'

#Buil ur
url_target = path + arguments
#print(url_target)

#Make request and capture response
response = requests.get(url_target)

#print(response)
print(type(response))

# Parsing or getting the dictionary out
print(response.json())
response_dictionary = response.json()

#print(type(response_dictionary))
print(type(response_dictionary))
# for key in response_dictionary.keys():
#     print(key)

result_dictionary = response_dictionary['result']

#print(result_dictionary)

for key in result_dictionary.keys():
    print(key, 'the value inside is', result_dictionary[key])