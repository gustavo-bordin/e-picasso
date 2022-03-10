# Picasso
## An automated art generator

Powered by NVIDIA GauGAN® / NVIDIA Canvas
[![NVIDIA](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8f660QLE5xkEUQCbra7abUYewsH0krs9EOpKbdiQqi_7i8Mp0z-OW0--5tU2qe42vNy8&usqp=CAU)](https://www.nvidia.com/en-us/studio/canvas/)

Picasso allows you to input any image, this image is going to be processed by an Artificial Inteligence from Nvidia, and it will output another image, based on the first one.

## Features

- Generate an image using another image

## Flow
1. Reads all the image files inside input_images folder
2. Iterates through the files
3. Posts each file to the Nvidia Amazon Storage
4. Gets the ouput image already processed
5. Deletes the input image

## Files and folders
- **/output_images**
   - Where the output images will be saved, after being processed by the AI
- **/input_images**
   - Where you should put the images you want to process
- **/core**
   - Where the core files are, the ones that does the major part of Picasso
- **picasso.py**
   - Entrypoint file, where it calls all the other functionalities to start the execution
- **image_handler.py**
   - A class for handling everything that has to do with images, like saving, deleting, generating a name for them, etc.
- **inferer.py**
  - A class for handling the part of inputing the image to the NVIDIA servers.
- **receiver.py**
  - A class for handling the part of getting the processed image from the NVIDIA servers.