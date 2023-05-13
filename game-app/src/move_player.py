

class MovePlayer:

    def __init__(self, map, height, width, step, move_y, move_x, find):
        self.self = self
        self.map = map
        self.height = height
        self.width = width
        self.step = step
        self.move_y = move_y
        self.move_x = move_x
        self.find = find

    def move(self, move_y, move_x):
        wall = 1
        ball = 3
        end = 5
        if self.game_end():
            return

        old_player_y, old_player_x = self.find()
        new_player_y = old_player_y + move_y
        new_player_x = old_player_x + move_x

        if self.map[new_player_y][new_player_x] == wall:
            return

        if self.map[new_player_y][new_player_x] in [ball, end]:
            new_ball_y = new_player_y + move_y
            new_ball_x = new_player_x + move_x

            if self.map[new_ball_y][new_ball_x] in [wall, ball, end]:
                return

            self.map[new_player_y][new_player_x] -= 3
            self.map[new_ball_y][new_ball_x] += 3

        self.map[old_player_y][old_player_x] -= 4
        self.map[new_player_y][new_player_x] += 4
        self.step += 1
