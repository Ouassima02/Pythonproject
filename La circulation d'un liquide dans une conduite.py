
from PIL import Image
from PIL import ImageDraw
img = Image.open('C://Users//admin//Pictures//IMAGE EXERCICE.png')
I1=ImageDraw.Draw(img)
D1=input("enter la valeur de diamètre:")
V1=input("entrer la valeur de la vitesse 1:")
V2=input("entrer la valeur de la vitesse 2:")
MV=input("entrer la valeur de la masse volumique:")
import math
angle =math.tan(10*3.14/180)
print(angle)
try:
         D1=float(D1)
         V1=float(V1)
         V2=float(V2)
         MV=float(MV)
         L=D1/(2*angle)*(1-(V1/V2)**(1/2))
         DeltaP=1/2*MV*((V1**2)-(V2**2))
         print("la valeur de la longeur est :", L, "mm")
         print("la valeur de DeltaP est:",DeltaP,"Pa")

except:
         print("error")
