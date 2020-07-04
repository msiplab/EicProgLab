class CellState:
    """マス目の状態クラス"""
    
    def __init__(self, mark):
        """コンストラクタ"""
        self.__mark = mark
        
    def __str__(self):
        """文字列への変換"""
        return self.__mark 
