# Omniverse Synthetic Data Generation
In this Repo you can find how to leverage NVIDIA Omniverse Isaac-sim and Python to generate synthetic data and training on [Ultralytics YOLOv8](https://docs.ultralytics.com/) model.

Our task is to generate the **product sticker** outside of the product's package. Because each product need 3 hours to build up and wrap up, so it need much time to get a large amounts of data to train a detection model, and the data collected manually might not have good quality, this process is time comsuming and cost inefficiency.  

Using `Synthetic data` to replace real-world collected data is an ideal way to solve the problems above, it can reduce the manually cost, and save a lot of time. Let's start it!
<figure style="text-align:center;">
  <img src="https://github.com/leekunhan/transfer_learning_omniverse/assets/85284680/0044b35b-09c9-4a5b-b7ce-6cb70af2f637" alt="圖片說明" style="max-width:80%;">
  <figcaption style="margin-top:10px;">Picture：High-level architecture of Isaac-sim & Replicator。</figcaption>
</figure>

### What will add later
---
* [NVIDIA TAO Toolkit](https://developer.nvidia.com/tao-toolkit)
### Some Resource
---
* [Replicator API](https://docs.omniverse.nvidia.com/py/replicator/1.5.1/source/extensions/omni.replicator.core/docs/API.html)
* [Replicator Docs](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html#theory-behind-training-with-synthetic-data)
* [Script Editor Docs](https://docs.omniverse.nvidia.com/extensions/latest/ext_script-editor.html)
