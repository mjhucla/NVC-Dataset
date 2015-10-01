# -*- coding: utf-8 -*-
"""Python class of util function of novel visual concepts dataset.

TODO:
  1. Evaluation functions for the dataset
"""
import os
import logging
import json
import copy
import numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

logger = logging.getLogger('NvcDataset')
FORMAT = "[%(filename)s:line %(lineno)4s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.INFO)

class NvcDataset:
  """Python class of util function of novel visual concepts dataset."""
  def __init__(self, annotation_path, image_root):
    """Load data and initialize the train, val and test set."""
    with open(annotation_path) as fin:
      dataset = json.load(fin)
    logger.info('Dataset loaded with %d novel concepts', 
                len(dataset['concepts']))
    self.version = dataset['version']
    self.concepts = dataset['concepts']
    self.images = dataset['images']
    self.annotation_path = annotation_path
    self.image_root = image_root
    self._generate_category_to_image_index()
    logger.info('Train, val, test set initialized')
    
  def load_image_features(self, image_features_path,
                          image_feature_name='img_feat_vgg'):
    """Load features for the each image.
    
    Args:
      image_features_path: path to the file containing the image features. This
        file should be a numpy dictionary. The key is the image name (same as
        self.images[0]['image_name']. The value is the corresponding image
        feature)
    """
    dct_img_feat = numpy.load(image_features_path).tolist()
    for image in self.images:
      image_name = image['image_name']
      if image_name not in dct_img_feat:
        logger.warn('%s image feature missing!', image_name)
        continue
      image[image_feature_name] = dct_img_feat[image_name]
    
  def getter_image_data_list(self, concepts, split='train',
                             flag_copy=True):
    """Return a list of image data of the specified concepts and set.
    
    Args:
      concepts: a list of concepts
      split: image set that we want to get the image.
        three options: 'train', 'val' or 'test'
      flag_copy: if it is True, return the copy of the list of image_data.
        warning: if it is False, change of the image_data in the returned list 
        will change the original copy in the dataset
        
    Return:
      a list of image data of the specified concepts and set.
    """
    if split == 'train':
      image_set = self.train_set
    elif split == 'val':
      image_set = self.val_set
    elif split == 'test':
      image_set = self.test_set
    else:
      logger.fatal('Unknown set split %s!', split)
    for concept in concepts:
      assert concept in concepts, 'Unknown concept: %s!' % concept
    images = []
    for concept in concepts:
      images = images + image_set[concept]
    if flag_copy:
      return copy.deepcopy(images)
    else:
      return images
    
  def getter_image_path(self, image_data):
    """Return path of the image from image_data."""
    return os.path.join(self.image_root, image_data['concept'], 
                        image_data['image_name'] + '.jpg')
                        
  def getter_concepts(self):
    """Return the list of concepts"""
    return copy.deepcopy(self.concepts)
    
  def visualize_image_data(self, image_data):
    """Visualize the image data."""
    img=mpimg.imread(self.getter_image_path(image_data))
    plt.figure()
    plt.imshow(img)
    plt.axis('off')
    print 'Descriptions:'
    for sentence in image_data['sentences']:
      print '  %s' % sentence['raw']
    
  def _generate_category_to_image_index(self):
    """Private function to set the train, val, and test set.
    
    train_set, val_set, and test_set are dictionaries. Their keys are concepts.
    The value of a key (concept) is the list of image data belongs to the 
    concept.
    """
    train_set = {}
    for concept in self.concepts:
      train_set[concept] = []
    val_set = copy.deepcopy(train_set)
    test_set = copy.deepcopy(train_set)
    
    for image_data in self.images:
      concept = image_data['concept']
      assert concept in self.concepts
      split = image_data['train_val_test_split']
      if split == 'train':
        train_set[concept].append(image_data)
      elif split == 'val':
        val_set[concept].append(image_data)
      elif split == 'test':
        test_set[concept].append(image_data)
      else:
        logger.fatal('Unknown set split %s!', split)
        
    self.train_set = train_set
    self.val_set = val_set
    self.test_set = test_set