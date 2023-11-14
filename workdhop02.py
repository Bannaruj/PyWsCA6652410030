import random

def guess_number():
    target_number = random.randint(1, 100)

    while True:
        try:
            user_guess = int(input("ทายตัวเลข (1-100): "))

            if user_guess == target_number:
                print("ยินดีด้วยคุณทายถูก!")
                break
            elif user_guess < target_number:
                print("คุณทายผิด ตัวเลขที่ป้อนน้อยไป")
            else:
                print("คุณทายผิด ตัวเลขที่ป้อนมากไป")

        except ValueError:
            print("โปรดป้อนตัวเลขที่ถูกต้อง")

if __name__ == "__main__":
    guess_number()