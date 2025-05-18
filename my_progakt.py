from customtkinter import*
class MainWindow(CTk)
    def __init__(self):
        super().__init__()
        self.geometry("400X300")

        self.frame= CTkFrame(self, fg_color='light blue', width=200, hight=self.winfo_height())
        self.frame.pack_propagate(Ealse)
        self.frame.configure(wight=0)
        self.frame.place(x=0, y=0)
        self.is_show_menu = False
        self.frame_wight = 0

        self.label = CTkLabel(self.frame, text='Ваше Імя')
        self