import torch
from collections import OrderedDict
model_path1 = '/Users/yunyubai/Downloads/s_model1.pth'
model_path2 = '/Users/yunyubai/Downloads/s_model2.pth'
model_path = '/Users/yunyubai/Downloads/lighthead-rcnn-extractor-pretrained.pth'
model_dict = torch.load(model_path, map_location='cpu')
model_dict1 = torch.load(model_path1, map_location='cpu')
model_dict2 = torch.load(model_path2, map_location='cpu')

num = len(model_dict1)
keys = list(model_dict1.keys())
mp={}
for k in range(len(keys)):
    mp[k] = keys[k]

total_model = OrderedDict()
for i in range(num):
    total_model[mp[i]] = model_dict1[mp[i]]


num = len(model_dict2)
keys = list(model_dict2.keys())
mp={}
for k in range(len(keys)):
    mp[k] = keys[k]

for i in range(num):
    total_model[mp[i]] = model_dict2[mp[i]]
torch.save(total_model, '/Users/yunyubai/Downloads/s_model.pth')


'''  check 
num = len(model_dict)
keys = list(model_dict.keys())
mp={}
for k in range(len(keys)):
    mp[k] = keys[k]
for k in range(num):
    assert total_model[mp[k]].equal(model_dict[mp[k]])
'''