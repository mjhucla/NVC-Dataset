# download and extract images
mkdir ./images
wget -O ./images/NVC_v201509_images.tar.gz www.stat.ucla.edu/~junhua.mao/projects/child_learning_folder/NVC_v201509_images.tar.gz
cd ./images
tar -xzf NVC_v201509_images.tar.gz
rm NVC_v201509_images.tar.gz
cd ..

# download pre-calculated VggNet features
mkdir ./cache
wget -O ./cache/NVC_v201509_image_feat_VGGnet.npy www.stat.ucla.edu/~junhua.mao/projects/child_learning_folder/NVC_v201509_image_feat_VGGnet.npy
