import javax.swing.JFrame;

public class SwingExample {

    public static void main(String[] args) {

       // JFrameクラスのインスタンスを生成 
        JFrame frame = new JFrame("プログラミング");

        // 閉じるボタン押下時のアプリケーションの振る舞いを決定
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // ウィンドウの初期サイズ（幅，高さ）をピクセル単位で設定
        frame.setSize(320, 160);
        // ウィンドウの表示場所を規定
        frame.setLocationRelativeTo(null);
        // ウィンドウを表示
        frame.setVisible(true); 
    } 
}
