import random
import math
import signal
import time

playerOneHealth: int
playerTwoHealth: int
playerOneParalyzed = 0
playerTwoParalyzed = 0
currentPlayer = 1
playerTwoAI: bool
attacks = [
    "Mega Punch",
    "Super Smash",
    "Ninja Kick",
    "Leprechaun Magic",
    "Pirate Attack"
]

def chooseAttack(player: int) -> str:
    print("Attacks:")
    for i in range(len(attacks)):
        print("  " + str(i + 1) + ". " + attacks[i])
    if playerTwoAI and player == 2:
        xRaw = random.randint(0, len(attacks) - 1)
        x = str(xRaw)
        print("Choose Attack for Player " + str(player) + ": " + attacks[xRaw])
    else:
        x = input("Choose Attack for Player " + str(player) + ": ")
    for i in range(len(attacks)):
        if x.lower() == attacks[i].lower():
            return attacks[i]
        elif x == str(i + 1):
            return attacks[i]
    print("Invalid Attack!")
    return chooseAttack(player)

def fixHealth():
    global playerOneHealth, playerTwoHealth
    if playerOneHealth < 0:
        playerOneHealth = 0
    if playerTwoHealth < 0:
        playerTwoHealth = 0

def handleEffective(player: int):
    global playerOneHealth, playerTwoHealth, playerOneParalyzed, playerTwoParalyzed
    print("Effective Attack!")
    damage = random.randint(11, 20)
    paralyze = math.ceil((damage - 10) / 4)
    print("Player " + str(player) + " Did " + str(damage) + " Damage!")
    if player == 1:
        if not handleBlock(player):
            playerTwoHealth = playerTwoHealth - damage
            fixHealth()
            print("Player 2 Has " + str(playerTwoHealth) + " Health!")
            if paralyze > playerTwoParalyzed:
                playerTwoParalyzed = playerTwoParalyzed + paralyze
            print("Player 2 Is Paralyzed For " + str(playerTwoParalyzed) + " Turns!")
    elif player == 2:
        if not handleBlock(player):
            playerOneHealth = playerOneHealth - damage
            fixHealth()
            print("Player 1 Has " + str(playerOneHealth) + " Health!")
            if paralyze > playerOneParalyzed:
                playerOneParalyzed = playerOneParalyzed + paralyze
            print("Player 1 Is Paralyzed For " + str(playerOneParalyzed) + " Turns!")

def handleIneffective(player: int):
    global playerOneHealth, playerTwoHealth
    print("Ineffective Attack!")
    damage = random.randint(1, 10)
    print("Player " + str(player) + " Attacked With " + str(damage) + " Damage!")
    if player == 1:
        if not handleBlock(player):
            playerTwoHealth = playerTwoHealth - damage
            fixHealth()
            print("Player 2 Has " + str(playerTwoHealth) + " Health!")
    elif player == 2:
        if not handleBlock(player):
            playerOneHealth = playerOneHealth - damage
            fixHealth()
            print("Player 1 Has " + str(playerOneHealth) + " Health!")

def handleAttack(attack: str, player: int):
    effectiveAttack = random.randint(1, len(attacks))
    for i in range(len(attacks)):
        if attack == attacks[i]:
            if effectiveAttack == i:
                handleEffective(player)
            else:
                handleIneffective(player)

def alarmHandler(*_):
    raise ValueError("TimeoutError")

signal.signal(signal.SIGALRM, alarmHandler)

def inputTimeout(timeout: int) -> str:
    signal.alarm(timeout)
    try:
        return input("> ")
    except ValueError:
        print("\nYou Ran Out Of Time!")
        return ""
    finally:
        signal.alarm(0)

def handleBlock(player: int) -> bool:
    blockingPlayer = player + 1
    if blockingPlayer == 3:
        blockingPlayer = 1
    print("Player " + str(blockingPlayer) + ", Block in 3,")
    time.sleep(1)
    print("Player " + str(blockingPlayer) + ", Block in 2,")
    time.sleep(1)
    print("Player " + str(blockingPlayer) + ", Block in 1,")
    time.sleep(1)
    print("Player " + str(blockingPlayer) + ", Press a Random Key 1-4 Then Hit ENTER to Block!")
    key = random.randint(1, 4)
    if playerTwoAI and blockingPlayer == 2:
        keyPress = str(random.randint(1, 4))
        print("> " + keyPress)
    else:
        keyPress = inputTimeout(2)
    if keyPress == str(key):
        print("Attack Blocked!")
        return True
    else:
        print("Block Failed!")
        return False

print("NinjaFight By Connor Nolan!\n")

def setHealth():
    global playerOneHealth, playerTwoHealth
    defaultHealth = input("Enter Default Health (100): ")
    if defaultHealth == "":
        playerOneHealth = 100
        playerTwoHealth = 100
    else:
        try:
            if int(defaultHealth) >= 0:
                playerOneHealth = int(defaultHealth)
                playerTwoHealth = int(defaultHealth)
            else:
                print("Invalid Value!")
                setHealth()
        except ValueError:
            print("Invalid Value!")
            setHealth()

def setAI():
    global playerTwoAI
    defaultAI = input("Enter If Player 2 is an AI (False): ")
    if defaultAI == "":
        playerTwoAI = False
    elif defaultAI.lower() == "false":
        playerTwoAI = False
    elif defaultAI.lower() == "true":
        playerTwoAI = True
    elif defaultAI.lower() == "no":
        playerTwoAI = False
    elif defaultAI.lower() == "yes":
        playerTwoAI = True
    elif defaultAI.lower() == "n":
        playerTwoAI = False
    elif defaultAI.lower() == "y":
        playerTwoAI = True
    elif defaultAI.lower() == "0":
        playerTwoAI = False
    elif defaultAI.lower() == "1":
        playerTwoAI = True
    else:
        print("Invalid Value!")
        setAI()

setHealth()
setAI()
print("Player 1 Has " + str(playerOneHealth) + " Health!")
print("Player 2 Has " + str(playerTwoHealth) + " Health!\n")

while playerOneHealth > 0 and playerTwoHealth > 0:
    if currentPlayer == 1:
        print("Player 1's Turn!")
        if playerOneParalyzed > 0:
            playerOneParalyzed = playerOneParalyzed - 1
            print("Player 1 Is Paralyzed For " + str(playerOneParalyzed) + " More Turns!")
        else:
            handleAttack(chooseAttack(currentPlayer), currentPlayer)
        print()
        currentPlayer = 2
    elif currentPlayer == 2:
        print("Player 2's Turn!")
        if playerTwoParalyzed > 0:
            playerTwoParalyzed = playerTwoParalyzed - 1
            print("Player 2 Is Paralyzed For " + str(playerTwoParalyzed) + " More Turns!")
        else:
            handleAttack(chooseAttack(currentPlayer), currentPlayer)
        print()
        currentPlayer = 1

if playerOneHealth < 1 and playerTwoHealth > 0:
    print("Player 2 Wins!")
elif playerOneHealth > 0 and playerTwoHealth < 1:
    print("Player 1 Wins!")
else:
    print("You Tied!")
