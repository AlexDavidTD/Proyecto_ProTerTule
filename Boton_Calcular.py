from tkinter import *; import math as ma; from tkinter import messagebox as mb
def Calculo(inputs, labels, mezcla):
    Azucar=mezcla.get();input1_Min=inputs[0];input2_Pro=inputs[1];input3_Fib=inputs[2];input4_Car=inputs[3];input5_Agu=inputs[4];\
        input6_Gra=inputs[5];input7_Tem=inputs[6];input8_Pres=inputs[7];input9_Calid=inputs[8];label_Space=labels[0];\
            label_Space2=labels[1];label_EntalR=labels[2];label_EinR=labels[3];label_CpR=labels[4];label_DenR=labels[5];\
                label_KR=labels[6];label_AlpR=labels[7];chos=float(input1_Min.get());proteina=float(input2_Pro.get());\
                    fibra=float(input3_Fib.get());carboh=float(input4_Car.get());h2o=float(input5_Agu.get());lipido=float(input6_Gra.get())
    if chos<0 or chos>1 or proteina<0 or proteina>1 or fibra<0 or fibra>1 or carboh<0 or carboh>1 or h2o<0 or h2o>1 or lipido<0 or lipido>1:
        mb.showerror("ERROR","Recuerde que no se admiten valores negativos o mayores a 1")
    temp=float(input7_Tem.get())
    if temp <-40 or temp>150:
        mb.showerror("ERROR", "Temperatura fuera de rango\nReceurda que la tempreatura debe estar\ndentro del rango admitido de '-40°C hasta 150°C")
    sumalim=chos+proteina+fibra+carboh+h2o+lipido;sumalim=round(sumalim, 15)
    vrb=[chos,proteina,fibra,carboh,h2o,lipido,temp, sumalim]
    def calculo1(vrb):
        chos=vrb[0];proteina=vrb[1];fibra=vrb[2];carboh=vrb[3];h2o=vrb[4];lipido=vrb[5];temp=vrb[6];sumalim=vrb[7]
        if sumalim==1:
            cpprot= 2.0082+1.2089*(10**-3)*(temp)-1.3129*(10**-6)*(temp**2); cplip= 1.9842+1.4733*(10**-3)*(temp)-4.8008*(10**-6)*(temp**2)\
                ;cpcarboh=1.5488+1.9625*(10**-3)*(temp)-5.9399*(10**-6)*(temp**2); cpfib= 1.8459+1.8306*(10**-3)*(temp)-4.6509*(10**-6)*(temp**2)\
                    ;cpchos= 1.02926+1.8896*(10**-3)*(temp)-3.6817*(10**-6)*(temp**2)
            if temp<0 and temp>-40:
                cph2o= 4.0817-5.3062*(10**-3)*(temp)+9.9516*(10**-4)*(temp**2)
            elif temp>=0 and temp<150:
                cph2o= 4.1762-9.0864*(10**-5)*(temp)+5.4731*(10**-6)*(temp**2)\
                    ;cpalim=(cplip*lipido)+(cpprot*proteina)+(cpfib*fibra)+(cpcarboh*carboh)+(cpchos*chos)+(cph2o*h2o)
            label_CpR.configure(text=round((cpalim),4))
            denpro= 1.3299*(10**3)-5.1840*(10**-1)*temp;denlip= 9.2559*(10**2)-4.1757*(10**-1)*temp\
                ;dencarb= 1.5991*(10**3)-3.1046*(10**-1)*temp;denfib=1.3115*(10**3)-3.6589*(10**-1)*temp\
                    ;denchos=2.4238*(10**3)-2.8063*(10**-1)*temp;denh2o= 9.9718*(10**2)+3.1439*(10**-3)*temp-3.7574*(10**-3)*(temp**2)\
                        ;densid=1/((proteina/denpro)+(lipido/denlip)+(carboh/dencarb)+(fibra/denfib)+(chos/denchos)+(h2o/denh2o))\
                            ;label_DenR.configure(text=round((densid), 3))
            proteina2=(proteina/denpro)/(1/densid);lipido2=(lipido/denlip)/(1/densid);carboh2=(carboh/dencarb)/(1/densid)\
                ;fibra2=(fibra/denfib)/(1/densid);chos2=(chos/denchos)/(1/densid);h2o2=(h2o/denh2o)/(1/densid)
            kprot= 1.7881*(10**-1)+1.1958*(10**-3)*temp-2.7178*(10**-6)*temp**2;klip= 1.8071*(10**-1)-2.7604*(10**-3)*temp-1.7749*(10**-7)*temp**2\
                ;kcarboh=2.0141*(10**-1)+1.3874*(10**-3)*temp-4.3312*(10**-6)*temp**2;kfibra=1.8331*(10**-1)+1.2497*(10**-3)*temp-3.1683*(10**-6)*temp**2\
                    ;kchos=3.2962*(10**-1)+1.4011*(10**-3)*temp-2.9069*(10**-6)*temp**2;kh2o= 5.7109*(10**-1)+1.7625*(10**-3)*temp-6.7036*(10**-6)*temp**2\
                        ;kalim= (kprot*proteina2)+(klip*lipido2)+(kcarboh*carboh2)+(kfibra*fibra2)+(kchos*chos2)+(kh2o*h2o2);kalim=kalim/1000\
                            ;label_KR.configure(text=format(kalim, '.3E'))
            alpha=kalim/(densid*cpalim);label_AlpR.configure(text=round((alpha), 10))
            entalp=cpalim*temp;label_EntalR.configure(text=round((entalp), 3))
            v=0;Dp=1;u=entalp-(v*Dp);label_EinR.configure(text=round((u), 3))
        else:
            mb.showerror("ERROR", "Recuerda que la sumatoria de las\nfracciónes másicas debe ser 1")
    def calculo2(vrb):
        chos=vrb[0];proteina=vrb[1];fibra=vrb[2];carboh=vrb[3];h2o=vrb[4];lipido=vrb[5];temp=vrb[6];sumalim=vrb[7];calidad=float(input9_Calid.get());presion=float(input8_Pres.get())
        if calidad<=0 or calidad>0.85:
            mb.showerror("ERROR", "Calidad fuera de rango\n\nrecuerda que la caldiad 'X' debe estar\n0 < X <= 0.85")
        if presion <=0:
            mb.showerror("ERROR", "Presión negativa o nula\n\nRecuerda que la presión no puede ser <= 0")
        Ms_Agua = 1-calidad;Fraccion_Agua = Ms_Agua*h2o;Fracción_Vapor = calidad*h2o;Consentración = chos+proteina+fibra+carboh+lipido\
            ;Brix = Consentración*100;Pres = presion*10;Variables_ingresadas=[chos,proteina,fibra,carboh,lipido];Cont_Variables = 0
        for i in Variables_ingresadas:   
            if i>0 and i<=1:
                Cont_Variables = Cont_Variables + 1 
        if Cont_Variables == 0:
            mb.showerror("ERROR", "Revise los datos ingresados\n\nParece que no ingresó ningún dato de composición")
        else:
            Vapor_a_distribuir = Fracción_Vapor/Cont_Variables
        h2o=h2o-Fracción_Vapor
        if chos>0 and chos<=1:
            chos=chos+Vapor_a_distribuir 
        if proteina>0 and proteina<=1:
            proteina=proteina+Vapor_a_distribuir
        if fibra>0 and fibra<=1:
            fibra=fibra+Vapor_a_distribuir
        if carboh>0 and carboh<=1:
            carboh=carboh+Vapor_a_distribuir
        if lipido>0 and lipido<=1:
            lipido=lipido+Vapor_a_distribuir
        Pv=presion*7.50062
        if presion>0.61 and presion<=101.325: 
            a=8.0713; b=1730.63; c=233.426
        elif presion>101.325 and presion<=22064:
            a=8.14019; b=1810.94; c=244.485
        L=ma.log10(Pv);temp_ebu = ((b/(a-L))-c)
        if temp <= temp_ebu:
            mb.showwarning("CUIDADO","Revise los datos ingresados\n\nPara los datos ingresados se recomienda utilizar\
                \nel tipo de mezcla 'Liquido Saturado o Subenfriado'")
        elif temp > temp_ebu:
            label_Space.configure(text="Datos ingresados correctamente", font=("Lucida Fax", 12))
        if Azucar == 'Sacarosa':
            alf =3.061/(10**2); bet =0.094; gam =0.136; dlt =5.328/(10**2)
        elif Azucar == 'Azúcares reductores':
            alf =2.227/(10**2); bet =0.588; gam =0.119; dlt =3.593/(10**2)
        elif Azucar == 'Jugo de frutas':
            alf =1.360/(10**2); bet =0.749; gam =0.106; dlt =3.390/(10**2)
        elif Azucar == 'Extracto de café':
            alf =0.8474/(10**2); bet =0.9895; gam =0.1163; dlt =2.570/(10**2)
        elif Azucar == 'Jugo de manzana':
            alf =1.3602/(10**2); bet =0.7489; gam =0.1054; dlt =3.390/(10**2)
        elif Azucar == 'Soluciones de azucar':
            alf =3.0612/(10**2); bet =0.0942; gam =0.1356; dlt =5.329/(10**2)
        elif Azucar == 'Liquido Saturado (Sub-enfriado)':
            temp_Sis = temp
        epe=alf*(Brix**bet)*(Pres**gam)*(ma.exp(dlt*Brix))
        def validar_epe(epe):
            if epe > 10:
                mb.showerror("ERROR", "Revise los datos ingresados\n\nLa elevación del punto de ebullición (EPE)\nestá fuera del rángo lógico permitido (10°C)")
            elif epe <= 10:
                label_Space2.configure(text="Perfecto, la EPE está dentro\ndel margen lógico permitido (10°C)",font=("Lucida Fax", 12))
        validar_epe(epe)
        temp_Sis = temp_ebu + epe
        if sumalim==1:
            cpprot= 2.0082+1.2089*(10**-3)*(temp_Sis)-1.3129*(10**-6)*(temp_Sis**2);cplip= 1.9842+1.4733*(10**-3)*(temp_Sis)-4.8008*(10**-6)*(temp_Sis**2)\
                ;cpcarboh=1.5488+1.9625*(10**-3)*(temp_Sis)-5.9399*(10**-6)*(temp_Sis**2);cpfib= 1.8459+1.8306*(10**-3)*(temp_Sis)-4.6509*(10**-6)*(temp_Sis**2)\
                    ;cpchos= 1.02926+1.8896*(10**-3)*(temp_Sis)-3.6817*(10**-6)*(temp_Sis**2);cph2o= 4.1762-9.0864*(10**-5)*(temp_Sis)+5.4731*(10**-6)*(temp_Sis**2)\
                        ;cpalim=(cplip*lipido)+(cpprot*proteina)+(cpfib*fibra)+(cpcarboh*carboh)+(cpchos*chos)+(cph2o*h2o);cpmasa=(cplip*lipido)+(cpprot*proteina)+(cpfib*fibra)+(cpcarboh*carboh)+(cpchos*chos)\
                            ;cpvapor=32.24*(temp_Sis)+0.1923*(10**-2)*(temp_Sis)+1.055*(10**-5)*(temp_Sis**2)+(-3.595)*(10**-9)*(temp_Sis**3);label_CpR.configure(text=round((cpalim),4))
            denpro= 1.3299*(10**3)-5.1840*(10**-1)*temp_Sis;denlip= 9.2559*(10**2)-4.1757*(10**-1)*temp_Sis;dencarb= 1.5991*(10**3)-3.1046*(10**-1)*temp_Sis\
                ;denfib=1.3115*(10**3)-3.6589*(10**-1)*temp_Sis;denchos=2.4238*(10**3)-2.8063*(10**-1)*temp_Sis;denh2o= 9.9718*(10**2)+3.1439*(10**-3)*temp_Sis-3.7574*(10**-3)*(temp_Sis**2)\
                    ;densid=1/((proteina/denpro)+(lipido/denlip)+(carboh/dencarb)+(fibra/denfib)+(chos/denchos)+(h2o/denh2o));label_DenR.configure(text=round((densid), 3))
            proteina2=(proteina/denpro)/(1/densid);lipido2=(lipido/denlip)/(1/densid);carboh2=(carboh/dencarb)/(1/densid);fibra2=(fibra/denfib)/(1/densid)\
                ;chos2=(chos/denchos)/(1/densid);h2o2=(h2o/denh2o)/(1/densid)
            kprot= 1.7881*(10**-1)+1.1958*(10**-3)*temp_Sis-2.7178*(10**-6)*temp_Sis**2;klip= 1.8071*(10**-1)-2.7604*(10**-3)*temp_Sis-1.7749*(10**-7)*temp_Sis**2\
                ;kcarboh=2.0141*(10**-1)+1.3874*(10**-3)*temp_Sis-4.3312*(10**-6)*temp_Sis**2;kfibra=1.8331*(10**-1)+1.2497*(10**-3)*temp_Sis-3.1683*(10**-6)*temp_Sis**2\
                    ;kchos=3.2962*(10**-1)+1.4011*(10**-3)*temp_Sis-2.9069*(10**-6)*temp_Sis**2;kh2o= 5.7109*(10**-1)+1.7625*(10**-3)*temp_Sis-6.7036*(10**-6)*temp_Sis**2\
                        ;kalim= (kprot*proteina2)+(klip*lipido2)+(kcarboh*carboh2)+(kfibra*fibra2)+(kchos*chos2)+(kh2o*h2o2);kalim=kalim/1000;label_KR.configure(text=format(kalim, '.3e'))
            alpha=kalim/(densid*cpalim);label_AlpR.configure(text=format(alpha, '.3e'))
            cp1=cph2o*Fraccion_Agua;cp2=cpvapor*Fracción_Vapor
            entalp=temp_Sis*(cpmasa+cp1+cp2);label_EntalR.configure(text=round((entalp), 3))
            v=0;P=1;u=entalp-(P*v);label_EinR.configure(text=round((u), 3))
        else:
            mb.showerror("ERROR", "Recuerda que la sumatoria de las\nfracciónes másicas debe ser 1")
    if Azucar == 'Sacarosa':
        calculo2(vrb)
    elif Azucar == 'Azúcares reductores':
        calculo2(vrb)
    elif Azucar == 'Jugo de frutas':
        calculo2(vrb)
    elif Azucar == 'Extracto de café':
        calculo2(vrb)
    elif Azucar == 'Jugo de manzana':
        calculo2(vrb)
    elif Azucar == 'Soluciones de azucar':
        calculo2(vrb)
    elif Azucar == 'Liquido Saturado (Sub-enfriado)':
        calculo1(vrb)