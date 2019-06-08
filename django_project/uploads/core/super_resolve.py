from __future__ import print_function
import argparse
import torch
from PIL import Image
from torchvision.transforms import ToTensor

from uploads.core.model import Net




import os.path
from os import listdir




import numpy as np


script_dir = os.path.dirname(os.path.abspath(__file__))


# # Training settings

# parser = argparse.ArgumentParser(description='PyTorch Super Res Example')
# parser.add_argument('--upscale_factor', type=int, required=True, help="super resolution upscale factor")
# parser.add_argument('--cuda', action='store_true', help='use cuda?')


# parser.add_argument('--input_image', type=str, required=True, help='input image to use')
# parser.add_argument('--model', type=str, required=True, help='model file to use')
# parser.add_argument('--output_filename', type=str, help='where to save the output image')
# parser.add_argument('--cuda', action='store_true', help='use cuda')

# opt = parser.parse_args()

print("I'm in super_resolve.py")


def predict(img_path, output_image_name):

    # print("dir list")
    # arr = os.listdir("media")
    # print(arr)


    
    print("hi, i'm in")
    img = Image.open(img_path).convert('YCbCr')
    y, cb, cr = img.split()

    # initializing the model for state_dict, need default arg parse
    model = Net(upscale_factor= 2)


    model.load_state_dict(torch.load(os.path.join(script_dir, "model_epoch_3.pth")))


    img_to_tensor = ToTensor()
    input = img_to_tensor(y).view(1, -1, y.size[1], y.size[0])


    out = model(input)
    out = out.cpu()
    out_img_y = out[0].detach().numpy()
    out_img_y *= 255.0
    out_img_y = out_img_y.clip(0, 255)
    out_img_y = Image.fromarray(np.uint8(out_img_y[0]), mode='L')

    out_img_cb = cb.resize(out_img_y.size, Image.BICUBIC)
    out_img_cr = cr.resize(out_img_y.size, Image.BICUBIC)
    out_img = Image.merge('YCbCr', [out_img_y, out_img_cb, out_img_cr]).convert('RGB')

    out_img.save(output_image_name)
    print('output image saved to ', "out.png")

#predict('dataset/BSDS300/images/test/14037.jpg')
