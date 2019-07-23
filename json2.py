import json
import os
from lxml.etree import Element, SubElement, tostring
from PIL import Image


class json2xml(object):
    def __init__(self, inpath, outpath, imgpath):
        self.inpath = inpath
        self.outpath = outpath
        self.imgpath = imgpath
        if not os.path.exists(outpath):
            os.makedirs(outpath)
        self.files = os.listdir(inpath)
        if '.DS_Store' in self.files:
            self.files.remove('.DS_Store')
        self.filenum = len(self.files)
        self.transform()

    def transform(self):
        for file in self.files:
            im = Image.open(self.imgpath+'/'+file[:-5]+'.png')
            width, height = im.size
            outfile = self.outpath+'/'+file[:-5]+'.xml'
            annos = json.load(open(self.inpath+'/'+file, 'r'))
            node_root = Element('annotation')

            node_folder = SubElement(node_root, 'folder')
            node_folder.text = 'VOC2007'
            node_filename = SubElement(node_root, 'filename')
            node_filename.text = file
            node_owner = SubElement(node_root, 'owner')
            node_name = SubElement(node_owner, 'name')
            node_name.text = 'HengTian'

            node_size = SubElement(node_root, 'size')
            node_width = SubElement(node_size, 'width')
            node_width.text = str(width)
            node_height = SubElement(node_size, 'height')
            node_height.text = str(height)
            node_depth = SubElement(node_size, 'depth')
            node_depth.text = '1'
            node_seg = SubElement(node_root, 'segmented')
            node_seg.text = '0'

            for item in annos['form']:
                for w in  item['words']:
                    node_object = SubElement(node_root, 'object')
                    node_name = SubElement(node_object, 'name')
                    node_name.text = 'word'  # 我们做的是二元分类
                    node_difficult = SubElement(node_object, 'difficult')
                    node_difficult.text = '0'
                    node_bndbox = SubElement(node_object, 'bndbox')
                    node_xmin = SubElement(node_bndbox, 'xmin')
                    node_xmin.text = str(w['box'][0])
                    node_ymin = SubElement(node_bndbox, 'ymin')
                    node_ymin.text = str(w['box'][1])
                    node_xmax = SubElement(node_bndbox, 'xmax')
                    node_xmax.text = str(w['box'][2])
                    node_ymax = SubElement(node_bndbox, 'ymax')
                    node_ymax.text = str(w['box'][3])

            xml = tostring(node_root, pretty_print=True)  # 格式化显示，该换行的换行
            xml = xml.decode('utf-8')

            with open(outfile, 'w', encoding='utf-8') as f:
                f.write(xml)

if __name__ == '__main__':
    inpath = '/Users/yunyubai/Downloads/dataset/training_data/annotations'
    outpath = '/Users/yunyubai/Downloads/dataset/training_data/xmls'
    imgpath = '/Users/yunyubai/Downloads/dataset/training_data/images'
    json2xml(inpath, outpath, imgpath)

