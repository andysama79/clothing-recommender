import cv2
from smplx import SMPLX
import numpy as np


impath = 'dataset/humans/images/Helen.png'
img = cv2.imread(impath)

smpl = SMPLX(model_path='../smplx/models/SMPL_python_v.1.1.0/smpl/models/basicmodel_f_lbs_10_207_0_v1.1.0.pkl')

result = smpl(img)

print(result.keys())

mesh = smpl.get_mesh(result)

smpl.visualize(img, result, mesh)