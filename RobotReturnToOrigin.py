class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0;
        y = 0;
        for i in range(0, len(moves)):
            if moves[i] == "R":
                x += 1
            if moves[i] == "L":
                x -= 1
            if moves[i] == "U":
                y += 1
            if moves[i] == "D":
                y -= 1
        if ((x == 0) & (y == 0)):
            return True
        else:
            return False