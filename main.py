import os

class progress_bar():
    def create(iteration, total, prefix="", suffix ="", decimal = 1, lenght = 100, fill='█', unfill='-'):
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
        parameter = progress_bar()
        size = os.get_terminal_size()
        
        if parameter.percentage == True:
            percent = f" {round((iteration/total)*100, decimal)} %"
        else:
            percent = ""

        if parameter.percentage_number == True:
            number_percent = f" {iteration}/{total} " 
        else:
            number_percent = ""

        # Lenght
        if lenght == -1:
            lenght = size.columns - (len(prefix) + len(suffix) + (4+decimal) + 5)
        if size.columns < (len(prefix) + lenght + len(suffix) + len(percent) + len(number_percent) + 5):
            lenght = size.columns - (len(prefix) + len(suffix) + len(percent) + len(number_percent) + 5)
        if lenght <= 0:
            print("Error, the window is very too little for print a progress bar !")
            return "Window_little"
        
        bar_filled = fill * int(round((iteration*lenght/total), 0))
        bar = bar_filled + unfill * (lenght-int(round((iteration*lenght/total), 0)))

        print(f"{prefix} |{bar}|{percent}{number_percent}{suffix}", end="\r")
        if iteration == total:
            print()

    def percentage(self, input):
        """
        Define if print a % number. (Default : False)

        Example :
            progress_bar.percentage = True
        """
        if type(input) == bool:
            self.percentage == input
        else: 
            print('Error, the input is not as bool')

    def percentage_number(self, input):
        """
        Define if print a raw % number (Default : False)

        Example :
            progress_bar.percentage_number = True
        """
        if type(input) == bool:
            self.percentage_number == input
        else: 
            print('Error, the input is not as bool')