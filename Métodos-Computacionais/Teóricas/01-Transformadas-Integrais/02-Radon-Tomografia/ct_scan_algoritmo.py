#-*- coding: iso-8859-1 -*-
#
# 
# usa modulo imutils e requer ficheiro sinogram.png com ... sinograma a inverter!
#
"Importar pacotes/fun��es"
import numpy as np 
import imutils
from skimage.transform import rotate ## Rotina para rodar imagem
import scipy.fftpack as fft          ## Fast Fourier Transform
import scipy.misc                    ## Contem pacote para gravar arrays numpy como imagem .png

from PIL import Image, ImageChops


## Fun��es    


"M�todo da transformada de Radon - transforma uma imagem num sinograma (N�o � usada para a reconstru��o - foi"
"assim que o sinograma de que partimos foi gerado"
def radon(image, steps):        
    #Constroi a Transformada de Radon usando 'steps' projec��es da 'imagem'. 
    height, width = np.shape(image)
    projections = np.zeros((steps,width))    # Array numpy para acumular projec��es.
    dTheta =                                 # Incremento do �ngulo das rota��es.
    
    for i in range(steps):
        projections[i,:] =  ???? # fazer a projec��o na direc��o \theta_i
        # c�digo a escrever
    return projections       # Devolve as projec��es como um sinograma.
    


"Transforma o sinograma para o dom�nio das frequ�ncias usando transformada de Fourier"
def fft_translate(projs):
	# ????? c�digo a escrever
    return fft_proj



"Filtra as  projec��es usando um filtro em rampa"
def ramp_filter(ffts):
    ramp =  ?????           # filtro
    return ffts * ramp

"Regressa ao dom�nio espacial usando uma transformada de Fourier inversa"
def inverse_fft_translate(operator):
    return ????? # fft filtrada



"Reconstr�i a imagem retroprojectando as projec��es filtradas (ou n�o)"
def back_project(sinograma filtrado):
    laminograma = np.zeros(?????) ##
    dTheta =   ????            ##
    for i in range(�ngulos):
        temp = rotate(?????, dTheta*i)  # pode usar rotina rotate do scipy!!
        laminograma += temp
    return laminograma



## Programa principal, que usa rotinas anteriores

########  Parte inicial, para simulat a TAC. Na 
imagem =   ?????                # ler imagem  do paciente (aqui ainda queremos gerar sinograma) e criar array numpy

sinograma = radon(imagem, 180)
imutils.imshow(sinograma)
###################
# Daqui em diante, reconstru�ao propriamente dita. Na pr�ctica � aqui que come�amos, dado um sinograma.
#
"Importar a imagem como array numpy e mostrar a imagem do sinograma original"
print("Sinograma Original")
sinogram =  ?????  # ler sinograma, plot


"Tentar reconstruir a imagem directamente do sinograma, sem usar qualquer tipo de filtragem (retroprojec��o n�o filtrada)"
print("Reconstruc��o sem filtragem")
unfiltered_reconstruction =  ?????# retroprojec��o que d� esborratado. Plot, gravar, imagem


"Usar a FFT para passar o sinograma para o dom�nio das frequ�ncias e imprimir o resultado"
frequency_domain_sinogram =  ??????                      # Plot, gravar, imagem      #


"Filtragem das projec��es no dom�nio das frequ�ncias, multiplicando cada uma pelo filtro em rampa (nas frequ�ncias)"
filtered_frequency_domain_sinogram = ?????   # filtrar espectro. Plot, gravar, imagem 


"Usar a FFT inversa para regressar ao dom�nio espacial"
filtered_spatial_domain_sinogram = ????     # de volta ao dom�nio espacial. Plot, gravar, imagem 


"Reconstru��o  da imagem original 2D por retroprojec��o filtrada"
reconstructed_image = ????    # retroprojectar a filtrada. Plot, gravar, imagem 


