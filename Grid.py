from dataclasses import dataclass

# grid size
width = 5
height = 5


@dataclass(frozen=True)
class Grid:
    grid_width: int = width
    grid_height: int = height

    def valid_x(self, pox_x):
        return self.grid_width >= int(pox_x) >= 0

    def valid_y(self, pos_y):
        return self.grid_height >= int(pos_y) >= 0

    def valid_position(self, pos_x, pos_y):
        max_grid_limit = self.grid_width * self.grid_height
        if self.valid_x(int(pos_x)) and self.valid_y(int(pos_y)):
            return int(pos_x) * int(pos_y) <= max_grid_limit
        else:
            return False
