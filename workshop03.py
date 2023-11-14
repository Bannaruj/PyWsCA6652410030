import math

def rectangle_area(width, length):
    return width * length

def circle_area(radius):
    return math.pi * radius**2

def rectangle_volume(width, length, height):
    return width * length * height

def circle_volume(radius):
    return (4/3) * math.pi * radius**3

def menu():
    print("************************************************ AREA & CUBE ************************************************")
    print("1. พื้นที่สี่เหลี่ยม  2. พื้นที่วงกลม  3. ปริมาตรทรงสี่เหลี่ยม  4. ปริมาตรทรงกลม  0. ออกจากการทำงาน")
    print("******************************************************************************************************")

def main():
    while True:
        menu()
        try:
            choice = input("เลือกเมนู : ")

            if choice == '1':
                width = float(input("ป้อนความกว้าง : "))
                length = float(input("ป้อนความยาว : "))
                print(f"พื้นที่สี่เหลี่ยมที่คำนวณได้คือ: {rectangle_area(width, length):.2f}")
            elif choice == '2':
                radius = float(input("ป้อนรัศมี : "))
                print(f"พื้นที่วงกลมที่คำนวณได้คือ: {circle_area(radius):.2f}")
            elif choice == '3':
                width = float(input("ป้อนความกว้าง : "))
                length = float(input("ป้อนความยาว : "))
                height = float(input("ป้อนความสูง : "))
                print(f"ปริมาตรทรงสี่เหลี่ยมที่คำนวณได้คือ: {rectangle_volume(width, length, height):.2f}")
            elif choice == '4':
                radius = float(input("ป้อนรัศมี : "))
                print(f"ปริมาตรทรงกลมที่คำนวณได้คือ: {circle_volume(radius):.2f}")
            elif choice == '0':
                print("ออกจากการทำงาน")
                break
            else:
                print("กรุณาเลือกเมนู 1, 2, 3, 4 หรือ 0 เท่านั้น")
        except ValueError :
            print("กรุณาป้อนเลข:")
if __name__ == "__main__":
    main()