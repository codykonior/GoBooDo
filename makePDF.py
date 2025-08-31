from fpdf import FPDF
import os
from PIL import Image
from tqdm import tqdm
import img2pdf

class createBook:

    def __init__(self,name,path):
        self.name = name
        self.path = path
        nameList = sorted([d for d in os.listdir(os.path.join(path,'Images')) if d != '.DS_Store'],key= lambda x : int(x[:-4]))
        self.imageNameList = [os.path.join(path,'Images',x) for x in nameList]

    def makePdf(self):
        useimg2pdf = True

        if useimg2pdf:
            if not os.path.exists(os.path.join(self.path,'Output')):
                os.mkdir(os.path.join(self.path,'Output'))
            name = str(self.name[:min(10,len(self.name))]).replace(" ","")
            name = ''.join(ch for ch in name if ch.isalnum()) + "_img2pdf.pdf"
            img2pdf.default_dpi = 72.0
            with open(os.path.join(self.path,'Output',name),"wb") as f:
                f.write(img2pdf.convert(self.imageNameList))
        else:
            firstPath = self.imageNameList[0]
            width, height = Image.open(firstPath).size
            pdf = FPDF(unit="pt", format=[width, height])
            for pagePath in tqdm(self.imageNameList):
                pdf.add_page()
                pdf.image(pagePath,0,0)
            if not os.path.exists(os.path.join(self.path,'Output')):
                os.mkdir(os.path.join(self.path,'Output'))
            name = str(self.name[:min(10,len(self.name))]).replace(" ","")
            name = ''.join(ch for ch in name if ch.isalnum()) + ".pdf"
            pdf.output(os.path.join(self.path,'Output',name),"F")
