import random

def guess(num, ans):
    if 0 < num < 11:
        if num == ans:
            print('you are a genius')
            return True
    else:
        print("hey bozo, I said 1~10")
        return False


if __name__ == "__main__":

    answer = random.randint(1, 10)
    while True:
        try:
            guessed = int(input("guess a number 1~10:\t"))
            if guess(guessed, answer):
                break

        except ValueError:
            print("please enter a number")
            continue
