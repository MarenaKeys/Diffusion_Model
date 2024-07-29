
# Summer Research: Stable Diffusion Models 
My research

## Task 1: Tutorial on Generative Modeling

This [Tutorial](https://www.youtube.com/watch?v=cS6JQpEY9cs) explains the foundations of Denoising Diffusion Probabilistic Models (DDPMs), generative models, and advanced techniques. Other applications of diffusion models are discussed such as medical imaging and image-to-image. 



## Task 2: Pytorch Tutorial 

This [Section](https://github.com/MarenaKeys/Diffusion_Model/tree/main/Task%202) shows how to compute matrix operations using Pytorch along with others basics such as how to construct a neural network and other math operations. <br/>

Other [PyTorch Tutorials](https://www.youtube.com/playlist?list=PLhhyoLH6IjfxeoooqP9rhU3HJIAVAJ3Vz) can be found in this YouTube playlist by Aladdin Persson.


## Task 3: Pretrained Models 

For the first notebook, I used images of cats to train the model and for the second model, I used images of yorkies. The resulting images of the first model were more realistic compared to the images produced in the second model.
 
1. The model that is finetuned based on cat images is available via: <br>
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MarenaKeys/Diffusion_Model/blob/main/Task%203/Fast_DreamBooth_(Cats).ipynb)


[![Model on 🤗 ](https://huggingface.co/datasets/huggingface/badges/resolve/main/model-on-hf-md.svg)](https://huggingface.co/mkeys20/cats-random)



![00001-2045230319 (1)](https://github.com/user-attachments/assets/69904cc7-04cf-4c74-b4f5-a94e6d458aed)

2. Colab Notebook Link (Yorkies): [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/MarenaKeys/Diffusion_Model/blob/main/YorkieDreamBooth.ipynb)
   
<img width="1315" alt="Screenshot 2024-07-28 at 8 14 47 PM" src="https://github.com/user-attachments/assets/ffdf2ea5-be18-4153-ae36-7fd797edce3b">

## Task 4: Custom Dataset 

For this task, I used the [COCO API Demo](https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocoDemo.ipynb) to finetune a model that uses a [metadata.jsonl file](https://github.com/MarenaKeys/Diffusion_Model/blob/main/Task%204/metadata.jsonl.json) to load and display captions for a unique subset of images. [COCO](https://cocodataset.org/#download) is a large dataset that can be used for image captioning, object detection, and segmentation. I specifically worked with the 2014 dataset.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/MarenaKeys/Diffusion_Model/blob/main/Task%204/CustomCOCO.ipynb)

[![Model on 🤗 ](https://huggingface.co/datasets/huggingface/badges/resolve/main/model-on-hf-md.svg)](https://huggingface.co/mkeys20/CustomCOCO)


Below are examples of images along with their captions that my model generated:

<img width="650" alt="Screenshot 2024-07-27 at 3 02 58 PM" src="https://github.com/user-attachments/assets/1028626f-c66f-454e-82b1-a34666a30af2">


<img width="754" alt="Screenshot 2024-07-25 at 9 54 08 AM" src="https://github.com/user-attachments/assets/75b095a2-cc29-4fb4-a06f-3a758f059843">


## Task 5: Understanding Stable Diffusion & UNet Architecture 
- I learned about the different components of a UNet and how to build one using Google Colab. I looked at the internal compenents of stable diffusion.
Colab Notebooks by Binxu Wang: <br> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1TvOlX2_l4pCBOKjDI672JcMm4q68sKrA?usp=sharing)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1mm67_irYu3qU3hnfzqK5yQC38Fd5UFam?usp=sharing#scrollTo=xiDr0zU3tAbR)
<img width="715" alt="Screenshot 2024-07-18 at 10 56 24 AM" src="https://github.com/user-attachments/assets/4b783c57-19c3-493b-91f1-05dd15bc4db4">

## Task 6: Cross Attention/MNIST Dataset
The MNIST dataset consists of ....

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Y5wr91g5jmpCDiX-RLfWL1eSBWoSuLqO?usp=sharing#scrollTo=PyG11jszkaYM)

<img width="605" alt="Screenshot 2024-07-27 at 2 56 57 PM" src="https://github.com/user-attachments/assets/8040a7a2-126a-416f-8bef-79f94ba67c60">

