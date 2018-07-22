'''
リストの作成
'''
import random

index = random.sample(range(18), 18) #抽出する添字を取得

sq = [(i) for i in index]  #sampleをとる
for i in index:
  if sq[i] == 0:
    print("A")
  if sq[i] == 1:
    print("B")
  if sq[i] == 2:
    print("C")
  if sq[i] == 3:
    print("D")
  if sq[i] == 4:
    print("E")
  if sq[i] == 5:
    print("F")
  if sq[i] == 6:
    print("G")
  if sq[i] == 7:
    print("H")
  if sq[i] == 8:
    print("I")
  if sq[i] == 9:
    print("J")
  if sq[i] == 10:
    print("K")
  if sq[i] == 11:
    print("L")
  if sq[i] == 12:
    print("M")
  if sq[i] == 13:
    print("N")
  if sq[i] == 14:
    print("O")
  if sq[i] == 15:
    print("P")
  if sq[i] == 16:
    print("Q")
  if sq[i] == 17:
    print("R")
