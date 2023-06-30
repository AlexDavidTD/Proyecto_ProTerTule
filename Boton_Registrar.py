from tkinter import *; from tkinter import messagebox as mb; import pandas as pd; import customtkinter as ctk; import os; import sys

def Registrar(inputs, labels, Entalpia, EnergiaInt, CalorEsp, Densidad, ConductTerm, DifusTerm, Temperatura, Presión, Calidad, boton5):
    label_EntalR=labels[2];label_EinR=labels[3]; label_CpR=labels[4]; label_DenR=labels[5]; label_KR=labels[6]; label_AlpR=labels[7];\
        Temp=inputs[6]; Pres=inputs[7]; Calid=inputs[8]
    r= mb.askyesno("Registrar Datos", "¿Desea registrar estos datos, en la base de datos?")
    if r==YES:
        Entalpia.append(label_EntalR.cget("text")); EnergiaInt.append(label_EinR.cget("text")); CalorEsp.append(label_CpR.cget("text"));\
            Densidad.append(label_DenR.cget("text")); ConductTerm.append(label_KR.cget("text")); DifusTerm.append(label_AlpR.cget("text"));\
                Temperatura.append(Temp.get()); Presión.append(Pres.get()), Calidad.append(Calid.get())
        mb.showinfo("Datos Registrados", "Estos resultados han sido registrados\nen la base de datos, ¡Exitosamente!\n\nRecuerde guardar al finalizar")
        boton5.configure(state="disabled")
def Guardar(Entalpia, EnergiaInt, CalorEsp, Densidad, ConductTerm, DifusTerm, Temperatura, Presión, Calidad):
    r=mb.askyesno("Guardar Datos", "¿Desea guardar la base de datos en un archivo de Excel?")
    if r==YES:
        confirm=mb.askyesno("Exportar Archivo Excel", "¿Ya finalizó los cálculos?\n A continuación se exportarán los resultados\nque usted registró, a un archivo .XLSX")
        if confirm==YES:
            raiz2=ctk.CTk();raiz2.title("ProTerTule V6.0 - Exportar .XLSX");raiz2.geometry("300x150+20+20");raiz2.configure(padx=40, pady=20);raiz2.resizable(False,False)
            def resource_path(relative_path):
                try:
                    base_path = sys._MEIPASS
                except Exception:
                    base_path = os.path.abspath(".")
                return os.path.join(base_path, relative_path) 
            path=resource_path("icono.ico");raiz2.iconbitmap(path)
            input_nombre = ctk.CTkEntry(master=raiz2, font=("Lucida Fax", 14));input_nombre.grid(pady=5, column=0, row=1)
            label_nombre = ctk.CTkLabel(master=raiz2,text="Inserte el nombre del archivo", font=("Lucida Fax", 14));label_nombre.grid(column=0, row=0)
            def Guardar2():
                datos={'h':Entalpia, 'μ':EnergiaInt, 'Cp':CalorEsp,'ρ':Densidad, 'K':ConductTerm, 'α':DifusTerm, 'Temp°C':Temperatura, 'kPa':Presión, 'X':Calidad}
                mb.showinfo("Default", "Tu archivo se guardará en la ruta por defecto:\nCarpeta Raíz")
                nombre=str(input_nombre.get() + ".xlsx")
                archivo=pd.DataFrame(datos, columns=['h','μ','Cp','ρ','K','α', 'Temp°C', 'kPa', 'X'])
                archivo.to_excel(nombre, sheet_name="pag", engine="openpyxl")
                mb.showinfo("Ruta", "Tu archivo se gaurdó correctametne\n\nLo puedes encontrar en la ruta especificada:")
                sys.exit()
            boton= ctk.CTkButton(master=raiz2,text=("Guardar"), font=("Britannic Bold", 14), command=Guardar2);boton.grid(pady=5, column=0, row=5)
            raiz2.mainloop()
