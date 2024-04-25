# Omni.replicator.core
omni.replicator.core is an open core API in Isaac Sim, featuring multiple functions to control meshes and objects. It is a crucial component in SDG pipelines.

First let's use below import code to import API
```py
import omni.replicator.core as rep
```

We will talk most of the important API in SDG pipeline, more details can see in the [docs](https://docs.omniverse.nvidia.com/py/replicator/1.10.10/source/extensions/omni.replicator.core/docs/API.html#module-omni.replicator.core.trigger).  

- [Omni.replicator.core](#omnireplicatorcore)
  - [Create](#create)
    - [Object](#object)
    - [light](#light)
    - [Material](#material)
    - [different path](#different-path)
  - [Distribution](#distribution)
  - [Get](#get)
  - [Modify](#modify)
  - [Randomizer](#randomizer)
  - [Triggers](#triggers)
  - [Physics](#physics)
  - [Replicator Orchestration](#replicator-orchestration)
    - [Preview SDG](#preview-sdg)
    - [Run SDG](#run-sdg)
    - [Stop SDG](#stop-sdg)
---
`Create` and `Get` are foundational operations in SDG. Typically, the `Create` function is used in conjunction with `Distribution` to manage resources effectively.
## Create
use create class such as ```rep.create.[cone, cube, light ... ]```

### Object
* rep.create.cone
* rep.create.cube
* rep.create.cylinder
* rep.create.disk
* rep.create.plane
* rep.create.sphere
* rep.create.torus

the above objects have same parameters can use  
**parameters**
* position: Union[ReplicatorItem, float, Tuple[float]] = None, 
* scale: Union[ReplicatorItem, float, Tuple[float]] = None
* pivot: Union[ReplicatorItem, Tuple[float]] = None
* rotation: Union[ReplicatorItem, float, Tuple[float]] = None
* look_at: Union[ReplicatorItem, str, Path, Tuple[float, float, float]] = None
* look_at_up_axis: Union[ReplicatorItem, Tuple[float]] = None
* semantics: List[Tuple[type: str, data: str]] = None
* material: Union[ReplicatorItem, Prim] = None
* visible: bool = True
* as_mesh: bool = True
* count: int = 1

### light
* rep.create.light

**parameters**  
* rotation: Union[ReplicatorItem, float, Tuple[float]] = None
* count: int = 1 
* light_type: str ["cylinder", "disk", "distant", "dome", "rect", "sphere"] = None
* color: Union[ReplicatorItem, Tuple[float, float, float]] = (1.0, 1.0, 1.0)
* intensity: Union[ReplicatorItem, float] = 1000.0
* exposure: Union[ReplicatorItem, float] = None
* temperature: Union[ReplicatorItem, float] = 6500


### Material
* rep.create.material_omnipbr

**parameters**
* count: int = 1
* diffuse_texture: str = None

### different path
* from_dir
* from_usd
  * items: List[Union[ReplicatorItem, str, Path]]
  * semantics: List[Tuple[str, str]] = None

## Distribution
* rep.distribution.choice
* rep.distribution.log_uniform
* rep.distribution.normal
* rep.distribution.sequence
* rep.distribution.uniform

**parameters**
* lower: Tuple
* upper: Tuple
* num_samples: int = 1
* seed: Optional[int] = None
* name: Optional[str] = None

* rep.distribution.combine  

**parameters**
* items: list
* name: Optional[str] = None

## Get
* rep.get.prims

**parameters**
* path_pattern: str = None
* path_pattern_exclusion: str = None
* prim_types: Union[str, List[str]] = None
* prim_types_exclusion: Union[str, List[str]] = None
* semantics: Union[List[Tuple[str, str]], Tuple[str, str]] = None
* semantics_exclusion: Union[List[Tuple[str, str]], Tuple[str, str]] = None
* cache_result: bool = True

## Modify
`Modify` is used to change the behaviors of existing objects, such as their position, scale, and radius, depending on the object's properties.

1. rep.modify.pose

**parameters**
* position: Union[ReplicatorItem, float, Tuple[float]] = None
* rotation: Union[ReplicatorItem, float, Tuple[float]] = None
* rotation_order: str = 'XYZ'
* scale: Union[ReplicatorItem, float, Tuple[float]] = None
* size: Union[ReplicatorItem, float, Tuple[float]] = None
* pivot: Union[ReplicatorItem, Tuple[float]] = None
* look_at: Union[ReplicatorItem, List[Union[str, Path]]] = None
* look_at_up_axis: Union[str, Tuple[float, float, float]] = None
* input_prims: Union[ReplicatorItem, List[str]] = None

---
2. rep.modify.semantics

**parameters**
* semantics: List[Tuple[str, str]] = None
* input_prims: Union[ReplicatorItem, List[str]] = None

---
3. rep.modify.visibility

**parameters**
* value: Union[ReplicatorItem, List[bool]] = None

## Randomizer
Most of the time, `Randomizer` will also conjunction with `Distribution`.

1. rep.randomizer.register
Register a new function under omni.replicator.core.randomizer

**parameters**
* fn: Callable[[...]
* Union[ReplicatorItem, Node]], override: bool = True

2. rep.randomizer.rotation

**parameters**
* min_angle: Tuple[float, float, float] = (- 180.0, - 180.0, - 180.0)
* max_angle: Tuple[float, float, float] = (180.0, 180.0, 180.0),

3. rep.randomizer.materials

**parameters**
* materials: Union[ReplicatorItem, List[str]]

4. rep.randomizer.color

**parameters**
* colors: Union[ReplicatorItem, List[Tuple[float]]]

## Triggers
Triggers is use to represent the replicator result in omniverse

---
add property
## Physics
* rep.physics.collider
approximation_shape: str

* rep.physics.rigid_body
velocity: Union[ReplicatorItem, Tuple[float, float, float]] = (0.0, 0.0, 0.0)

## Replicator Orchestration
### Preview SDG
In the script editor, run `rep.orchestrator.preview()`

In the toolbar, find the Replicator menu and select Preview

### Run SDG
In the script editor, run `rep.orchestrator.run()`

In the toolbar, find the Replicator menu and select Run

### Stop SDG
In the script editor, run `rep.orchestrator.stop()`

In the toolbar, find the Replicator menu and select Stop