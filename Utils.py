class Path:
    @staticmethod
    def get_path(path, source):
        return '{}{}'.format(path, source)

class Color:
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 64)
    WHITE = (255, 255, 255)
    GRAY = (50, 50, 50)
    YELLOW = (247, 177, 33)
    RED = (255, 0, 0)