def calculate_platform_reqd(arrivals, departures, no_of_trains):
    # Sorting the given arrival and departure arrays
    arrivals.sort()
    departures.sort()

    # Initializing counters, trains and platforms variable
    i = j = 0
    total_trains = 1
    platforms_reqd = 1 if no_of_trains >  0 else 0

    # Looping till all arrival and departures are processed
    while (j < no_of_trains and (i + 1) < no_of_trains):
        # Checking if next arrival is lesser than current departure
        if (arrivals[i+1] <= departures[j]):
            # Increasing total trains count when new train arrives
            total_trains += 1
            i += 1

            # Saving maximum trains at a time to platforms required
            if (total_trains > platforms_reqd):
                platforms_reqd = total_trains
        else:
            # Decreasing total trains count when a train departs
            total_trains -= 1
            j += 1
    return platforms_reqd

# Creating an array of Train arrival and departure times
arrivals    =   [900,  915, 1030, 1045]
departures  =   [930, 1300, 1100, 1145]
no_of_trains =   len(arrivals)

# Calling the function to calculate required platforms
platforms_reqd = calculate_platform_reqd(arrivals, departures, no_of_trains)

print("Minimum Number of Railway Platforms Required: ", platforms_reqd)
# Minimum Number of Railway Platforms Required: 3