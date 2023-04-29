def flights(*args):
    flights_dict = {}

    for index, flight in enumerate(args):
        if flight == "Finish":
            break

        if index % 2 == 0:
            if flight not in flights_dict:
                flights_dict[flight] = 0
        else:
            flights_dict[args[index - 1]] += int(flight)

    return flights_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))

