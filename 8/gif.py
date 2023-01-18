import os
import imageio

file_list = sorted(os.listdir("D:\PY1\PY\8\m"))

Image = []
for f in file_list:
    file_path = "D:/PY1/PY/8/m/" + f
    image = imageio.imread(file_path)
    Image.append(image)

imageio.mimsave("my_gif.gif",Image,fps=4)