import tkinter.font as tkfont

class FontManager:
    def __init__(self):
        self.title_font = tkfont.Font(family="Times New Roman", size=10, weight="bold")
        self.label_font = tkfont.Font(family="Times New Roman", size=10)
        self.button_font = tkfont.Font(family="Times New Roman", size=10, weight="bold")
        self.text_font = tkfont.Font(family="Times New Roman", size=10)

    def get_title_font(self):
        return self.title_font

    def get_label_font(self):
        return self.label_font

    def get_button_font(self):
        return self.button_font

    def get_text_font(self):
        return self.text_font