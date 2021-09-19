import os
import glob
import random

DATA_DIR_OLD = '../data/xrays/'
DATA_DIR = '../data/chest_xrays/'
COVID_DIR = os.path.join(DATA_DIR,"COVID")
PNEUMONIA_DIR = os.path.join(DATA_DIR,"Viral Pneumonia")
NORMAL_DIR = os.path.join(DATA_DIR,'Normal')

COVID_AUG_DIR = os.path.join(DATA_DIR,"COVID Aug")
PNEUMONIA_AUG_DIR = os.path.join(DATA_DIR,"Viral Pneumonia Aug")

CATEGORY = {'Normal': 0, 'Viral Pneumonia': 1, 'COVID': 2}
LABELS =["COVID",  "Normal", "Viral Pneumonia"]
NUM_CATEGORY = 3

IMAGE_SIZE = 75
EPOCHS = 20
BATCH_SIZE = 16

MODEL_DIR = '../model/'
# MODEL_TEMP_PATH = os.path.join(MODEL_DIR,"model_temp.h5")
# MODEL_PATH = os.path.join(MODEL_DIR,"model.h5")



def get_temp_model_path(model_name):
    return os.path.join(MODEL_DIR,model_name + "_temp.h5")

def get_model_path(model_name):
  return os.path.join(MODEL_DIR,model_name + ".h5")


def get_random_normal_xray():
  img_name = random.choice(os.listdir(NORMAL_DIR))
  img_path = os.path.join(NORMAL_DIR,img_name)
  return img_path

def get_random_pneumonia_xray():
  img_name = random.choice(os.listdir(PNEUMONIA_DIR))
  img_path = os.path.join(PNEUMONIA_DIR,img_name)
  return img_path

def get_random_covid_xray():
  img_name = random.choice(os.listdir(COVID_DIR))
  img_path = os.path.join(COVID_DIR,img_name)
  return img_path