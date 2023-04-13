import os

if __name__ == '__main__':
    print("Welocome to Robospeaker . Created by Khalid Rehman")
    while True:
        x = input("Enter what are you want to speak: ")
        if x == "q":
            os.system("say 'bye bye friends'")
            break
        command = f"Say this {x}"
        os.system(command)

