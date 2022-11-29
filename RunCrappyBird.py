import os
import webbrowser

def main():
    '''Run both game and website one after the other
    '''
    os.system("python CrappyBird.py")
    webbrowser.open("http://127.0.0.1:5000")
    os.system("python app.py")

if __name__ == "__main__":
    main()