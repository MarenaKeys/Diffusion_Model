
# Summer Research: Stable Diffusion Models 

My research consists of learning about generative models, specifically Stable Diffusion and Denoising Diffusion Probabilistic Models. Throughout this process, I learned how to create custom datasets, fine-tune models, and the internal structure of stable diffusion.

<br> Through this repository, I will walk you through the tasks I worked on in able to fine-tune my own model as well as understanding the components and internal architecture of stable diffusion.

**Generative Models & Stable Diffusion**
- Generative Models are models that generate new samples based on the data learned during training
- Stable Diffusion is a generative model that makes images from text prompts

** Denoising Diffusion Probabilistic Models**
-
<img width="1046" alt="Screenshot 2024-06-17 at 10 46 10 AM" src="https://github.com/user-attachments/assets/64afcbe5-7aed-4448-9992-db3e08ae6f99">


**Fine-tuning Method**

DreamBooth is a machine learning technique where one can train (fine-tune) a pretrained model to create a custom set of images. I used Google Colab, similar to Jupyter, to test and run the models.




## Task 1: Tutorial on Generative Modeling

This [Tutorial](https://www.youtube.com/watch?v=cS6JQpEY9cs) explains the foundations of Denoising Diffusion Probabilistic Models (DDPMs), generative models, and advanced techniques. Other applications of diffusion models are discussed such as medical imaging and image-to-image. 



## Task 2: Pytorch Tutorial 

This [Section](https://github.com/MarenaKeys/Diffusion_Model/tree/main/Task%202) shows how to compute matrix operations using Pytorch along with others basics such as how to construct a neural network and other math operations. <br/>

Other [PyTorch Tutorials](https://www.youtube.com/playlist?list=PLhhyoLH6IjfxeoooqP9rhU3HJIAVAJ3Vz) can be found in this YouTube playlist by Aladdin Persson.


## Task 3: Pretrained Models 

For this task, I trained two models on Google Colab using DreamBooth. For the first notebook, I used images of cats to train the model and for the second model, I used images of Yorkshire Terriers (Yorkies) dogs. The resulting images of the first model were more realistic compared to the images produced in the second model.

### Getting Started
**Install dependencies** <br>
Both models require certain packages/software to be installed in order to run the model. Below is an example from the notebook trained on Yorkies: <br>
```

!wget -q https://gist.githubusercontent.com/FurkanGozukara/be7be5f9f7820d0bb85a3052874f184e/raw/d8d179da6cab0735bd5832029c2dec5163db87b4/train_dreambooth.py
!wget -q https://github.com/ShivamShrirao/diffusers/raw/main/scripts/convert_diffusers_to_original_stable_diffusion.py
%pip uninstall torchtext --yes
%pip install -qq git+https://github.com/ShivamShrirao/diffusers
%pip install torch==2.2.0 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 --upgrade
%pip install -q -U --pre triton --upgrade
%pip install -q accelerate transformers ftfy gradio natsort safetensors
%pip install bitsandbytes==0.41.3  --upgrade
%pip install xformers==0.0.24  --upgrade
%pip install triton==2.2.0 --upgrade
%pip install diffusers==0.27.0 --upgrade

```

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


## Task 5: Understanding Stable Diffusion & U-Net Architecture 
The following notebooks show the different components of a U-Net and how to build one using Google Colab as well as the internal compenents of stable diffusion. Essentially, the U-Net gets it name from its (U) shape and consists of four encoders (left) and four decoders (right) to process a text prompt and produce an image corresponding to it for example.
Colab Notebooks by Binxu Wang: <br> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1TvOlX2_l4pCBOKjDI672JcMm4q68sKrA?usp=sharing)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1mm67_irYu3qU3hnfzqK5yQC38Fd5UFam?usp=sharing#scrollTo=xiDr0zU3tAbR)
<img width="715" alt="Screenshot 2024-07-18 at 10 56 24 AM" src="https://github.com/user-attachments/assets/4b783c57-19c3-493b-91f1-05dd15bc4db4">

## Task 6: Cross Attention/MNIST Dataset
The MNIST dataset consists of handwritten digits from zero to nine. The following notebook implements the U-Net architecture and trains the model on MNIST dataset in order to show the viewer a working Stable-Diffusion-like model.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Y5wr91g5jmpCDiX-RLfWL1eSBWoSuLqO?usp=sharing#scrollTo=PyG11jszkaYM)

<img width="605" alt="Screenshot 2024-07-27 at 2 56 57 PM" src="https://github.com/user-attachments/assets/8040a7a2-126a-416f-8bef-79f94ba67c60">

## Task 7: Results

Using the custom dataset from Task 4 that consists of one hundred images, I trained the first model, from Task 3, on ten images along with their captions. The following results were shown: <br>

### Insert Colab
### Insert HuggingFace

## Conclusion
