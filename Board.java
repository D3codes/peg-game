class Board {
  private boolean[] board = new boolean[15];

  public Board() {
    setBoard();
  }

  public void setBoard() {
    for(int i = 1; i < board.length; i++)
      board[i] = true;

    board[0] = false;
  }

  public boolean movePossible() {
    for(int i = 0; i < board.length; i++) {
      for(int j = 0; j < board.length; j++) {
        if(canMove(i, j))
          return true;
      }
    }
    return false;
  }

  public boolean wonGame() {
    int pegs = 0;
    for(int i = 0; i < board.length; i++) {
      if(board[i])
        pegs++;
      if(pegs > 1)
        return false;
    }
    return true;
  }

  public boolean isOccupied(int index) {
    return board[index];
  }

  public boolean canMove(int start, int end) {
    if(!board[start] || board[end])
      return false;

    int middle = middle(start, end);
    if(middle == -1)
      return false;

    return board[middle];
  }

  private int middle(int start, int end) {
    switch(start) {
      case 0:
        if(end == 3)
          return 1;
        if(end == 5)
          return 2;
        break;

      case 1:
        if(end == 6)
          return 3;
        if(end == 8)
          return 4;
        break;

      case 2:
        if(end == 7)
          return 4;
        if(end == 9)
          return 5;
        break;

      case 3:
        if(end == 0)
          return 1;
        if(end == 5)
          return 4;
        if(end == 10)
          return 6;
        if(end == 12)
          return 7;
        break;

      case 4:
        if(end == 11)
          return 7;
        if(end == 13)
          return 8;
        break;

      case 5:
        if(end == 0)
          return 2;
        if(end == 3)
          return 4;
        if(end == 12)
          return 8;
        if(end == 14)
          return 9;
        break;

      case 6:
        if(end == 1)
          return 3;
        if(end == 8)
          return 7;
        break;

      case 7:
        if(end == 2)
          return 4;
        if(end == 9)
          return 8;
        break;

      case 8:
        if(end == 1)
          return 4;
        if(end == 6)
          return 7;
        break;

      case 9:
        if(end == 2)
          return 5;
        if(end == 7)
          return 8;
        break;

      case 10:
        if(end == 3)
          return 6;
        if(end == 12)
          return 11;
        break;

      case 11:
        if(end == 4)
          return 7;
        if(end == 13)
          return 12;
        break;

      case 12:
        if(end == 5)
          return 8;
        if(end == 3)
          return 7;
        if(end == 10)
          return 11;
        if(end == 14)
         return 13;
        break;

      case 13:
        if(end == 4)
          return 8;
        if(end == 11)
          return 12;
        break;

      case 14:
        if(end == 5)
          return 9;
        if(end == 12)
          return 13;
        break;

      default:
        return -1;
    }
    return -1;
  }

  public boolean move(int start, int end) {
    if(!canMove(start, end))
      return false;

    board[start] = false;
    board[end] = true;
    board[middle(start, end)] = false;
    return true;
  }
}
