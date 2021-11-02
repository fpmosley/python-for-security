from random import randrange


def main():
    dice = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    dice_roll_res(dice)


def dice_rolling():
    rolls = int(input("Times to roll the dice: "))
    print("Rolling the dice")
    return rolls


def dice_roll_res(dice):
    for i in range(dice_rolling()):
        roll_res = randrange(1, 7)
        dice[roll_res] += 1
    print(dice)


main()
