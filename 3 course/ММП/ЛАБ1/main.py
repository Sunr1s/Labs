import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


class Var:
    density_sphere = 2.21
    density_liquid  = 1.2
    max_density_liquid  = 10.5
    h = 1
    r = 0.25
    g = 10
    viscosity = 0.5
    max_viscosity = 3.8

def main(x,y,step):
    global v , t
    results = ()
    while Var.density_liquid < Var.max_density_liquid and Var.viscosity < Var.max_viscosity:
        v = 2/9*(Var.g*(math.pow(Var.r,2)))*((Var.density_sphere - Var.density_liquid) / Var.viscosity)
        t = 1/v
        print(f'Швидкість: {str(round(v,5))} Час: {str(round(t,5))} густина: {round(Var.density_liquid,3)} , в:язкість: {round(Var.viscosity,3)}')
        if v > 0 and t > 0:
            print(f'Швидкість: {str(round(v,5))} Час: {str(round(t,5))} густина: {round(Var.density_liquid,3)} , в:язкість: {round(Var.viscosity,3)}')
        else:
            print(f'Тіло буде вспливати! Якщо густина: {round(Var.density_liquid,3)} , в:язкість: {round(Var.viscosity,3)} та більше!')
            break
        results = results + (v,t,Var.density_liquid,Var.viscosity)
        if x:
            Var.density_liquid +=step
        if y:
           Var.viscosity+=step  
    return results

def printDiagrams(res):
    i,j, k = 0 , 0 ,0
    temp = []
    lenRes = len(res)
    while lenRes > 0:
        i+=4
        temp.append (res[j:i])  
        j = i
        lenRes -= 4
        k +=1

    plt.style.use('_mpl-gallery')

    # make data
    x,y,z = [],[],[]
    for a in temp:
        x.append(a[0])
        y.append(a[1])
        z.append(a[2])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    vertices = [list(zip(x,y,z))]
    poly = Poly3DCollection(vertices, alpha=0.8)
    ax.add_collection3d(poly)
    ax.set_xlim(0,1)
    ax.set_ylim(-279,1080)
    ax.set_zlim(0.5,3.8) 
    ax.set_xlabel("Швидкість")
    ax.set_ylabel("Час")
    ax.set_zlabel("Густина")

    for a in temp:
        z.append(a[3])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    vertices = [list(zip(x,y,z))]
    poly = Poly3DCollection(vertices, alpha=0.8)
    ax.add_collection3d(poly)
    ax.set_xlim(0,1)
    ax.set_ylim(-279,1080)
    ax.set_zlim(1.2,10.5) 
    ax.set_xlabel("Швидкість")
    ax.set_ylabel("Час")
    ax.set_zlabel("Шільність")
    plt.show()



if __name__ == "__main__":
    x = True
    y = True
    res = main(x, y, 0.05)
    printDiagrams(res)