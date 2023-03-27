
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

def getCandidateAction(status, prev):
    leftm, leftc, rightm, rightc, turn = status
    actions = []
    if turn == 0:
        if leftm >= 1 and leftc >= 1:
            actions.append("1C1M")
        if leftm >= 1:
            actions.append("1M")
        if leftm >= 2:
            actions.append("2M")
        if leftc >= 1:
            actions.append("1C")
        if leftc >= 2:
            actions.append("2C")

    if turn == 1:
        if rightm >= 1 and rightc >= 1:
            actions.append("1C1M")
        if rightm >= 1:
            actions.append("1M")
        if rightm >= 2:
            actions.append("2M")
        if rightc >= 1:
            actions.append("1C")
        if rightc >= 2:
            actions.append("2C")

    if prev != "INIT":
        actions.remove(prev)
    return actions


def PrintCMDS(answer):
    for tmp in answer:
        print(tmp[0], end="-")

if __name__ == "__main__":

    answer = []
    status = []
    status.append((3, 3, 0, 0, 0))
    answer.append(getCandidateAction(status[0], "INIT"))

    while True:
        Display(status[-1])
        cmd = answer[-1][0]
        nextStatus = GameWorld(status[-1], cmd)
        state = GameDefine(nextStatus)

        if state == 1:
            PrintCMDS(answer)
            answer[-1].pop(0)
            if len(answer[-1]) == 0:
                answer.pop(-1)
            print("Game Over")
        elif state == 2:
            PrintCMDS(answer)
            print("Success!")
            break
        else:
            isbe = False
            for compare in status[1:]:
                if compare == nextStatus or nextStatus == status[0]:
                    answer[-1].pop(0)
                    isbe = True
                    break
            if isbe == False:
                status.append(nextStatus)
                answer.append(getCandidateAction(status[-1], cmd))

        if len(answer[-1]) == 0:
            PrintCMDS(answer[:-2])
            print("Game Over")
            status.pop(-1)
            answer.pop(-1)
            answer[-1].pop(0)

