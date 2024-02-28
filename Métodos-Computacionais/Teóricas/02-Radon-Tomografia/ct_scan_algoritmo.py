#-*- coding: iso-8859-1 -*-
#
# 
# usa modulo imutils e requer ficheiro sinogram.png com ... sinograma a inverter!
#
"Importar pacotes/funções"
import numpy as np 
import imutils
from skimage.transform import rotate ## Rotina para rodar imagem
import scipy.fftpack as fft          ## Fast Fourier Transform
import scipy.misc                    ## Contem pacote para gravar arrays numpy como imagem .png

from PIL import Image, ImageChops


## Funções    


"Método da transformada de Radon - transforma uma imagem num sinograma (Não é usada para a reconstrução - foi"
"assim que o sinograma de que partimos foi gerado"
def radon(image, steps):        
    #Constroi a Transformada de Radon usando 'steps' projecções da 'imagem'. 
    height, width = np.shape(image)
    projections = np.zeros((steps,width))    # Array numpy para acumular projecções.
    dTheta =                                 # Incremento do ângulo das rotações.
    
    for i in range(steps):
        projections[i,:] =  ???? # fazer a projecção na direcção \theta_i
        # código a escrever
    return projections       # Devolve as projecções como um sinograma.
    


"Transforma o sinograma para o domínio das frequências usando transformada de Fourier"
def fft_translate(projs):
	# ????? código a escrever
    return fft_proj



"Filtra as  projecções usando um filtro em rampa"
def ramp_filter(ffts):
    ramp =  ?????           # filtro
    return ffts * ramp

"Regressa ao domínio espacial usando uma transformada de Fourier inversa"
def inverse_fft_translate(operator):
    return ????? # fft filtrada



"Reconstrói a imagem retroprojectando as projecções filtradas (ou não)"
def back_project(sinograma filtrado):
    laminograma = np.zeros(?????) ##
    dTheta =   ????            ##
    for i in range(ângulos):
        temp = rotate(?????, dTheta*i)  # pode usar rotina rotate do scipy!!
        laminograma += temp
    return laminograma



## Programa principal, que usa rotinas anteriores

########  Parte inicial, para simulat a TAC. Na 
imagem =   ?????                # ler imagem  do paciente (aqui ainda queremos gerar sinograma) e criar array numpy

sinograma = radon(imagem, 180)
imutils.imshow(sinograma)
###################
# Daqui em diante, reconstruçao propriamente dita. Na práctica é aqui que começamos, dado um sinograma.
#
"Importar a imagem como array numpy e mostrar a imagem do sinograma original"
print("Sinograma Original")
sinogram =  ?????  # ler sinograma, plot


"Tentar reconstruir a imagem directamente do sinograma, sem usar qualquer tipo de filtragem (retroprojecção não filtrada)"
print("Reconstrucção sem filtragem")
unfiltered_reconstruction =  ?????# retroprojecção que dá esborratado. Plot, gravar, imagem


"Usar a FFT para passar o sinograma para o domínio das frequências e imprimir o resultado"
frequency_domain_sinogram =  ??????                      # Plot, gravar, imagem      #


"Filtragem das projecções no domínio das frequências, multiplicando cada uma pelo filtro em rampa (nas frequências)"
filtered_frequency_domain_sinogram = ?????   # filtrar espectro. Plot, gravar, imagem 


"Usar a FFT inversa para regressar ao domínio espacial"
filtered_spatial_domain_sinogram = ????     # de volta ao domínio espacial. Plot, gravar, imagem 


"Reconstrução  da imagem original 2D por retroprojecção filtrada"
reconstructed_image = ????    # retroprojectar a filtrada. Plot, gravar, imagem 


