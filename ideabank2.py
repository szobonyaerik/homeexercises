import  sys


if  "--delete" not in sys.argv:
    idea = input("Write your idea here: " )

    filename = open("ideas.txt", "a")
    filename.write(idea)
    filename.write( "\n")
    filename.close()

    filename = open("ideas.txt" , "r")
    print(filename.read())
elif "--delete" in sys.argv:
    i = sys.argv.index("--delete")
    j = (int(sys.argv[i + 1]) -1)
    kill = open("ideas.txt", "r").readlines()
    with open("ideas.txt", "w") as z:
        for index,line in enumerate(kill):
            if index != j:
                z.write(line)
