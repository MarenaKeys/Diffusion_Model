
# Summer Research: Stable Diffusion Models 


## Task 1: Tutorial on Generative Modeling##

-  Task 1/Tutorial Video <br/>
-  Slides: https://docs.google.com/presentation/d/1-wqg4TmuoHn_27VloxSIcTxclBT9nwbPXd8IxFcXxto/edit?usp=sharing



## Task 2: Pytorch Tutorial ##

The resulting path shows how to compute basic matrix operations using Pytorch <br/>
Results: Task 2/TensorMath.py <br/>

https://github.com/MarenaKeys/Diffusion_Model/tree/36c4e8b2b8e75bfd9e119daf669055dff76a423b/Task%202




## Task 3: Pretrained Models ##

For the first notebook, I used images of cats to train the model and for the second model, I used images of yorkies. The resulting images of the first model were more realistic compared to the images produced in the second model.
 
1. The model that is finetuned based on cat images is available via
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)(https://github.com/MarenaKeys/Diffusion_Model/blob/main/Task%203/Fast_DreamBooth_(Cats).ipynb)
Hugging Face: mkeys20/cats-random<br/>

![00001-2045230319 (1)](https://github.com/user-attachments/assets/69904cc7-04cf-4c74-b4f5-a94e6d458aed)

2. Colab Notebook Link (Yorkies): https://colab.research.google.com/drive/1OotPx46vZvCVeLLn0PIBSrRwFAv6bteE?usp=sharing
<img width="312" alt="Screenshot 2024-07-25 at 9 51 30 AM" src="https://github.com/user-attachments/assets/f909cbec-0975-4da1-95ba-5915357f0f84">

## Task 4: Custom Dataset ##

For this task, I used the [COCO API Demo](https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocoDemo.ipynb) to finetune a model that uses a metadata.jsonl file to load and display captions for a unique subset of images. [COCO](https://cocodataset.org/#download) is a large dataset that can be used for image captioning, object detection, and segmentation. I specifically worked with the 2014 dataset.

- Colab Notebook Link: https://colab.research.google.com/drive/1t9fXUIVZRv5nSO1zlXleNA-bR5AJyiJj?usp=sharing
- Hugging Face: mkeys20/CustomCOCO
- Path: Task 4/CustomCOCO.ipynb<br>
- Generate random metadata.jsonl files: https://colab.research.google.com/drive/1nHs9pkYo7gycqPvoo6CSrLvRBxywn4Sr?usp=sharing

Below are examples of images along with their captions that my model generated:

<img width="650" alt="Screenshot 2024-07-27 at 3 02 58 PM" src="https://github.com/user-attachments/assets/1028626f-c66f-454e-82b1-a34666a30af2">


<img width="754" alt="Screenshot 2024-07-25 at 9 54 08 AM" src="https://github.com/user-attachments/assets/75b095a2-cc29-4fb4-a06f-3a758f059843">


## Task 5: Understanding Stable Diffusion & UNet Architecture 
- I learned about the different components of a UNet and how to build one using Google Colab. I looked at the internal compenents of stable diffusion.
- Colab Notebooks: https://colab.research.google.com/drive/1TvOlX2_l4pCBOKjDI672JcMm4q68sKrA?usp=sharing <br> https://colab.research.google.com/drive/1mm67_irYu3qU3hnfzqK5yQC38Fd5UFam?usp=sharing

<img width="715" alt="Screenshot 2024-07-18 at 10 56 24 AM" src="https://github.com/user-attachments/assets/4b783c57-19c3-493b-91f1-05dd15bc4db4">

## Task 6: MNIST Dataset
The MNIST dataset consists of ....
<img width="605" alt="Screenshot 2024-07-27 at 2 56 57 PM" src="https://github.com/user-attachments/assets/8040a7a2-126a-416f-8bef-79f94ba67c60">

