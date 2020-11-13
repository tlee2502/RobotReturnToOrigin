public class Robot {
	
    public boolean backToOrigin(String moves) {
        int x = 0, y = 0;
		
        for (char i : moves.toCharArray()) {
            if (i == 'U') {
                y--;
            } else if (i == 'D') {
				y++;
            } else if (i == 'L') {
				x--;
            } else if (i == 'R') {
				x++;
            }
        }	
        return (x == 0 && y == 0);
    }
}