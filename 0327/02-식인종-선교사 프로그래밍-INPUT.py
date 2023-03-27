
def GameWorld(status, cmd):
    leftm, leftc, rightm, rightc, turn = status

    if cmd == '1C' and turn == 0 and leftc >= 1:
        leftc -= 1
        rightc += 1
    elif cmd == '1C' and turn == 1 and rightc >= 1:
        leftc += 1
        rightc -= 1
    elif cmd == '2C' and turn == 0 and leftc >= 2:
        leftc -= 2
        rightc += 2
    elif cmd == '2C' and turn == 1 and rightc <= 2:
        leftc += 2
        rightc -= 2

    elif cmd == '1M' and turn == 0 and leftm >= 1:
        leftm -= 1
        rightm += 1
    elif cmd == '1M' and turn == 1 and rightm >= 1:
        leftm += 1
        rightm -= 1
    elif cmd == '2M' and turn == 0 and leftm >= 2:
        leftm -= 2
        rightm += 2
    elif cmd == '2M' and turn == 1 and rightm <= 2:
        leftm += 2
        rightm -= 2
    elif cmd == '1C1M' and turn == 0 and leftm >= 1 and leftc >= 1:
        leftm -= 1
        rightm += 1
        leftc -= 1
        rightc += 1
    elif cmd == '1C1M' and turn == 1 and rightm >= 1 and rightc >= 1:
        leftm += 1
        rightm -= 1
        leftc += 1
        rightc -= 1

    turn += 1
    if turn > 1:
        turn = 0
    return (leftm, leftc, rightm, rightc, turn)

def GameDefine(status):
    leftm, leftc, rightm, rightc, turn = status
    gameState = 0  # 0 계속 / 1 게임오버 / 2 게임 승

    if (rightm != 0 and rightm < rightc) or (leftm != 0 and leftm < leftc):
        gameState = 1
    elif leftm == 0 and leftc == 0:
        gameState = 2

    return gameState

def Display(status):
  leftm, leftc, rightm, rightc, turn = status

  print(" " * (3-leftm), "☆" * leftm," "*20, "☆" * rightm)
  if(turn == 0):
    print(" " * 3, "▼", " "*20)
  else:
    print(" " * 3, " "*20, "▼")

  print(" " * (3-leftc), "★" * leftc, " "*20, "★" * rightc)

cmds = ["1C", "2C", "1M", "2M", "1C1M"]
import random
if __name__ == "__main__":
    answer = []
    status = (3, 3, 0, 0, 0)
    while True:
        Display(status)
        cmd = random.choice(cmds)  #input("커맨드를 입력하세요 :")
        nextStatus = GameWorld(status, cmd)
        state = GameDefine(nextStatus)
        if state == 1:
            print("Game Over")
            answer = []
            status = (3, 3, 0, 0, 0)
            #break
        elif state == 2:
            print("Success!")
            break
        else:
            answer.append(cmd)
            status = nextStatus

print(answer)