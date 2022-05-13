# Digital Human Imaging


Nella disciplina dell'arte sono tanti i disegni lasciati dai maggiori artisti, molti di questi sono esperimenti singoli, altri veri e propri studi o idee originarie sulla realizzazione di una prossima opera.
Il progetto indaga e restituisce la possibilità di concedere vita, ridare anima a queste “carte” all’apparenza inermi, trasferendoci uno stile a scelta dell'utente.

# Requisiti e imports
<ul>
  <li>Python 3</li>
  <li>pytorch, torchvision, cudatoolkit, numpy, PIL, matplotlib, sklearn</li>
</ul>



<pre>
import matplotlib.pyplot as plt
import numpy as np
import ipywidgets as widgets
import torch
from utils_misc import pil_loader, pil_resize_long_edge_to, pil_to_tensor
</pre>


# Iperparametri modificabili
<pre>

</pre>


# Esempio
Disegno di ritratto di Raffaello + Stile di Raffaello nella Maddalena -> Disegno finale





# Demo

<a href="https://colab.research.google.com/drive/1E8Wtr8iGeZH-DagAIKppHKsxVxfJDc8k?usp=sharing">Demo</a>   
Eseguibile e modificabile su Google Colab




# Ringraziamenti
Il codice appartiene ai seguenti paper
<ul>
  <li>Deformable Style Transfer. Sunnie S. Y. Kim and Nicholas Kolkin and Jason Salavon and Gregory Shakhnarovich. ECCV 2020  2020. <a href="https://arxiv.org/abs/2003.11038">[paper]</a> <a href="https://github.com/sunniesuhyoung/DST">[code]</a></li>
  <li>Style Transfer by Relaxed Optimal Transport and Self-Similarity. Nicholas Kolkin, Jason Salavon and Gregory Shakhnarovich. CVPR 2019. [paper] [code]</li>
  <li>WarpGAN: Automatic Caricature Generation. Yichun Shi, Debayan Deb and Anil K. Jain. CVPR 2019. [paper] [code]</li>
  <li>Neural Best-Buddies: Sparse Cross-Domain Correspondence. Kfir Aberman, Jing Liao, Mingyi Shi, Dani Lischinski, Baoquan Chen and Daniel Cohen-Or. SIGGRAPH 2018. [paper] [code]</li>
  </ul>
