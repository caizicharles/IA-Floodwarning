<<<<<<< HEAD
=======
def stations_within_radius(stations, centre, r):
    distance_from_position = []
    names = []
    station_coordinates = []
    station_x_coordinate = []
    station_y_coordinate = []
    for i in stations:
        station_coordinates.append(i.coord)
    for i in stations:
        names.append(i.name)

    for i in range(len(station_coordinates)):
        station_x_coordinate.append(station_coordinates[i][0])
    
    for i in range(len(station_coordinates)):
        station_y_coordinate.append(station_coordinates[i][1])
    
    for i in range(len(station_coordinates)):
        a = station_x_coordinate[i]
        b = station_y_coordinate[i]
        distance = ((a - centre)**2 + b**2)**0.5
        distance_from_position.append(distance)

    for i in distance_from_position:
        if i > r:
            names.pop(i)
        else:
            continue
    
    


>>>>>>> ec5c9bd059ac7f8a69049dac35543bcfc7fa4da3
