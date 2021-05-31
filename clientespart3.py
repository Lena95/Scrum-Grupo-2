bg = "#808080",
fg = "#363636",
activebackground= '#A9A9A9',
activeforeground= '#363636',
font = ("verdana", "10"),
command = self.insere_cliente
)
self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.1)

# Botão Alterar
self.bt_alterar = Button(self.aba1, text="Alterar", bd = 2, bg = "#808080", fg = "#363636",
    activebackground= '#A9A9A9', activeforeground='#363636',
    font = ("verdana", "10"), command = self.altera_cliente)
self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.1)


# Botão Apagar
self.bt_apagar = Button(self.aba1, text="Apagar", bd = 2, bg = "#808080", fg = "#363636",
    activebackground = '#A9A9A9', activeforeground = '#363636',
    font = ("verdana", "10"), command = self.deleta_cliente)
self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.1)

# Criação da Label e Entrada do Código
self.lb_codigo =  Label(self.aba1, text = "Código", bg="3636360", fg = "#808080", font = ("trebouchet", "10"))
self.lb_codigo.place(relx = 0.008, rely = 0.02)

self.codigo_entry = Entry(self.aba1, validate="key", validatecommand=self.vcmd2)
self.codigo_entry.place(relx = 0.008, rely = 0.11, relwidth= 0.07, relheight= 0.08)

# Criação da Label e Entrada do Nome
self.lb_nome = Label(self.aba1, text="Nome", bg="#363636", fg= "808080", font = ("trebouchet", 10))