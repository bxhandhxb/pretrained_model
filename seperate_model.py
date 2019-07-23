import torch
from collections import OrderedDict

#model_path = '/Users/yunyubai/Downloads/lighthead_rcnn_model_gpu.pth'
model_path = '/Users/yunyubai/Downloads/lighthead-rcnn-extractor-pretrained.pth'
model_dict = torch.load(model_path, map_location='cpu')

num = len(model_dict)
keys = list(model_dict.keys())
mp={}
for k in range(len(keys)):
    mp[k] = keys[k]

s_model1 = OrderedDict()
s_model2 = OrderedDict()
for i in range(400):
    s_model1[mp[i]] = model_dict[mp[i]]
torch.save(s_model1, '/Users/yunyubai/Downloads/s_model1.pth')

for i in range(400, num):
    s_model2[mp[i]] = model_dict[mp[i]]
torch.save(s_model2, '/Users/yunyubai/Downloads/s_model2.pth')

