import urllib.request
import urllib
import numpy as np
import cv2
import os
import sys
from matplotlib import pyplot as plt

def baixaImagensNegativas():

   # link_imagens_negativas = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152' 
    link_imagens_negativas = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n04154340' 
    urls_imagens_negativas =  urllib.request.urlopen(link_imagens_negativas).read().decode()

    if not os.path.exists('negativas'):

        os.makedirs('negativas')



    numero_imagem = 1417



    for i in urls_imagens_negativas.splitlines():

        try:

            print(i)

            urllib.request.urlretrieve(i, "negativas/"+str(numero_imagem)+".jpg")

            img = cv2.imread("negativas/"+str(numero_imagem)+".jpg",cv2.IMREAD_GRAYSCALE)

            imagem_redimensionada = cv2.resize(img, (100,100))

            cv2.imwrite("negativas/"+str(numero_imagem)+".jpg",imagem_redimensionada)

            numero_imagem += 1

        except Exception as e:

            print(str(e))

def removeImagensComFalha():

    if not os.path.exists('feias'):
        os.makedirs('feias')

    igual = False

    for file_type in ['negativas']:

        for img in os.listdir(file_type):

            for feia in os.listdir('feias'):

                try:

                    caminho_imagem = str(file_type)+'/'+str(img)

                    feia = cv2.imread('feias/'+str(feia))

                    pergunta = cv2.imread(caminho_imagem)

                    if feia.shape == pergunta.shape and not(np.bitwise_xor(feia,pergunta).any()):

                        print('Apagando imagem feia!')

                        print(caminho_imagem)

                        os.remove(caminho_imagem)

                except Exception as e:

                    print(str(e))

def renomeiaImagensParaOrdenar():
    
    for i, f in enumerate(os.listdir('negativas')):
        print (i, f)
        
        f_new = '{}.jpg'.format(i)
        if f != f_new and f_new != '1.jpeg':
            os.rename(f, f_new)
            print ('{}.').format(i), f, '->', f_new


def geraListaDeImagensNegativas():
    for file_type in ['negativas']:

        for img in os.listdir(file_type):

            if file_type == 'negativas':

                line = file_type+'/'+img+'\n'

                with open('bg.txt','a') as f:

                    f.write(line)

            elif file_type == 'positivas':

                line = file_type+'/'+img+' 1 0 0 150 150\n'

                with open('info.dat','a') as f:

                    f.write(line)

def testeReconhecimento():

    # Define o número da Webcam

    # Responsável por ler arquivo XML

    
    # Inicializa o Classificador Cascade

    faceCascade = cv2.CascadeClassifier('data\cascade.xml')

    frame = cv2.imread('teste3.bmp')
    
    # Converte o frame para escalas de cinza e descarta os dados de cores

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray=equalizeHist(gray)
    # Detecta objetos e retorna o array de objetos

    fingerprint = faceCascade.detectMultiScale(gray, scaleFactor=1.01, minNeighbors=2, minSize=(20,20),flags=cv2.CASCADE_SCALE_IMAGE )
        # Desenha um retângulo em torno do objeto


    for (x,y,w,h) in fingerprint:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    # Mostra o Frame ao usuário

    cv2.imshow("Foto", frame)
    cv2.waitKey(0)


testeReconhecimento()
