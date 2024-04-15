Table of content
---
- [1. Analyze Task](#1-analyze-task)
- [2. Add CardBox](#2-add-cardbox)
- [3. Generate Sticker](#3-generate-sticker)
  - [String Sticker](#string-sticker)
  - [Information Sticker](#information-sticker)
    - [Generate Barcode](#generate-barcode)
    - [Combine All Elements](#combine-all-elements)
- [4. Add Replicator](#4-add-replicator)
- [5. Add Annotator](#5-add-annotator)
- [6. Train YOLOv8 Model](#6-train-yolov8-model)
---
Workflow can see as below image.
<p align="center">
<img height="300" src="../picture/workflow.png">  
</p>

Clone the repo
```shell
git clone https://github.com/leekunhan/Omniverse_Synthetic_Generation.git
```
change directory to turtorial
```shell
cd turtorial
```
---
# 1. Analyze Task  
We need to know which part we need to do simulate, and we can get this information from analyzing golden data as below picture of this task.    
<p align="center">
<img height="250" src="../picture/golden_data.jpg">  
</p>
<p align="center">
Picture：Golden Data
</p>
as we can see, the target can be shown as below:  

* Five different stickers with important product information.
* One sticker with multiple string.

<p align="center">
<img height="250" src="../picture/golden_data_after.png">  
</p>
<p align="center">
Picture：Targets we are focusing on
</p>
And there is one most important thing. Card Box background.  

Fortunately, there are some pre-build cardbox usd files can use in omniverse(Isaac-sim), so that we don't need to build by ourself.   

We can find card box usd in your nucleus localhost 

# 2. Add CardBox

```
omniverse://localhost/NVIDIA/Assets/ArchVis/Industrial/Containers/Cardboard/
```
<p align="center">
<img height="200" src="../picture/nucleus_cardbox.png">  
</p>

Then you can pick one card box type you like. I'll pick `CardBox_C2.usd`   
and drag it into our scene.

<p align="center">
<img height="200" src="../picture/cardbox.png">  
</p>

# 3. Generate Sticker
Please down all package in requirement run:
```shell
pip install -r requirements.txt
```

Let start from generate easy sticker - String sticker.  
we only need one python package - Pillow.
## String Sticker
Code can be found in [sitcker_generate](./sticker_generate/string_sticker_generater.ipynb)  
1. Generate a blank background.
2. Add random string on it.
3. Save image.
   
<p align="center">
<img height="150" src="../picture/stickers/syn/string_syn.png">  
</p>

**(NOTE: All detail can be change by case)**

## Information Sticker
Let's analyze the most complicated sticker to see what elements we need.
<p align="center">
<img height="250" src="../picture/real_product_sticker.png">  
</p>

**Element:**
* Title (TO:, SO:, PO: ...)
* Information (GBT, Carton ...)
* Barcodes
* Barcode Information (ADN-MB0019-001 ...)
* Straght lines & Horizontal lines

We can seperate these elements to "Can done through Pillow" & "Can't done through Pillow", and there only Barcode can't done through Pillow, So we need to generate it in independent processing.

### Generate Barcode

### Combine All Elements

# 4. Add Replicator

# 5. Add Annotator

# 6. Train YOLOv8 Model