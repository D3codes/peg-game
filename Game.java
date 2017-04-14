class Game {

  private Console console;
  private Board board;

  public Game() {
    board = new Board();
    console = new Console(board);
  }

  public void play() {
    int[] moves;
    console.clearScreen();
    while(true) {
      console.printBoard();
      moves = console.getMove();
      console.clearScreen();
      if(!board.move(moves[0], moves[1]))
        console.invalidMoveMessage();

      if(board.wonGame()) {
        console.winMessage();
        if(console.playAgain())
          board.setBoard();
        else
          break;
      }

      if(!board.movePossible()){
        console.gameOverMessage();
        if(console.playAgain())
          board.setBoard();
        else
          break;
      }
    }
  }
}
