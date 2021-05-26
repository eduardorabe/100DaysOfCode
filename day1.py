#1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of his pet.

#4. Combine the name of their city and pet and show them their band name.

#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/

print("Hi! Welcome to Band Name Creator!")
print("What's the name of the city you grew up in?")
city = input()
print("What's your favorite pet name?")
petname = input()

print(city + " " + petname + " " + "could be your band name!")
