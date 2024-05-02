import omni.replicator.core as rep
import numpy as np

with rep.new_layer():
    rep.set_global_seed(np.random.randint(0, 1000))
    # Create light
    distance_light = rep.create.light(
        position = (0, 0, 10),
        rotation=rep.distribution.uniform((0,-0,-180), (0,0,180)),
        intensity=rep.distribution.normal(300000, 2),
        temperature=rep.distribution.normal(6500, 4000),
        light_type="cylinder")
    
    # Create ground plane
    plane = rep.create.plane(
        position=(0, 0, 0),
        rotation=(0, 0, 0),
        scale=50,
        # semantics=[("class", "ground")]
    )

    # Create simple shapes to manipulate
    cubes = rep.create.cube(
        semantics=[("class", "cube")],
        position=rep.distribution.uniform((-25, -25, 0), (25, 25, 0)),
        count=6,
    )

    cones = rep.create.cone(
        semantics=[("class", "cone")],
        position=rep.distribution.uniform((-25, -25, 0), (25, 25, 0)),
        count=10,
    )