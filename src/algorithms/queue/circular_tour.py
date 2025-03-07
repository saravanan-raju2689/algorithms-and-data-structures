def circular_tour(pumps):
    total_petrol = 0
    total_distance = 0
    current_petrol = 0
    start_index = 0

    for i in range(len(pumps)):
        petrol, distance = pumps[i]
        total_petrol += petrol
        total_distance += distance
        current_petrol += petrol - distance

        if current_petrol < 0:
            start_index = i + 1
            current_petrol = 0

    if total_petrol < total_distance:
        return -1

    return start_index