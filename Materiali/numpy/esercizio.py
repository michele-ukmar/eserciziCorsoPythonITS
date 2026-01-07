import numpy as np
# Calcola l'immagine media dei volti. 

# Scarica il set di dati Labeled Faces in the Wild (google: LFW face dataset). Scegli un volto con almeno 100 immagini. 
# http://vis-www.cs.umass.edu/lfw/
# http://vis-www.cs.umass.edu/lfw/lfw.tgz

import requests
import os
import skimage.io

# Estrai il file .tgz in una cartella del tuo computer.
lfw_path = os.path.dirname(__file__)
lfw_path_file = os.path.join(lfw_path, 'lfw.tgz')
# get the dataset and save it to disk
# if file exists, skip download
if not os.path.exists(lfw_path_file):
    r = requests.get('http://vis-www.cs.umass.edu/lfw/lfw.tgz', stream=True)
    # save request content to file
    with open(lfw_path_file, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)

# extract the dataset
import tarfile
lfw_path = os.path.join(lfw_path, 'lfw')
if not (os.path.exists(lfw_path)):
    with tarfile.open(lfw_path_file , 'r:gz') as tar:
        tar.extractall(lfw_path)

# Chiamare numpy.zeros per creare un tensore float64 250 x 250 x 3 per contenere il risultato 
# (250 x 250 è la dimensione dell'immagine, 3 è il numero di canali di colore).
risultato = np.zeros((250, 250, 3), dtype=np.float64)

# find the folder with at least 100 images
for folder in os.listdir(lfw_path):
    folder_path = os.path.join(lfw_path, folder)
    if os.path.isdir(folder_path):
        if len(os.listdir(folder_path)) >= 100:
            lfw_path = folder_path
            break

# Leggi ogni immagine con skimage.io.imread, converti in float e accumula 
for filename in os.listdir(lfw_path):
    if filename.endswith('.jpg'):
        filepath = os.path.join(lfw_path, filename)
        img = skimage.io.imread(filepath).astype(np.float64)
        risultato += img

risultato /= len(os.listdir(lfw_path))
# Scrivi il risultato medio con skimage.io.imsave
risultato_path = os.path.join(os.path.dirname(__file__), 'media.jpg')
skimage.io.imsave(risultato_path, risultato)

