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
