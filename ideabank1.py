import  sys


if  "--list" not in sys.argv:
    idea = input("Write your idea here: " )

    filename = open("ideas.txt", "a")
    filename.write(idea)
    filename.write( "\n")
    filename.close()

filename = open("ideas.txt" , "r")
print(filename.read())
