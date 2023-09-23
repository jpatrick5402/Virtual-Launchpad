import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.button = customtkinter.CTkButton(
            self, text="my button", command=self.button_callbck0, height=50)
        self.button.grid(padx=20, pady=20, row=0, column=0)

        self.button = customtkinter.CTkButton(
            self, text="my button", command=self.button_callbck1, height=50)
        self.button.grid(padx=20, pady=20, row=0, column=1)

        self.button = customtkinter.CTkButton(
            self, text="my button", command=self.button_callbck2, height=50)
        self.button.grid(padx=20, pady=20, row=0, column=2)

        self.button = customtkinter.CTkButton(
            self, text="my button", command=self.button_callbck3, height=50)
        self.button.grid(padx=20, pady=20, row=1, column=0)

        self.button = customtkinter.CTkButton(
            self, text="my button", command=self.button_callbck4, height=50)
        self.button.grid(padx=20, pady=20, row=1, column=1)

        self.button = customtkinter.CTkButton(
            self, text="my button", command=self.button_callbck4, height=50)
        self.button.grid(padx=20, pady=20, row=1, column=2)

    def button_callbck0(self):
        print("button clicked")

    def button_callbck1(self):
        print("button clicked")

    def button_callbck2(self):
        print("button clicked")

    def button_callbck3(self):
        print("button clicked")

    def button_callbck4(self):
        print("button clicked")


app = App()
app.mainloop()
