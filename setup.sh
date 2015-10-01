# download and extract images
wget -O ./images/NVC_images.tar.gz https://www.stat.ucla.edu/~junhua.mao/projects/child_learning_folder/NVC_images.tar.gz
cd ./images
tar -xzf NVC_images.tar.gz
cd ..

# download pre-calculated VggNet features
wget -O ./cache/NVC_v201509_image_feat_VGGnet.npy https://www.stat.ucla.edu/~junhua.mao/projects/child_learning_folder/NVC_v201509_image_feat_VGGnet.npy