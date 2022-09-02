import sys


class RoverRoute:
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

    def __init__(self, x, y, rotation, x_boundary, y_boundary):
        self.x = int(x)
        self.y = int(y)
        self.rotation = rotation
        self.x_boundary = int(x_boundary)
        self.y_boundary = int(y_boundary)

    def update(self, orientation):
        if orientation == 'L':
            self.rotation = self.next_rotation_l.get(self.rotation)
        elif orientation == 'R':
            self.rotation = self.next_rotation_r.get(self.rotation)
        elif orientation == 'M':
            self.x = self.x + self.move[self.rotation][0]
            self.y = self.y + self.move[self.rotation][1]
        if self.x > self.x_boundary + 1 or self.y > self.y_boundary + 1:
            raise Exception("new plateau position is out of range")


class StreamingInputOutput:
    def __init__(self, stream_in):
        self.stream_in = stream_in

    def read(self):
        return self.stream_in.readline()


def main():
    stream = StreamingInputOutput(sys.stdin)
    x_size, y_size = stream.read().split()

    while(True):
        try:
            x, y, rotation = stream.read().split()
            plateau = RoverRoute(x, y, rotation, x_size, y_size)
            movements = stream.read().split()
            for rotate_or_move in movements:
                plateau.update(rotate_or_move)

            print(plateau.x, plateau.y, plateau.rotation)
        except Exception as e:
            print("Exception raised: ", e)
            break


if __name__ == "__main__":
    main()
