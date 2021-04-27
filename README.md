# Image Tailor

![logo](assets/logo.jpg)

Photo by <a href="https://unsplash.com/@bady?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">bady abbas</a> on <a href="https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

Image tailor is an open source image creator.
Use cut-off, stitching or other method to generate pictures

## Component
Currently, Image Tailor have 3 components:
- `ImagesLoader` Image loader class
- `JigsawPuzzle` Mosaic data augmentation
  - refer: [YOLOv4: Optimal Speed and Accuracy of Object Detection](https://arxiv.org/abs/2004.10934v1)
    - Figure 3: Mosaic represents a new method of data augmentation.
    - 4.2. Influence of different features on Classifier training
    - 7. Acknowledgements [link](https://github.com/ultralytics/yolov3)
- `StickerPlayer` Mixing-and-Pasting Generator

## Example
All examples are under `src/example`, please refer these code slices as quick start.
