import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# 0< image >= 2, if list show two image side by side
def show_image(image, size=(8, 6), order="stack", tricks=False):    
    
    fig = plt.figure(figsize=size)    
    if isinstance(image, list): 
        if order == "stack":            
            rows = len(image)
            pos = range(1, rows + 1)            
            for i in range(rows):
                ax = fig.add_subplot(rows,1,pos[i])
                ax.imshow(image[i])
                if not tricks:                
                    ax.set(xticks=[], yticks=[])
        else:
            cols = len(image)
            pos = range(1, cols + 1)            
            for i in range(cols):
                ax = fig.add_subplot(1, cols,pos[i])
                ax.imshow(image[i])
                if not tricks:                
                    ax.set(xticks=[], yticks=[])
                
    elif isinstance(image, np.ndarray):
        # when single image
        ax = fig.subplots(nrows=1, ncols=1, sharey='row')
        ax.imshow(image)
        if not tricks:                
            ax.set(xticks=[], yticks=[])
    else:
#         ax = fig.subplots(1, 1, sharey='row')
        plt.text(0.35, 0.5, 'Sorry no image content found, Close Me!', dict(size=30))
    

# 0< image >= 2, if list show two image side by side
def show_image_cube(image, size=(8, 6), tricks=False):    
    
    fig2 = plt.figure(constrained_layout=True, figsize=size)
    spec2 = gridspec.GridSpec( ncols=len(image[0]), nrows=len(image), figure=fig2)
    
    for ci, colImage in enumerate(image):        
        for ri, rowImage in enumerate(colImage):            
            ax = fig2.add_subplot(spec2[ci, ri])            
            ax.imshow(rowImage)            
            if not tricks:                
                ax.set(xticks=[], yticks=[])
				
				


class Shred:
    def __init__(self, image, shredType="Default"):
        self.image = image
        self.shredType = ""
    
    def __repr__(self):
        return self.image
    
    def default(self, angel="h", size=10, percent=False):
        shredImage = []
        if percent:            
            size = int((size*self.image.shape[0])/100)          
            cuts = range(int(self.image.shape[0]/size))
        else:
            cuts = range(int(self.image.shape[0]/size))
        left, top, = 0, 0
        
        width = size
        
        if angel == "h":
            
            for cut in cuts:                         
                shred = self.image[top:top+width, left:]
                shredImage.append(shred)
                top += size
                if (top+size) > self.image.shape[0]:                
                    shred = self.image[top:,:]# rowshered                    
                    if all(shred.shape):
                        shredImage.append(shred)
#                         show_image(shred)
                
        else:
            for cut in cuts:                         
                shred = self.image[:, width-size:width]
                shredImage.append(shred)                                    
                if (width+size) > self.image.shape[0]:                
                    shred = self.image[:, width:]# rowshered                    
                    if all(shred.shape):
                        shredImage.append(shred)
#                         show_image(shred)
                width += size
        return shredImage
    
    def cubic(self, angle="h", size=(10, 10), percent=False):
        # first defult v and then h
        # or crop each part and appen in 2d array
        size = list(size)
        shredImage = [] # 2d list rows/cols
                
        if percent:
            # h percentage
            size[0] = (int((size[0]*self.image.shape[0])/100))
            # w percentage
            size[1] = (int((size[1]*self.image.shape[0])/100))        
            print(size)

        left, top, = 0, 0

        height = size[0]
        width = size[1]
        
        colCut = range(int(self.image.shape[0]/height)) # height        
        rowCut = range(int(self.image.shape[1]/width)) # width
        
        colShredList = []
        for cCut in colCut:                     
            colShred = self.image[top:top+height, left:]
            colShredList.append(colShred)
#             show_image(colShred)
            
            top += height
            
            if (top+size[0]) > self.image.shape[0]:
                colShred = self.image[top:, left:]
                if all(colShred.shape):
                    colShredList.append(colShred) 
#                 show_image(colShred)

                     
#         colImage = colShredList[0]         #tempTop:tempTop+width 
        for colImage in colShredList:
            rowShred = []   
            print("[INFO : ColShape] ",colImage.shape)
            if colImage.shape[0] == size[0]:
                width = size[1]
                for i in rowCut:                        
                    cellShred = colImage[:, width-size[1]:width]# rowshered                 
                    rowShred.append(cellShred) 
#                     show_image(cellShred)
#                     print(cellShred.shape)

#                     # adding extrat part at last
                    if (width+size[1]) > colImage.shape[1]:                
                        cellShred = colImage[:, width:]# rowshered   
                        if all(cellShred.shape):
                            rowShred.append(cellShred)
#                             print("[INFO : RowShape] ",cellShred.shape)

#                         show_image(cellShred)
                    width += size[1]
                shredImage.append(rowShred)
            else:                
                width = size[1]
                for i in rowCut:            
                    cellShred = colImage[:, width-size[1]:width]# rowshered                 
                    rowShred.append(cellShred) 
#                     show_image(cellShred)
#                     print(cellShred.shape)

#                     # adding extrat part at last
                    if (width+size[1]) > colImage.shape[1]:                
                        cellShred = colImage[:, width:]# rowshered
                        if all(cellShred.shape):
                            rowShred.append(cellShred)
#                             print("[INFO : RowShape] ",cellShred.shape)
#                         show_image(cellShred)
                    width += size[1]
                shredImage.append(rowShred)
        return shredImage
    
    def hexagon(self, size=10):
        pass
    def show_image(self):
        # use above funciton to display image
        pass
    def test_shred(self):
        # show_image(np.concatenate(shl, axis=1))
        pass