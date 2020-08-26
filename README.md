# PID-aplicado-a-un-sistema-de-segundo-orden_Ziegler-Nichols_PYTHON

La función de transferencia de segundo orden de forma general se define de la siguiente manera:

![](https://latex.codecogs.com/svg.latex?G_%7Bs%7D%3D%5Cfrac%7Bw_%7Bn%7D%5E2%7D%7Bs%5E2&plus;2%5Czeta%20w_%7Bn%7Ds&plus;w_%7Bn%7D%5E2%7D)

Por tanto se hace referencia la necesidad de obtener un numerador y un denominador, para el caso del programa Transfer_Fuction_and_PID.py, el numerador y el denominador se establece como, num=[3,5], den=[1,3,2,**Kc**], en donde se puede determinar la planta del sistema variando el valor critico del denominador **Kc**.

La función de transferencia de un PID en el dominio de la frecuencia está definida de la siguiente forma:

![](https://latex.codecogs.com/svg.latex?G_%7Bc%7D%3D%5Cfrac%7BK_%7Bp%7DT_%7Bp%7DT_%7Bi%7Ds%5E%7B2%7D&plus;K_%7Bp%7DT_%7Bi%7Ds&plus;K_%7Bp%7D%7D%7BT_%7Bi%7Ds%7D)

La función de transferencia del PID en el dominio de la frecuencia se define en el script Transfer_Fuction_and_PID.py como: 
a=Kp*Ti*Td, b=Kp*Ti, c=Kp, d=Ti.

* num1=[a,b,c]

* den2=[0,d,0]

* sys3=crtl.tf(num1,den2)

Nota: Al variar el valor crítico de Kc eventualmente cambiara el valor Pcr, el cual es el valor de la diferencia de tiempo entre el segundo pico y el primero, del sistema subamortiguado, observar la figura *Pcr_TF.png*, en posteriores versiones se pretende definir al programa .py para determinar este valor de forma automática, además de agregar sistemas de control discretos.
