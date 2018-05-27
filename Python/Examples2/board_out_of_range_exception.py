class BoardOutOfRangeException(Exception):
    """盤外指定時の例外クラス（Exceptionの子クラス）"""
    
    def __init__(self, msg):
        Exception.__init__(self, msg)
        
