#Creating a mapping of the states to abbreviate in the line of code
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
    'Washington': 'WA',
    'Mississippi': 'MS'
}

#Creating a badic set of states and the cites within them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
    'WA': 'Pullman',
    'MS': 'Jackson'
}

#adding more cites
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)
print("Michigan's abbreviation is:" , states['Michigan'])
print("Florida's abbreviation is:" , states['Florida'])
print("Washington's avvreviation is:" , states['Washington'])

#Do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])
print("Washington has: ", cities[states['Washington']])

#Print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#Print every city in states
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#Now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
#Safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

#Get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
