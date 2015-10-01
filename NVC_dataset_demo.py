
# coding: utf-8

# In[1]:

get_ipython().magic(u'matplotlib inline')
import sys
import os
sys.path.append('python_lib')
from class_nvc_dataset import NvcDataset


# In[2]:

annotation_path = os.path.join('annotations', 'NVC_v201509_trainval.json')
image_root = 'images'

# Load annotations
dataset = NvcDataset(annotation_path, image_root)

# Load pre-calculated image features (VggNet layer 15 feature, optional)
image_features_path = os.path.join('cache', 'NVC_v201509_image_feat_VGGnet.npy')
dataset.load_image_features(image_features_path)


# In[3]:

# Get and print the concepts in the dataset
concepts = dataset.getter_concepts()
print 'Concepts: %s' % ', '.join(concepts)

# Get the image and annotations of the speficied concepts
# Each annotations are representated by a python dictionary with the following keys:
#   - 'concept': novel concepts for the image
#   - 'image_id': unique id for the image
#   - 'image_name': file name for the image
#   - 'train_val_test_split': 'train' or 'val' or 'test'
#   - 'img_feat_vgg': an OPTIONAL image feature vector (vggnet in this case) for the image
#   - 'sentences': a list, each element of the list is a dictionary:
#     - 'raw': a string which is the raw annotated sentence
#     - 'tokens': tokenized sentence, NOT includes the period at the end
#     - 'sentence_id': unique id for the sentence
#     - 'image_id': unique image id that the sentence belongs
concepts_interested = ['kiss', 't-rex', 'tai-ji']
image_list = dataset.getter_image_data_list(concepts_interested, 'train')
print 'Get %d images' % len(image_list)


# In[4]:

dataset.visualize_image_data(image_list[0])


# In[5]:

dataset.visualize_image_data(image_list[69])


# In[6]:

dataset.visualize_image_data(image_list[115])

