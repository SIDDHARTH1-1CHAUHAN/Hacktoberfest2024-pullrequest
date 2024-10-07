#Hacktoberfest Contribution:-
import random

class MazeGame:
    def __init__(self, size):
        self.size = size
        self.graph = {}
        self.maze = [[' ' for _ in range(size)] for _ in range(size)]
        self.player = (0, 0)
        self.goal = (size - 1, size - 1)
        self.create_graph()

    def create_graph(self):
        for i in range(self.size):
            for j in range(self.size):
                neighbors = []
                if i > 0: neighbors.append((i-1, j))  # Up
                if i < self.size-1: neighbors.append((i+1, j))  # Down
                if j > 0: neighbors.append((i, j-1))  # Left
                if j < self.size-1: neighbors.append((i, j+1))  # Right
                self.graph[(i, j)] = neighbors

    def print_maze(self):
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) == self.player:
                    print('P', end=' ')
                elif (i, j) == self.goal:
                    print('G', end=' ')
                else:
                    print(self.maze[i][j], end=' ')
            print()
        print()

    def dfs(self, current, visited=None):
        if visited is None:
            visited = set()

        visited.add(current)
        if current == self.goal:
            print("You have reached the goal!")
            return True

        for neighbor in self.graph.get(current, []):
            if neighbor not in visited:
                if self.dfs(neighbor, visited):
                    return True
        return False

    def move_player(self, direction):
        x, y = self.player
        if direction == 'w' and x > 0:
            self.player = (x-1, y)
        elif direction == 's' and x < self.size-1:
            self.player = (x+1, y)
        elif direction == 'a' and y > 0:
            self.player = (x, y-1)
        elif direction == 'd' and y < self.size-1:
            self.player = (x, y+1)

    def play(self):
        print("Welcome to the Maze Game! Use 'w', 'a', 's', 'd' to move.")
        self.print_maze()
        while self.player != self.goal:
            move = input("Enter move: ")
            self.move_player(move)
            self.print_maze()
        print("Congratulations, you've reached the goal!")


if __name__ == "__main__":
    size = 5  # Maze size (5x5)
    game = MazeGame(size)
    game.play()
