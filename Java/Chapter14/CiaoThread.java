class CiaoThread extends Thread {
    private String _name;
    private int _sleepTime;
    
    CiaoThread(String name, int sleepTime) { 
        _name = name;
        _sleepTime = sleepTime; 
    }
    public void run() {
        try {
            for(int i=0; i<10; i++) {
                Thread.sleep(_sleepTime);
                System.out.println(_name + ": Ciao!");
            }
        } catch (InterruptedException ie) {
            System.err.println(ie.getMessage());
        }
    }
}
