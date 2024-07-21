import customtkinter as ctk

class Button(ctk.CTkButton):

    def __init__(self, parent, text, command=None):
        super().__init__(master=parent, text=text, command=command)
        self.configure(fg_color="#5e2f6f", hover_color="#7b3781", text_color="white", font=("OCR A Extended", 12, "bold"))
    
    def on_button_click(self):
        return False
    