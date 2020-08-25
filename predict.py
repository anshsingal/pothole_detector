import keras
from keras.models import load_model
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
def pred(path):
    model = load_model("prototype model")
    file = Image.open(path)
    img = np.resize(np.array(file), (1, 128, 128, 3))
    test = model.predict(img)
    return file, test[0,0]*100

if __name__=='__main__':
    file, result = pred('C:\\Users\\anshs\\Desktop\\study\\py\\datasets\\input\\pothole-detection-dataset\\normal\\16.jpg')
    print(result, '%')
    plt.imshow(file)
    plt.show()
