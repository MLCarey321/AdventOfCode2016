#!/usr/bin/python3

import sys

bots = {}
outputs = {}
instructions = {}
finished = False
found = False
solutionA = 0
solutionB = 0


def giveToBot(bot, val):
    if bot not in bots.keys():
        bots.keys().append(bot)
        bots[bot] = [val]
    else:
        bots[bot].append(val)


def giveToOutput(output, val):
    if output not in outputs.keys():
        outputs.keys().append(output)
        outputs[output] = [val]
    else:
        outputs[output].append(val)

while True:
    instruction = sys.stdin.readline()
    if len(instruction) > 1:
        parts = instruction.split()
        if parts[0] == "value":
            value = int(parts[1])
            bot = int(parts[5])
            giveToBot(bot, value)
        else:
            bot = int(parts[1])
            lowDest = " ".join(parts[5:7])
            highDest = " ".join(parts[10:12])
            instructions.keys().append(bot)
            instructions[bot] = [lowDest, highDest]
    else:
        break

while not (finished and found):
    finished = True
    for bot in bots.keys():
        if len(bots[bot]) == 2:
            finished = False
            if 61 in bots[bot] and 17 in bots[bot]:
                solutionA = bot
                found = True
            lowParts = instructions[bot][0].split()
            highParts = instructions[bot][1].split()
            lowDestNum = int(lowParts[1])
            highDestNum = int(highParts[1])
            lowVal = min(bots[bot])
            highVal = max(bots[bot])
            bots[bot] = []
            if lowParts[0] == "bot":
                giveToBot(lowDestNum, lowVal)
            elif lowParts[0] == "output":
                giveToOutput(lowDestNum, lowVal)
            if highParts[0] == "bot":
                giveToBot(highDestNum, highVal)
            elif highParts[0] == "output":
                giveToOutput(highDestNum, highVal)

solutionB = (sum(outputs[0]) * sum(outputs[1]) * sum(outputs[2]))
print solutionA
print solutionB
