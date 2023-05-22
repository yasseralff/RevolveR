from tkinter import *
import chapter.circular_motion.circular_motion as cm
import time

with open('chapter/circular_motion/circular.txt', 'r') as f:
    circular_keywords = [line.strip() for line in f.readlines()]

with open('chapter/circular_motion/force.txt', 'r') as f:
    force_keywords = [line.strip() for line in f.readlines()]

'''
UML Class Diagram
+-------------------------------+
|           RevolveRUI          |
+-------------------------------+
| - window: Tk                  |
| - dark_color_theme: {}        |
| - light_color_theme: {}       |
| - header_light: PhotoImage    |
| - header_dark: PhotoImage     |
| - icon_moon: PhotoImage       |
| - icon_sun: PhotoImage        |
| - top_centripetal: PhotoImage |
| - label: Label                |
| - header: Label               |
| - question: StringVar         |
| - question_entry: Entry       |
| - submit_bt: Button           |
| - answer: StringVar           |
| - answer_out: Label           |
| - theme_bt: Button            |
+-------------------------------+
| + __init__()                  |
| + solve()                     |
| + changetheme()               |
+-------------------------------+
'''


class RevolveRUI:
    def __init__(self):
        self.window = Tk()

        # Colors
        self.dark_color_theme = {1: "#0C134F", 2: "#1D267D", 3: "#5C469C", 4: "#D4ADFC"}
        self.light_color_theme = {1: "#A6D0DD", 2: "#FF6969", 3: "#FFD3B0", 4: "#FFF9DE"}

        x = int((self.window.winfo_screenwidth() / 2) - (400 / 2))
        y = int((self.window.winfo_screenheight() / 2) - (400 / 2))

        self.window.title('RevolveR')
        self.window.iconbitmap("./icon.ico")
        self.window.config(bg=self.dark_color_theme[2])
        self.window.geometry(f'400x400+{x}+{y}')
        self.window.resizable(False, True)

        # Photo assets
        self.header_light = PhotoImage(file='assets/header_light.png')
        self.header_dark = PhotoImage(file='assets/header_dark.png')
        self.icon_moon = PhotoImage(file='assets/icon_moon.png')
        self.icon_sun = PhotoImage(file='assets/icon_sun.png')
        self.top_centripetal = PhotoImage(file='assets/top_centripetal.png')

        # Header image
        self.label = Label(self.window,
                           image=self.header_dark,
                           bg=self.dark_color_theme[2])
        self.label.grid(row=0, column=0, columnspan=2)

        # Instruction
        self.header = Label(self.window,
                            text='Having problem with circular motion problems?\nWorry not! Just submit '
                                 'the question below and Voila!',
                            font="Segoe-UI-Variable-Text-Semibold 11 bold",
                            bg=self.dark_color_theme[2],
                            fg=self.dark_color_theme[4])
        self.header.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Entry for the question
        self.question = StringVar()
        self.question_entry = Entry(self.window,
                                    textvariable=self.question,
                                    width=30,
                                    font="Segoe-UI-Variable-Text-Semibold 11",
                                    bg=self.dark_color_theme[4],
                                    fg=self.dark_color_theme[3])
        self.question_entry.grid(row=2, column=0, padx=30, sticky='ew', columnspan=2)
        self.question_entry.insert(0, "Enter your question here")

        self.question_entry.bind('<Return>', self.solve)

        # Submit button
        self.submit_bt = Button(self.window,
                                text="Solve!",
                                command=self.solve,
                                bg=self.dark_color_theme[4],
                                fg=self.dark_color_theme[2],
                                font="Segoe-UI-Variable-Text-Semibold 11 bold")
        self.submit_bt.grid(row=3, column=0, columnspan=2, sticky=N, padx=50, pady=5)

        # Answer output
        self.answer = StringVar()
        self.answer.set("Your answer's here")
        self.answer_out = Label(self.window,
                                textvariable=self.answer,
                                bg=self.dark_color_theme[4],
                                fg=self.dark_color_theme[3],
                                font="Segoe-UI-Variable-Text-Semibold 11")
        self.answer_out.grid(row=4, column=0, columnspan=2, padx=10, sticky=N, pady=50)

        # "Copyright"
        self.copyright = Label(self.window,
                               text="Made by Miqdad Yasser Al-Fafa",
                               bg=self.dark_color_theme[2],
                               fg=self.dark_color_theme[4])
        self.copyright.grid(row=5, column=0, columnspan=2, pady=0)

        # Switch theme button
        self.theme_bt = Button(self.window,
                               image=self.icon_sun,
                               command=self.changetheme,
                               bg=self.dark_color_theme[4])
        self.theme_bt.grid(row=5, column=1, padx=5, sticky="NE", pady=5)

        # Configure grid weights and resizing behavior
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_rowconfigure(2, weight=1)
        self.window.grid_rowconfigure(3, weight=1)

        self.window.mainloop()

    # Method to solve the question
    def solve(self, event=None):
        problem_statement = self.question.get()
        am = cm.CircularMotion(circular_keywords, force_keywords)
        solution = am.solve_physics_problem(problem_statement)
        self.answer.set(solution)
        print(problem_statement)
        print(solution)

        time.sleep(1)
        self.toplevel()

    def toplevel(self):
        top = Toplevel()
        top.title("Formula")
        top.iconbitmap("./icon.ico")
        formula = Label(top, image=self.top_centripetal)
        formula.pack(padx=10, pady=10)

    # A method to change the color (theme)
    def changetheme(self):
        current_image = self.theme_bt.cget('image')
        if current_image == 'pyimage4':
            self.window.config(bg=self.light_color_theme[3])
            self.label.config(bg=self.light_color_theme[1], image=self.header_light)
            self.header.config(bg=self.light_color_theme[3], fg=self.light_color_theme[2])
            self.question_entry.config(bg=self.light_color_theme[4], fg=self.light_color_theme[2])
            self.submit_bt.config(bg=self.light_color_theme[1], fg=self.light_color_theme[2])
            self.answer_out.config(bg=self.light_color_theme[4], fg=self.light_color_theme[2])
            self.copyright.config(bg=self.light_color_theme[3], fg=self.light_color_theme[2])
            self.theme_bt.config(bg=self.light_color_theme[1], image=self.icon_moon)
        else:
            self.window.config(bg=self.dark_color_theme[2])
            self.label.config(bg=self.dark_color_theme[2], image=self.header_dark)
            self.header.config(bg=self.dark_color_theme[2], fg=self.dark_color_theme[4])
            self.question_entry.config(bg=self.dark_color_theme[4], fg=self.dark_color_theme[3])
            self.submit_bt.config(bg=self.dark_color_theme[4], fg=self.dark_color_theme[2])
            self.answer_out.config(bg=self.dark_color_theme[4], fg=self.dark_color_theme[3])
            self.copyright.config(bg=self.dark_color_theme[2], fg=self.dark_color_theme[4])
            self.theme_bt.config(bg=self.dark_color_theme[4], image=self.icon_sun)

# RevolveRUI()
