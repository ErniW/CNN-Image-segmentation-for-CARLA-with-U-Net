# CNN-Image-segmentation-for-CARLA-with-U-Net
Implementation of image segmentation task for autonomous car driving via U-Net architecture.

- Dataset comes with pickle files for images and masks separately. They were downsized to speed training time at cost of quality (I'm aware of it).
- You can use any kind of data for U-Net. For dataset preparation please refer to `pack_images.py` script (to run script type `python pack_images.py "./dataset/images"` - there you should have images and masks folder).