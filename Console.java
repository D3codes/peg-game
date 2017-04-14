import java.util.*;

class Console {

  private Scanner scanner;
  private Board board;

  private static final String ANSI_CLEAR = "\u001b[2J";
	private static final String ANSI_HOME = "\u001b[H";

  public Console(Board b) {
    scanner = new Scanner(System.in);
    board = b;
  }

  public void printBoard() {
    System.out.println("    " + getSymbol(board.isOccupied(0))
                        + "             0");
    System.out.println("   " + getSymbol(board.isOccupied(1)) + " "
                        + getSymbol(board.isOccupied(2))
                        + "           1  2");
    System.out.println("  " + getSymbol(board.isOccupied(3)) + " "
                        + getSymbol(board.isOccupied(4)) + " "
                        + getSymbol(board.isOccupied(5))
                        + "         3  4  5");
    System.out.println(" " + getSymbol(board.isOccupied(6)) + " "
                        + getSymbol(board.isOccupied(7)) + " "
                        + getSymbol(board.isOccupied(8)) + " "
                        + getSymbol(board.isOccupied(9))
                        + "       6  7  8  9");
    System.out.println(getSymbol(board.isOccupied(10)) + " "
                        + getSymbol(board.isOccupied(11)) + " "
                        + getSymbol(board.isOccupied(12)) + " "
                        + getSymbol(board.isOccupied(13)) + " "
                        + getSymbol(board.isOccupied(14))
                        + "    10 11 12 13 14");
  }

  private char getSymbol(boolean peg) {
    if(peg)
      return '|';
    return 'o';
  }

  public int[] getMove() {
    int[] inputs = new int[2];
    System.out.print("Which peg do you want to move?: ");
    inputs[0] = scanner.nextInt();
    System.out.print("Where do you want to move it?: ");
    inputs[1] = scanner.nextInt();
    scanner.nextLine();
    return inputs;
  }

  public void invalidMoveMessage() {
    System.out.println("Invalid Move");
  }

  public void clearScreen() {
    System.out.print(ANSI_CLEAR+ANSI_HOME);
  }

  public void winMessage() {
    System.out.println("You Won!");
  }

  public void gameOverMessage() {
    System.out.println("Game Over");
  }

  public boolean playAgain() {
    System.out.print("Play Again? (y/n): ");
    char input = scanner.nextLine().charAt(0);
    if(input == 'y' || input == 'Y')
      return true;
    return false;
  }
}
