move = {
    'N': [0, 1],
    'E': [1, 0],
    'W': [-1, 0],
    'S': [0, -1]
}

next_rotation_l = {
    'N': 'W',
    'E': 'N',
    'W': 'S',
    'S': 'E'
}

next_rotation_r = {
    'N': 'E',
    'E': 'S',
    'W': 'N',
    'S': 'W'
}


def calculate_next_position(position_x, position_y, rotation, orientations):
    for orientation in orientations:
        if orientation == 'L':
            rotation = next_rotation_l.get(rotation)
        elif orientation == 'R':
            rotation = next_rotation_r.get(rotation)
        elif orientation == 'M':
            position_x = int(position_x) + move[rotation][0]
            position_y = int(position_y) + move[rotation][1]

    return position_x, position_y, rotation


x_size, y_size = input().split()
while(True):
    try:
        first_position = input()
        position_x, position_y, rotation = first_position.split()
        orientations = input().split()
        x, y, r = calculate_next_position(
            position_x, position_y, rotation, orientations)
        print(x, y, r)
    except Exception as e:
        print("Somethings went wrong with this error: ", e)
        break;
