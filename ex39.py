x = int(input("Write level sound: "))

if x < 40:
    print("Level of sound is quieter than quiet room")
elif x == 40:
    print("Level of sound in quiet room")
elif 40 < x < 70:
    print("Level of sound between quiet room and alarm clock")
elif x == 70:
    print("Level of sound of alarm clock")
elif 70 < x < 106:
    print("Level of sound between alarm clock and gas lawnmower")
elif x == 106:
    print("Level of sound of gas lawnmower")
elif 106 < x < 130:
    print("Level of sound between gas lawnmower and jackhammer")
elif x == 130:
    print("Level of sound of jackhammer")
elif x > 130:
    print("Level of sound is louder than jackhammer")
