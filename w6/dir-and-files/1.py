import os
def printContent(level, path):
    for x in os.listdir(path):
        for i in range(level + 1):
            print(' '*5,end='')
        print(x)
        if os.path.isdir(path + "/" + x):
            printContent(level + 1, path + "/" + x)


printContent(0, "c:\\Users\\orazg\\OneDrive\\Рабочий стол\\pp2_2022_spring")