import matplotlib.pyplot as plt
import numpy as np

N=100
x = np.linspace(-2, 2, N)
y = np.linspace(-2, 2, N)
X, Y = np.meshgrid(x,y)

R = np.sqrt(X**2+Y**2)
Theta = np.arctan2(Y,X)

R_cyl=1.0

U=1.0

Phi = U * (R + (R_cyl**2/R))* np.cos(Theta)
Psi = U * (R - (R_cyl**2/R))* np.sin(Theta)

mask = R < R_cyl
Psi[mask] = np.nan

plt.figure(figsize=(6,6))
plt.contour(X,Y,Psi,levels=50,cmap="coolwarm")
plt.contour(X,Y,Phi,levels=50,colors="black",alpha=0.5)
plt.colorbar(label="Stream Function")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Potential flow around a cylinder")

circle=plt.Circle((0,0),R_cyl, color="black",fill=True)
plt.gca().add_patch(circle)

plt.show()
