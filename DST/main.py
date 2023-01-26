
# https://github.com/sunniesuhyoung/DST

import os
import sys
import time
import torch
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt # Per i grafici

from styletransfer import DST
from vggfeatures import VGG16_Extractor
from utils_plot import convert_image
from utils_misc import pil_loader, pil_resize_long_edge_to, pil_to_tensor

# Parse Arguments

content_path='venv/DST/example/content.jpg'
style_path='venv/DST/example/style.jpg'
content_pts_path='venv/DST/example/CleanedPts/correspondence_A.txt'
style_pts_path='venv/DST/example/CleanedPts/correspondence_B.txt'
output_dir='venv/static/example/DSTresults'
output_prefix='result'
im_size = 256
max_iter=int(sys.argv[1])
checkpoint_iter=50
content_weight=float(sys.argv[2]) # alpha
warp_weight=float(0.10) # beta
reg_weight=float(sys.argv[3]) # gamma
optim='sgd'
lr=float(0.3)
verbose=0
save_intermediate=0
save_extra=0
device='cpu' # cpu or cuda

# Print settings
print('\n\n---------------------------------')
print('Started Deformable Style Transfer')
print('---------------------------------')

print('\nSettings')
print('   content_path:', content_path)
print('   style_path:', style_path)
print('   content_pts_path:', content_pts_path)
print('   style_pts_path:', style_pts_path)
print('   output_dir:', output_dir)
print('   output_prefix:', output_prefix)
print('   im_size:', im_size)
print('   max_iter:', max_iter)
print('   checkpoint_iter:', checkpoint_iter)
print('   content_weight:', content_weight)
print('   warp_weight:', warp_weight)
print('   reg_weight:', reg_weight)
print('   optim:', optim)
print('   lr:', lr)
print('   verbose:', verbose)
print('   save_intermediate:', save_intermediate)
print('   save_extra:', save_extra)

# Create output directory
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define feature extractor
extractor = VGG16_Extractor().to(device)

# Load content/style images and keypoints
content_pil = pil_loader(content_path)
style_pil = pil_loader(style_path)
content_pts = np.loadtxt(content_pts_path, delimiter=',')
style_pts = np.loadtxt(style_pts_path, delimiter=',')

# Rescale images
content_resized = pil_resize_long_edge_to(content_pil, im_size)
style_resized = pil_resize_long_edge_to(style_pil, im_size)
content_im_orig = pil_to_tensor(content_resized).to(device)
style_im_orig = pil_to_tensor(style_resized).to(device)

# Rescale points (assuming that points are in the original image's scale)
c_width, c_height = content_pil.size
c_fac = im_size/max(c_width, c_height)
for i in range(content_pts.shape[0]):
    content_pts[i][0] *= c_fac
    content_pts[i][1] *= c_fac

s_width, s_height = style_pil.size
s_fac = im_size/max(s_width, s_height)
for i in range(style_pts.shape[0]):
    style_pts[i][0] *= s_fac
    style_pts[i][1] *= s_fac

content_pts = torch.from_numpy(content_pts).float()
style_pts = torch.from_numpy(style_pts).float()

# Initialize the output image as the content image (This is a simpler initialization
# than what's described in the STROTSS paper, but we found that results are similar)
initial_im = content_im_orig.clone()

# Run deformable style transfer
start_time = time.time()
output = DST(initial_im, content_im_orig, style_im_orig, extractor,
                content_path, style_path, content_pts, style_pts, style_pts_path,
                 output_dir, output_prefix,
                 im_size=im_size,
                 max_iter=max_iter,
                 checkpoint_iter=checkpoint_iter,
                 content_weight=content_weight,
                 warp_weight=warp_weight,
                 reg_weight=reg_weight,
                 optim=optim,
                 lr=lr,
                 verbose=verbose,
                 save_intermediate=save_intermediate,
                 save_extra=save_extra,
                 device=device)

content_pil = pil_resize_long_edge_to(pil_loader(content_path), int(im_size))   # Ridimensiona l'immagine iniziale
style_pil = pil_resize_long_edge_to(pil_loader(style_path), int(im_size))  # Ridimensiona l'immagine di stile


# Write the stylized output image
save_im = convert_image(output[0])
save_im = Image.fromarray(save_im)
save_im.save(output_dir + '/' + output_prefix + '.png')
# imwrite(output_dir + '/' + output_prefix + '.png', save_im)
print('\nSovrapposizione salvata in ', output_dir + '/' + output_prefix + '.png')


result_pil = pil_resize_long_edge_to(pil_loader(output_dir + '/' + output_prefix + '.png'), int(im_size)) # Ridimensiona il risultato

# Raffigura disegno iniziale, opera da cui è stata estratta la base cromatica e la sovrapposizione
fig = plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.imshow(content_pil); plt.axis('off'); plt.title('Disegno');
plt.subplot(1, 3, 2)
plt.imshow(style_pil); plt.axis('off'); plt.title('Opera');
plt.subplot(1, 3, 3)
plt.imshow(result_pil); plt.axis('off'); plt.title('Sovrapposizione');
plt.savefig(output_dir + '/' + 'sequenza' + '.png');   # Salva l'intera sequenza
print('\nIntera sequenza salvata in ', output_dir + '/' + 'sequenza' + '.png')


# Report total time
end_time = time.time()
total_time = (end_time - start_time) / 60
print('\nProcesso terminato dopo {:04.3f} minuti\n'.format(total_time))
