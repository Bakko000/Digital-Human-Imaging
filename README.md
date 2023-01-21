# Digital Human Imaging

Questo progetto di tesi ha lo scopo di creare un servizio web che permetta agli utenti di estrarre la base cromatica da un’opera finita e trasferirla in un disegno (dello stesso artista o meno), con lo scopo di identificare le analogie e le differenze tra esso ed il dipinto tramite confronto. La colorazione del disegno può rivelare infatti i dettagli più sfuggenti e sbiaditi che possono inizialmente sfuggire. Inoltre, i colori facilitano l’identificazione dei punti in comune o meno. A tal fine, una volta stabilito il modello di Neural Style Transfer più adatto, è stato realizzato il sito web che lo implementa, concedendo all’utente la possibilità di personalizzare i principali parametri che influiscono sul risultato finale.


# Requisiti e imports
<ul>
  <li>Python 3.x</li>
  <li>pytorch, torchvision, cudatoolkit, numpy, PIL, matplotlib, sklearn</li>
</ul>

Il servizio web è reso possibile da Flask e un ambiente virtuale: <b>venv</b>


<pre>
import matplotlib.pyplot as plt
import numpy as np
import torch
from utils_misc import pil_loader, pil_resize_long_edge_to, pil_to_tensor
</pre>


<b>Update 21/09/2022</b> sono stati rilevati problemi di incompatibilità con nuove versioni di pytorch (>1.9) al momento si consiglia di installare pytorch 1.9 con le librerie consigliate di riferimento:
<a href='https://pytorch.org/get-started/previous-versions/'>vedere qui per una lista completa</a>

Comunque la Demo ed il servizio web sono stati aggiornati.


# Iperparametri modificabili
<pre>
content_weight = 8
reg_weight = 500
warp_weight = 0.1
</pre>


# Esempio di ouput
Disegno di Raffaello + Stile di Raffaello


<a href="https://ibb.co/k9FXzP1"><img src="https://i.ibb.co/9VjWBdt/risultatoraffaritratto.png" alt="risultatoraffaritratto" border="0"></a>


# Demo

<a href="https://colab.research.google.com/drive/1YgZwq7jPIX-_1qN3aGBdiwnr_377IeXh?usp=sharing">Demo</a>   
Eseguibile e modificabile su Google Colab




# Ringraziamenti
Parti del codice appartengono ai seguenti paper
<ul>
  <li>Deformable Style Transfer. Sunnie S. Y. Kim and Nicholas Kolkin and Jason Salavon and Gregory Shakhnarovich. ECCV 2020  2020. <a href="https://arxiv.org/abs/2003.11038">[paper]</a> <a href="https://github.com/sunniesuhyoung/DST">[code]</a></li>
  <li>Style Transfer by Relaxed Optimal Transport and Self-Similarity. Nicholas Kolkin, Jason Salavon and Gregory Shakhnarovich. CVPR 2019. <a href="https://arxiv.org/abs/1904.12785v2">[paper]</a><a href="https://github.com/nkolkin13/STROTSS">[code]</a></li>
  <li>WarpGAN: Automatic Caricature Generation. Yichun Shi, Debayan Deb and Anil K. Jain. CVPR 2019. <a href="https://arxiv.org/abs/1811.10100">[paper]</a><a href="https://github.com/seasonSH/WarpGAN">[code]</a></li>
  <li>Neural Best-Buddies: Sparse Cross-Domain Correspondence. Kfir Aberman, Jing Liao, Mingyi Shi, Dani Lischinski, Baoquan Chen and Daniel Cohen-Or. SIGGRAPH 2018. <a href="https://arxiv.org/abs/1805.04140v2">[paper]</a><a href="https://github.com/kfiraberman/neural_best_buddies">[code]</a></li>
  </ul>
