city_map = {}

while True:
        city = input("Please enter the name of the city: ")
        city = city.replace(" ","")
        number_of_citizens = len(city) * 1_000_000
        city_map[city] = number_of_citizens
        if(city == 'alger'):
            break;

#this creates a lambda function that gets me the values of the map and then it makes a list of tuples and sorts them by the values of the map
print(city_map.items())
city_map_sorted = dict(sorted(city_map.items(), key=lambda item: item[1] ,reverse=True))
print(city_map_sorted)