# Omni.replicator.core
omni.replicator.core is an open core API in Isaac Sim, featuring multiple functions to control meshes and objects. It is a crucial component in SDG pipelines.

We will talk most of the important API in SDG pipeline, more details can see in the [docs](https://docs.omniverse.nvidia.com/py/replicator/1.5.1/source/extensions/omni.replicator.core/docs/API.html).  

- [Omni.replicator.core](#omnireplicatorcore)
  - [Create](#create)
    - [Camera](#camera)
    - [Object](#object)
    - [light](#light)
    - [Material](#material)
    - [different path](#different-path)
  - [Get](#get)
  - [Modify](#modify)
  - [Randomizer](#randomizer)
  - [Triggers](#triggers)
  - [Physics](#physics)
---
`Create` and `Get` are foundational operations in SDG. Typically, the `Create` function is used in conjunction with `Distribution` to manage resources effectively.
## Create
### Camera 
* camera
* stereo_camera

### Object
* cone
* cube
* cylinder
* disk
* plane
* sphere
* torus

### light
* light

### Material
* OmniPBR Material

### different path
* from_dir
* from_usd
* group



## Get
* prims

---
`Modify` is used to change the behaviors of existing objects, such as their position, scale, and radius, depending on the object's properties.
## Modify

## Randomizer
Most of the time, `Randomizer` will also conjunction with `Distribution`.
## Triggers


---
add property
## Physics
* collider
* mass
* physics_material
* rigid_body