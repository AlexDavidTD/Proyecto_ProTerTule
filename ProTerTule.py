import webbrowser; import customtkinter as ctk; from tkinter import messagebox as mb; import sys; import os;\
    from Boton_Nuevo import *; from Boton_Calcular import *; from Boton_Registrar import *
def Calcular():
    Calculo(inputs, labels, mezcla)
    boton5.configure(state="normal")
def Nuevo():
    restart(inputs, labels, Combo_Mezcla)
def Salir():
    salir=mb.askyesno("Salir","¿Desea salir del programa?")
    if salir==YES:
        sys.exit()
def about():
    r=mb.askyesno("Acerca de", "Para más información\nserá redirigido al repositorio publico de GitHub\ndonde está toda la información del programa")
    if r == YES:
        webbrowser.open('https://github.com/AlexDavidTD/Proyecto_ProTerTule')
Entalpia=[]; EnergiaInt=[]; CalorEsp=[]; Densidad=[]; ConductTerm=[]; DifusTerm =[];Temperatura=[]; Presión=[]; Calidad=[]
def Registro():
    Registrar(inputs, labels, Entalpia, EnergiaInt, CalorEsp, Densidad, ConductTerm, DifusTerm, Temperatura, Presión, Calidad, boton5)
def Guardado():
    Guardar(Entalpia, EnergiaInt, CalorEsp, Densidad, ConductTerm, DifusTerm, Temperatura, Presión, Calidad)
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path) 
ctk.set_appearance_mode("light");ctk.set_default_color_theme("dark-blue")
raiz=ctk.CTk();raiz.title("ProTerTule V6.0");raiz.geometry("1180x620+100+30");raiz.configure(padx=40, pady=20);raiz.resizable(False,False)
path=resource_path("icono.ico");raiz.iconbitmap(path); Canvas = ctk.CTkCanvas(width=380, height=170);path2 = resource_path("logo-udea-ingenieria.png")
logo_img2 = PhotoImage(file=path2);Canvas.create_image(190, 85, image=logo_img2);Canvas.grid(column=1, row=0), Canvas.configure(bg="white smoke")
Canvas2 = ctk.CTkCanvas(width=150, height=150); path2 = resource_path("temperatura.png"); logo_img = PhotoImage(file=path2)
Canvas2.create_image(75, 75, image=logo_img); Canvas2.grid(column=3, row=0); Canvas2.config(bg='white smoke')
input1_Min = ctk.CTkEntry(master=raiz, font=("Lucida Fax", 14));input1_Min.insert(END, string="0");input1_Min.grid(pady=1, column=1, row=2);input1_Min.configure(state="disabled")
label1_Min = ctk.CTkLabel(master=raiz,text="Minerales %", font=("Lucida Fax", 14));label1_Min.grid(column=0, row=2)
input2_Pro = ctk.CTkEntry(master=raiz, font=("Lucida Fax", 14));input2_Pro.insert(END, string="0");input2_Pro.grid(pady=1, column=1, row=3);input2_Pro.configure(state="disabled")
label2_Pro = ctk.CTkLabel(master=raiz,text="Proteina %", font=("Lucida Fax", 14));label2_Pro.grid(column=0, row=3)
input3_Fib = ctk.CTkEntry(master=raiz, font=("Lucida Fax", 14));input3_Fib.insert(END, string="0");input3_Fib.grid(pady=1, column=1, row=4);input3_Fib.configure(state="disabled")
label3_Fib = ctk.CTkLabel(master=raiz,text="Fibra %", font=("Lucida Fax", 14) );label3_Fib.grid(column=0, row=4)
input4_Car = ctk.CTkEntry(master=raiz, font=("Lucida Fax", 14));input4_Car.insert(END, string="0");input4_Car.grid(pady=1, column=1, row=5);input4_Car.configure(state="disabled")
label4_Car = ctk.CTkLabel(master=raiz,text="Carbohidratos %", font=("Lucida Fax", 14));label4_Car.grid(column=0, row=5)
input5_Agu = ctk.CTkEntry(master=raiz,font=("Lucida Fax", 14));input5_Agu.insert(END, string="0");input5_Agu.grid(pady=1, column=1, row=6);input5_Agu.configure(state="disabled")
label5_Agu = ctk.CTkLabel(master=raiz,text="H2O %", font=("Lucida Fax", 14));label5_Agu.grid(column=0, row=6)
input6_Gra = ctk.CTkEntry(master=raiz, font=("Lucida Fax", 14));input6_Gra.insert(END, string="0");input6_Gra.grid(pady=1, column=1, row=7);input6_Gra.configure(state="disabled")
label6_Gra = ctk.CTkLabel(master=raiz,text="Grasa %", font=("Lucida Fax", 14));label6_Gra.grid(column=0, row=7)
input7_Tem = ctk.CTkEntry(master=raiz, font=("Lucida Fax", 14));input7_Tem.insert(END, string="0");input7_Tem.grid(pady=1, column=1, row=8);input7_Tem.configure(state="disabled")
label7_Tem = ctk.CTkLabel(master=raiz,text="Tempratura [°C]", font=("Lucida Fax", 14));label7_Tem.grid(column=0, row=8)
input8_Pres = ctk.CTkEntry(master=raiz, font=("Lucida Fax", 14));input8_Pres.insert(END, string="0");input8_Pres.grid(pady=1, column=1, row=9);input8_Pres.configure(state="disabled")
label8_Pres = ctk.CTkLabel(master=raiz,text="Presión [KPa]", font=("Lucida Fax", 14));label8_Pres.grid(column=0, row=9)
input9_Calid = ctk.CTkEntry(master=raiz, font=("Lucida Fax", 14));input9_Calid.insert(END, string="0");input9_Calid.grid(pady=1, column=1, row=10);input9_Calid.configure(state="disabled")
label9_Calid = ctk.CTkLabel(master=raiz,text="Calidad de Vapor", font=("Lucida Fax", 14));label9_Calid.grid(pady=1, column=0, row=10)
label_creditos5= ctk.CTkLabel(master=raiz,text="ProTerTule\nDesarrollado por:\nAlex Torres D. y Oscar Ruíz P.\nIng. Agroindustrial\nUniversidad de Antioquia\nseccional Urabá",\
    font=("Lucida Calligraphy", 14));label_creditos5.grid(padx=30,column=2, row=0)
label_Space = ctk.CTkLabel(master=raiz,text="%-------------------------------------%", font=("Algerian", 16) );label_Space.grid(column=1, row=1)
label_Space2 = ctk.CTkLabel(master=raiz,text="%-------------------------------------%", font=("Algerian", 16));label_Space2.grid(column=1, row=14)
label_Ental = ctk.CTkLabel(master=raiz,text="Entalpia (h) =", font=("Lucida Fax", 14));label_Ental.grid(column=2, row=2)
label_EntalR = ctk.CTkLabel(master=raiz,text="     0     ", font=("Lucida Fax", 14));label_EntalR.grid(padx= 10,column=3, row=2)
label_EntalU = ctk.CTkLabel(master=raiz,text="kJ/Mol", font=("Lucida Fax", 14));label_EntalU.grid(column=4, row=2)
label_Ein = ctk.CTkLabel(master=raiz,text="Energia interna (μ) =", font=("Lucida Fax", 14));label_Ein.grid(column=2, row=3)
label_EinR = ctk.CTkLabel(master=raiz,text="     0     ", font=("Lucida Fax", 14));label_EinR.grid(padx= 10,column=3, row=3)
label_EinU = ctk.CTkLabel(master=raiz,text="kJ/Mol", font=("Lucida Fax", 14));label_EinU.grid(column=4, row=3)
label_Cp = ctk.CTkLabel(master=raiz,text="Calor Específico (Cp) =", font=("Lucida Fax", 14));label_Cp.grid(column=2, row=4)
label_CpR = ctk.CTkLabel(master=raiz,text="     0     ", font=("Lucida Fax", 14));label_CpR.grid(padx= 10,column=3, row=4)
label_CpU = ctk.CTkLabel(master=raiz,text="kJ/Kg*°C", font=("Lucida Fax", 14));label_CpU.grid(column=4, row=4)
label_Den = ctk.CTkLabel(master=raiz,text="Densidad (ρ) =", font=("Lucida Fax", 14));label_Den.grid(column=2, row=5)
label_DenR = ctk.CTkLabel(master=raiz,text="     0     ", font=("Lucida Fax", 14) );label_DenR.grid(padx= 10,column=3, row=5)
label_DenU = ctk.CTkLabel(master=raiz,text="Kg/m^3", font=("Lucida Fax", 14));label_DenU.grid(column=4, row=5)
label_K = ctk.CTkLabel(master=raiz,text="Conductividad Térmica (K) =", font=("Lucida Fax", 14));label_K.grid(column=2, row=6)
label_KR = ctk.CTkLabel(master=raiz,text="     0     ", font=("Lucida Fax", 14));label_KR.grid(padx= 10,column=3, row=6)
label_KU = ctk.CTkLabel(master=raiz,text="kJ/s*m*°C", font=("Lucida Fax", 14));label_KU.grid(column=4, row=6)
label_Alp = ctk.CTkLabel(master=raiz,text="Difusividad Térmica (α) =", font=("Lucida Fax", 14));label_Alp.grid(column=2, row=7)
label_AlpR = ctk.CTkLabel(master=raiz,text="     0     ", font=("Lucida Fax", 14));label_AlpR.grid(padx= 10,column=3, row=7)
label_AlpU = ctk.CTkLabel(master=raiz,text="m^2/s", font=("Lucida Fax", 14));label_AlpU.grid(column=4, row=7)
def Elegir(choise):
    def mensaje_liquido():
        mb.showinfo("Información","Para realizar este cálculo, es necesario que ingrese:\n\nComposición [%]\nTemperatura de ebullición [°C]\nPresión de saturación [kPa]\nCaldiad de vapor [0 < X <= 0.85]\n\nPresione 'Aceptar' para continuar" )
    def mensaje_azucar():
        mb.showinfo("Información","Para realizar este cálculo, es necesario que ingrese:\n\nComposición [%]\nTemperatura [°C]\n\nPresione 'Aceptar' para continuar" )
    def cambio():
        label7_Tem.configure(text="Tempratura Ebu. [°C]",);
        label8_Pres.configure(text="Presión Sat. [KPa]",)
        label_Ental.configure(text="Entalpia Vap. (hv) =",)
    def cambio2():
        label7_Tem.configure(text="Tempratura [°C]",)
        label8_Pres.configure(text="Presión [KPa]",)
        label_Ental.configure(text="Entalpia (h) =",)
    def entradas_azu():
        input1_Min.delete(0, END);input1_Min.insert(END, string="0");input1_Min.configure(state="disabled")
        input2_Pro.delete(0, END);input2_Pro.insert(END, string="0");input2_Pro.configure(state="disabled")
        input3_Fib.delete(0, END);input3_Fib.insert(END, string="0");input3_Fib.configure(state="disabled")
        input6_Gra.delete(0, END);input6_Gra.insert(END, string="0");input6_Gra.configure(state="disabled")
        input4_Car.configure(state="normal")
        input5_Agu.configure(state="normal")
        input7_Tem.configure(state="normal")
        input8_Pres.configure(state="normal")
        input9_Calid.configure(state="normal")
    def entrada_liq_Sat():
        input1_Min.configure(state="normal")
        input2_Pro.configure(state="normal")
        input3_Fib.configure(state="normal")
        input4_Car.configure(state="normal")
        input5_Agu.configure(state="normal")
        input6_Gra.configure(state="normal")
        input7_Tem.configure(state="normal")
        input8_Pres.delete(0, END);input8_Pres.insert(END, string="0");input8_Pres.configure(state="disabled")
        input9_Calid.delete(0, END);input9_Calid.insert(END, string="0");input9_Calid.configure(state="disabled")
    def restart():
        input1_Min.delete(0, END);input1_Min.insert(END, string="0");input1_Min.configure(state="disabled")
        input2_Pro.delete(0, END);input2_Pro.insert(END, string="0");input2_Pro.configure(state="disabled")
        input3_Fib.delete(0, END);input3_Fib.insert(END, string="0");input3_Fib.configure(state="disabled")
        input4_Car.delete(0, END);input4_Car.insert(END, string="0");input4_Car.configure(state="disabled")
        input5_Agu.delete(0, END);input5_Agu.insert(END, string="0");input5_Agu.configure(state="disabled")
        input6_Gra.delete(0, END);input6_Gra.insert(END, string="0");input6_Gra.configure(state="disabled")
        input7_Tem.delete(0, END);input7_Tem.insert(END, string="0");input7_Tem.configure(state="disabled")
        input8_Pres.delete(0, END);input8_Pres.insert(END, string="0");input8_Pres.configure(state="disabled")
        input9_Calid.delete(0, END);input9_Calid.insert(END, string="0");input9_Calid.configure(state="disabled")
    Slc = mezcla.get()
    if Slc == 'Seleccione una opción':
        cambio2();restart();mensaje_liquido()
    elif Slc == 'Sacarosa':
        cambio();entradas_azu();mensaje_liquido()
    elif Slc == 'Azúcares reductores':
        cambio();entradas_azu();mensaje_liquido()
    elif Slc == 'Jugo de frutas':
        cambio();entradas_azu();mensaje_liquido()
    elif Slc == 'Extracto de café':
        cambio();entradas_azu();mensaje_liquido()
    elif Slc == 'Jugo de manzana':
        cambio();entradas_azu();mensaje_liquido()
    elif Slc == 'Soluciones de azucar':
        cambio();entradas_azu();mensaje_liquido()
    elif Slc == 'Liquido Saturado (Sub-enfriado)':
        cambio2();entrada_liq_Sat();mensaje_azucar()
label_Space4 = ctk.CTkLabel(master=raiz,text="Tipo de Mezcla", font=("Lucida Fax", 14));label_Space4.grid(column=0, row=12)
mezcla=ctk.StringVar(value="Seleccione una opción")
Combo_Mezcla = ctk.CTkComboBox(master=raiz,font=("Constantia", 14),state="readonly",values=["Seleccione una opción","Sacarosa", "Azúcares reductores",\
    "Jugo de frutas", "Extracto de café", "Jugo de manzana", "Soluciones de azucar", "Liquido Saturado (Sub-enfriado)"], command=Elegir, variable=mezcla);Combo_Mezcla.grid(column=0, row=13)
inputs=[input1_Min, input2_Pro, input3_Fib, input4_Car, input5_Agu, input6_Gra, input7_Tem, input8_Pres, input9_Calid]
labels=[label_Space, label_Space2, label_EntalR, label_EinR, label_CpR, label_DenR, label_KR, label_AlpR, label7_Tem, label8_Pres, label_Ental]
boton = ctk.CTkButton(master=raiz,text=("Calcular"), font=("Britannic Bold", 16), command=Calcular);boton.grid(padx=5, pady=10, column=1, row=12)
boton2 = ctk.CTkButton(master=raiz,text=("Nuevo"), font=("Britannic Bold", 16), command=Nuevo);boton2.grid(column=1, row=13)
boton3 = ctk.CTkButton(master=raiz,text=("Salir"),font=("Lucida Calligraphy", 14), command=Salir);boton3.grid(column=3, row=14)
boton4 = ctk.CTkButton(master=raiz, text=("About"),font=("Lucida Calligraphy", 14), command=about);boton4.grid(padx=10, column=4, row=14)
boton5 = ctk.CTkButton(master=raiz,text=("Registrar"), font=("Britannic Bold", 16), command=Registro);boton5.grid(column=2, row=9)
boton6 = ctk.CTkButton(master=raiz,text=("Guardar"), font=("Britannic Bold", 16), command=Guardado);boton6.grid(column=2, row=10)
def cambiar_tema(choice):
    tema=Cmb_tema.get()
    if tema=='Dark':
        respuesta=mb.askyesno("Modo Oscuro","Se cambiará la interfáz a modo Oscuro\n¿Quiere continuar?")
        if respuesta==YES:
            Canvas.configure(bg="gray10")
            Canvas2.configure(bg="gray10")
            ctk.set_appearance_mode("dark")
    if tema=='Light':
        respuesta2=mb.askyesno("Modo Claro","Se cambiará la interfáz a modo Claro\n¿Quiere continuar?")
        if respuesta2==YES:
            Canvas.configure(bg="white smoke")
            Canvas2.configure(bg="white smoke")
            ctk.set_appearance_mode("light")
Cmb_tema=ctk.StringVar(value="Elige Tema")
tema=ctk.CTkComboBox(master=raiz,font=("Lucida Calligraphy", 14),state="readonly",values=["Dark", "Light"], command=cambiar_tema\
    ,variable=Cmb_tema);tema.grid(column=2, row=14)
label_Tema = ctk.CTkLabel(master=raiz,text="Tema",font=("Lucida Calligraphy", 14));label_Tema.grid(column=2, row=13)
raiz.mainloop()