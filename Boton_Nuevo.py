from tkinter import *; from tkinter import messagebox as mb
def restart(inputs, labels, Combo_Mezcla):
    def borrar_todo():
        input1_Min=inputs[0];input1_Min.delete(0, END);input1_Min.insert(END, string="0");input1_Min.configure(state="disable");
        input2_Pro=inputs[1];input2_Pro.delete(0, END);input2_Pro.insert(END, string="0");input2_Pro.configure(state="disable");
        input3_Fib=inputs[2];input3_Fib.delete(0, END);input3_Fib.insert(END, string="0");input3_Fib.configure(state="disable");
        input4_Car=inputs[3];input4_Car.delete(0, END);input4_Car.insert(END, string="0");input4_Car.configure(state="disable");
        input5_Agu=inputs[4];input5_Agu.delete(0, END);input5_Agu.insert(END, string="0");input5_Agu.configure(state="disable");
        input6_Gra=inputs[5];input6_Gra.delete(0, END);input6_Gra.insert(END, string="0");input6_Gra.configure(state="disable");
        input7_Tem=inputs[6];input7_Tem.delete(0, END);input7_Tem.insert(END, string="0");input7_Tem.configure(state="disable");
        input8_Pres=inputs[7];input8_Pres.delete(0, END);input8_Pres.insert(END, string="0");input8_Pres.configure(state="disable");
        input9_Calid=inputs[8];input9_Calid.delete(0, END);input9_Calid.insert(END, string="0");input9_Calid.configure(state="disable");
        label_Space=labels[0];label_Space.configure(text="%-------------------------------------%", font=("Algerian", 16))
        label_Space2=labels[1];label_Space2.configure(text="%-------------------------------------%", font=("Algerian", 16))
        label_EntalR=labels[2];label_EntalR.configure(text="     0     ")
        label_EinR=labels[3];label_EinR.configure(text="     0     ")
        label_CpR=labels[4];label_CpR.configure(text="     0     ")
        label_DenR=labels[5];label_DenR.configure(text="     0     ")
        label_KR=labels[6];label_KR.configure(text="     0     ")
        label_AlpR=labels[7];label_AlpR.configure(text="     0     ")
        label7_Tem=labels[8];label7_Tem.configure(text="Tempratura [°C]")
        label8_Pres=labels[9];label8_Pres.configure(text="Presión [KPa]")
        Combo_Mezcla.set("Seleccione una opción")    
    respuesta=mb.askyesno("Nuevo Cálculo","¡CUIDADO!\nLos últimos resultados obtenidos se perderán\n¿Desea realizar un nuevo cálculo?")
    if respuesta==YES:
        borrar_todo()