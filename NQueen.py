
from typing import List


def backtrack(r):
    
    if r ==n:
        copy=["  ".join(row) for row in board]
        print(copy)
        final.append(copy)
        return 


    for c in range(n):
        if c in col or (r+c) in positiveDigonal or (r-c) in NegativeDigonal:
            continue

        col.add(c)
        positiveDigonal.add(r+c)
        NegativeDigonal.add(r-c)

        board[r][c]="Q"
        backtrack(r+1)
        col.remove(c)
        positiveDigonal.remove(r+c)
        NegativeDigonal.remove(r-c)

        board[r][c]="#"



if __name__ == '__main__':


    print("Enter the number of Queens:")
    n=int(input())
    col=set()
    positiveDigonal=set() #(r+c)
    NegativeDigonal=set() #(r-c)
    final=[]
    board=[["#"]*n for i in range(n)]
    print(board)

    
        
    backtrack(0) 
    for mat in final:
        for row in mat:
            print(row,end='\n')
        print('\n')
    
  

    
    