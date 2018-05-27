import java.awt.Font;
import java.awt.Graphics;
import java.applet.Applet;

public class AppletExample extends Applet {

    public void paint(Graphics graphics) {
	
	Font font = new Font("TimesRoman", 
			     Font.PLAIN, 32);
	graphics.setFont(font);
	graphics.drawString("Ciao Mondo!", 30, 75);
    }
}
