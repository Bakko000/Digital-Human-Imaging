# Digital Human Imaging


Nella disciplina dell'arte sono tanti i disegni lasciati dai maggiori artisti, molti di questi sono esperimenti singoli, altri veri e propri studi o idee originarie sulla realizzazione di una prossima opera.
Il progetto indaga e restituisce la possibilità di concedere vita, ridare anima a queste “carte” all’apparenza inermi, trasferendoci uno stile a scelta dell'utente.

# Requisiti e imports
<ul>
  <li>Python 3</li>
  <li>pytorch, torchvision, cudatoolkit, numpy, PIL, matplotlib, sklearn</li>
</ul>

Il servizio web è reso possibile da Flask


<pre>
import matplotlib.pyplot as plt
import numpy as np
import torch
from utils_misc import pil_loader, pil_resize_long_edge_to, pil_to_tensor
</pre>


<b>Update 21/09/2022</b> sono stati rilevati problemi di incompatibilità con nuove versioni di pytorch (>1.9) al momento si consiglia di installare pytorch 1.9 con le librerie consigliate di riferimento:
<a href='https://pytorch.org/get-started/previous-versions/'>vedere qui per una lista completa</a>

Comunque la Demo ed il Servizio Web sono stati aggiornati.


# Iperparametri modificabili
<pre>
max_iter = 550 
content_weight = 8
reg_weight = 95
</pre>


# Esempio di ouput
Disegno di Raffaello + Stile di Raffaello


<a href="https://ibb.co/k9FXzP1"><img src="https://i.ibb.co/9VjWBdt/risultatoraffaritratto.png" alt="risultatoraffaritratto" border="0"></a>


# Demo

<a href="https://colab.research.google.com/drive/1YgZwq7jPIX-_1qN3aGBdiwnr_377IeXh?usp=sharing">Demo</a>   
Eseguibile e modificabile su Google Colab




# Ringraziamenti
Il codice appartiene ai seguenti paper
<ul>
  <li>Deformable Style Transfer. Sunnie S. Y. Kim and Nicholas Kolkin and Jason Salavon and Gregory Shakhnarovich. ECCV 2020  2020. <a href="https://arxiv.org/abs/2003.11038">[paper]</a> <a href="https://github.com/sunniesuhyoung/DST">[code]</a></li>
  <li>Style Transfer by Relaxed Optimal Transport and Self-Similarity. Nicholas Kolkin, Jason Salavon and Gregory Shakhnarovich. CVPR 2019. <a href="https://arxiv.org/abs/1904.12785v2">[paper]</a><a href="https://github.com/nkolkin13/STROTSS">[code]</a></li>
  <li>WarpGAN: Automatic Caricature Generation. Yichun Shi, Debayan Deb and Anil K. Jain. CVPR 2019. <a href="https://arxiv.org/abs/1811.10100">[paper]</a><a href="https://github.com/seasonSH/WarpGAN">[code]</a></li>
  <li>Neural Best-Buddies: Sparse Cross-Domain Correspondence. Kfir Aberman, Jing Liao, Mingyi Shi, Dani Lischinski, Baoquan Chen and Daniel Cohen-Or. SIGGRAPH 2018. <a href="https://arxiv.org/abs/1805.04140v2">[paper]</a><a href="https://github.com/kfiraberman/neural_best_buddies">[code]</a></li>
  </ul>
