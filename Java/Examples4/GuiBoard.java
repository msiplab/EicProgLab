import java.awt.Container;
import java.awt.Color;
import javax.swing.JFrame;
import javax.swing.JTable;

/* 
 * （利用法） 
 * Board board = new GuiBoard(); 
 *
 */  
public class GuiBoard extends Board {
    
    private JTable _table;
    
    /* コンストラクタ */
    public GuiBoard() {
	super();
	JFrame boardFrame = new JFrame("オセロ");
	boardFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	boardFrame.setSize(160,160);
	boardFrame.setLocationRelativeTo(null);
	_table = new JTable(8,8);
	_table.setBackground(Color.GREEN);
	Container container = boardFrame.getContentPane();
	container.add(_table);
	boardFrame.setVisible(true);
    }
    
    /* ボードの状態の表示 */
    public void displayState() {
	try {
	    for (int y = 1; y < 9; y++) {
		for (int x = 1; x < 9; x++) {
		    if (_getState(x, y).toString().equals("W"))
			_table.setValueAt("○",y-1,x-1);
		    else if(_getState(x, y).toString().equals("B"))
			_table.setValueAt("●",y-1,x-1);
		}
	    }
	} catch(BoardOutOfRangeException boore) {
	    System.err.print(boore.getMessage());
	}
	super.displayState();
    }
}
