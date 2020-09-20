n, k = map(int, input().split())

class board:
    def __init__(self):
        self.dosk = []
    def create(self,n):
        for i in range(n):
            self.dosk(append(['.']*n))
        for i in range(n):
            print(self.dosk[i])
        return self.dosk
    def put(self,b,m,k):
        self.desk[b-1][m-1] = k 
    def chek(self):

class AI:
    def __init__(self):
        self.micro_ii = []
    def choise(self,desk):
        if
        
        
def var_1():
    desk = board()
    desk.create()
    v = 0
    while desk.chek == False:
        v += 1
        if v // 2 == 0:
            k = '0'
            print('Player 1')
            s,l = map(int, input().split())
            desk.put(s,l,k)
        else:
            k = 'x'
            print('Player 2')
            s, l = map(int, input().split())
            desk.put(s,l,k)
    if v // 2 == 0:
        return 'Player 2 WIN'
    else:
        return 'Player 1 WIN'
def var_2():
    desk = board()
    desk.create()
    while desk.chek == False:
        if v // 2 == 0:
            k = str(input('player 1'))
            desk.put(k)
        else:
            print('AI')
            
        
    