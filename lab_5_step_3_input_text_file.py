import os

def open_input(file):
    with open(file, 'r') as f:
        text = f.read() #We use read() to read the actual contents of the file
        print(text)

def main():
    open_input(directory)

if __name__=="__main__":
    directory = (os.getcwd())
    directory += "/text.txt"
    main()
