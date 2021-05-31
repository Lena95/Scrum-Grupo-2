def frames_da_tela(self):
    self.frame_1 = Frame(
        self.root,
        bd = 4,  # Borda
        bg = "#363636",  # Cor de fundo (background color)
        highlightbackground = "#836FFF",
        highlightthickness = 1)
    self.frame_1.place(
        relx = 0.01,
        rely = 0.02,
        relwidth = 0.98,
        relheight = 0.46)
    self.frame_2 = Frame(
        self.root,
        bd = 4,
        bg = "#363636",
        highlightbackground = "#836FFF",
        highlightthickness = 1)
    self.frame_2.place(
        relx=0.01,
        rely=0, 5,
        relwidth=0.98,
        relheight=0.46)
def widgets-frame1(self):
    # Abas
    self.abas = ttk.Notebook(self.frame_1)
    self.aba1 = Frame(self.abas)
    self.aba2 = Frame(self.abas)