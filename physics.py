# Ficheiro de Python com constantes físicas que dão jeito, em unidades SI
import numpy as np

# Constantes Matemáticas
pi = np.pi

# Velocidade da Luz
c = 299_792_458

# Constante de Planck
h = 6.626_068e-34
hbar = h / (2 * np.pi)

# Carga elementar
qe = 1.602_176_46e-19

# Constante gravitacional
G = 6.674_30e-11

# Número de avogrado
Na = 6.022_140_76e23

# Massa do eletrão
me = 9.109_381_88e-31

# Massa do protão
mp = 1.672_621_58e-27

# Permitividade do vácuo
eps0 = 8.854_187_8e-12

# Permeabilidade do vácuo
mu0 = 1.256_637e-6

# Constante de Boltzmann
kB = 1.380_650_3e-23

# Uma atmosfera em Pascal
atm = 101_325

# Constante de Wien
B = 2.897_771_955e-3


T = 300
print(kB * T / qe)