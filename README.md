# Omniverse Synthetic Data Generation
In this repository, you will discover how to utilize NVIDIA Omniverse Isaac-sim along with Python for generating synthetic data and training the [Ultralytics YOLOv8](https://docs.ultralytics.com/) model.

Our task is to generate the **product sticker** to be placed outside the product's packaging. Given that each product requires three hours for assembly and packaging, accumulating a large dataset for training a detection model is time-consuming and inefficient, especially when the manually collected data may not be of high quality.

Utilizing `Synthetic data` as a substitute for real-world collected data offers a perfect solution to the aforementioned issues. It significantly reduces manual labor costs and saves considerable time. As illustrated below, the Omniverse supports RTX Rendering and a Simulation engine, enabling the simulation of real-world data. Moreover, through the use of the application layer above, it is possible to harness the Replicator and employ API code to randomly orchestrate and generate a diverse array of synthetic data.
<p align="center">
<img src="https://github.com/leekunhan/transfer_learning_omniverse/assets/85284680/0044b35b-09c9-4a5b-b7ce-6cb70af2f637" style="max-width:80%;height:auto;">  
</p>
<p align="center">
Picture：High-level architecture of Isaac-sim & Replicator
</p>

Let's start it! [Click](./turtorial)

### Notice 
--- 
**If you are new to Omniverse I `strongly` recommend reading the following contents to become more acquainted with this platform.**
* [Download Omniverse SDK](https://www.nvidia.com/zh-tw/omniverse/download/)
* [Omniverse Developer Guide Overview](https://docs.omniverse.nvidia.com/dev-guide/latest/index.html)
* [OpenUSD Overview](https://docs.omniverse.nvidia.com/usd/latest/index.html)
* [What Is Isaac Sim?](https://docs.omniverse.nvidia.com/isaacsim/latest/overview.html)
* [Youtube - Getting Started in NVIDIA Omniverse](https://youtube.com/playlist?list=PL4w6jm6S2lztLazLC7P0I4SnX3gxdL1Ad&si=53X1ctpgo9Yc0pEn)

### Upcoming Additions
---
* [NVIDIA TAO Toolkit](https://developer.nvidia.com/tao-toolkit)
### Resources
---
* [Replicator API](https://docs.omniverse.nvidia.com/py/replicator/1.5.1/source/extensions/omni.replicator.core/docs/API.html)
* [Replicator Docs](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html#theory-behind-training-with-synthetic-data)
* [Script Editor Docs](https://docs.omniverse.nvidia.com/extensions/latest/ext_script-editor.html)
* [**GTC2024 - Empower Virtual Collaboration for Digital Twins Through Omniverse**](https://www.nvidia.com/en-us/on-demand/session/gtc24-s63282/)
* [Youtube - Generate Synthetic Data with Omniverse Replicator](https://www.youtube.com/watch?v=amVjqaABfU8&ab_channel=NVIDIAOmniverse)
* [Youtube - Deep Dive: Omniverse Replicator](https://www.youtube.com/watch?v=AGtIV5xgpYc&ab_channel=NVIDIAOmniverse)
* [Youtube - Randomizing a Scene with NVIDIA Omniverse Replicator](https://www.youtube.com/watch?v=5gBRbFqmZSE&ab_channel=NVIDIAOmniverse)
* [Youtube - Boosting Perception Model Training with Synthetic Data](https://www.youtube.com/watch?v=pR-vuZr7SiY&t=202s&ab_channel=SnorkelAI)
* [ultralytics/ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)

### Hardware Utilized
* NVIDIA RTX4060Ti 16GB