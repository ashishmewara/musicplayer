from pygame import mixer

def play_music(file_path):
    mixer.init()
    mixer.music.load(file_path)
    mixer.music.play()

def pause_music():
    mixer.music.pause()

def resume_music():
    mixer.music.unpause()

def stop_music():
    mixer.music.stop()

def main():
    while True:
        print("1. Play")
        print("2. Pause")
        print("3. Resume")
        print("4. Stop")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            file_path = input("Enter the path of the music file: ")
            play_music(file_path)
        elif choice == "2":
            pause_music()
        elif choice == "3":
            resume_music()
        elif choice == "4":
            stop_music()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
