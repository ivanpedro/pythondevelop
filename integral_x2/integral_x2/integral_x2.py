
"""
integral entre a y b de x **p *dx

deltax = (b-a)/n: being n the aproximation presion value. 

"""

def potencia(x,p):
    return x**p



def integral_definida(f,a,b,n,p):

    if n == 0:
        sumatoria = 0
    else:

        deltax = (b - a)/float(n)
        sumatoria = 0

        for i in range(n):
            sumatoria =  deltax * f((a + i * deltax),p)

    return sumatoria


def main():

    inter_a = float(input("Beging of interval: "))
    inter_b = float(input("Ending of interval: "))
    power = int(input("Power integral: "))
    approx_n = int(input("Number of rectangles: "))

    print('Integration between {0} y {1}'.format(inter_a,inter_b))
    
    print('Integral of x**{0} {1}'.format(power,integral_definida(potencia , inter_a, inter_b, approx_n, power)))


#def cuadrado(x):
#    return x**2

#def cubo(x):
#    return x**3

#def integral_definida(f,a,b,n):

#    if n == 0:
#        sumatoria = 0
#    else:

#        deltax = (b - a)/float(n)
#        sumatoria = 0

#        for i in range(n):
#            sumatoria =  deltax * f(a + i * deltax)

#    return sumatoria


#def main():

#    inter_a = float(input("Beging of interval: "))
#    inter_b = float(input("Ending of interval: "))
   
#    approx_n = int(input("Number of rectangles: "))

#    print('Integration between {0} y {1}'.format(inter_a, inter_b))
#    print('Integral of x**2 {0}'.format(integral_definida(cuadrado , inter_a, inter_b, approx_n))) 
#    print('Integral of x**3 {0}'.format(integral_definida(cubo , inter_a, inter_b, approx_n)))   

if __name__ == '__main__':

    main()