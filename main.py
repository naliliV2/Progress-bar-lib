import time 
import os

def progress_bar(iteration, total, prefix="", suffix ="", decimal = 1, lenght = 100, fill='█', unfill='-'):
    """
    Call in a loop for create a progress bar.

    Requiere :
    iteration   -   Current iteration (Type : INT)
    total       -   Total iteration (Type : INT)
    
    Optional :
    prefix      -   Text before fill (Type : STR)           Default : ""
    suffix      -   Text after percent (Type : STR)         Default : ""
    decimal     -   Number of decimal (Type : INT)          Default : "1"
    lenght      -   Lenght of fill (Type : INT)             Default : "100"
    fill        -   The caractere of fill (Type : STR)      Default : '█'
    unfill      -   The caractere of unfill (Type : STR)    Default : '-'
    """
    size = os.get_terminal_size()
    if size.columns < (len(prefix)+len(suffix)+lenght+(4+decimal)+5):
        lenght = size.columns - (len(prefix) + len(suffix) + (4+decimal) + 5)
        if lenght <= 0:
            print("Error, the window is very too little for print a progress bar !")
            return "Window_little"
    
    if lenght == -1:
        lenght = size.columns - (len(prefix) + len(suffix) + (4+decimal) + 5)

    percent = round((iteration/total)*100, decimal)
    bar_filled = fill * int(round((iteration*lenght/total), 0))
    bar = bar_filled + unfill * (lenght-int(round((iteration*lenght/total), 0)))

    print(f"{prefix}|{bar}| {percent}% {suffix}", end="\r")
    if iteration == total:
        print()