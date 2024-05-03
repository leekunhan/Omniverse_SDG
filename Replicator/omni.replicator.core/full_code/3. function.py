import omni.replicator.core as rep
import numpy as np

with rep.new_layer():
    rep.set_global_seed(np.random.randint(0, 1000))
    # Create light
    distance_light = rep.create.light(
        position = (0, 0, 10),
        rotation=(0, 0, 0),
        intensity=300000,
        temperature=6500,
        light_type="cylinder")

    # Create ground plane
    plane = rep.create.plane(
        position=(0, 0, 0),
        rotation=(0, 0, 0),
        scale=50,
        semantics=[("class", "ground")]
        )

    torus = rep.create.torus(
            position=(0, 0, 0),
            count=1,
            scale = 10,
            semantics=[("shape", "torus")]
        )
    mat = rep.create.material_omnipbr(
        diffuse=rep.distribution.uniform((0, 0, 0), (1, 1, 1)),
        roughness=rep.distribution.uniform(0, 1),
        metallic=rep.distribution.choice([0, 1]),
        emissive_color=rep.distribution.uniform((0, 0, 0.5), (0, 0, 1)),
        emissive_intensity=rep.distribution.uniform(0, 1000),
        count = 10
        )
    def mat_change():
        with torus:
            rep.modify.pose(position=rep.distribution.uniform((-25, -25, 0), (25, 25, 0)),
                            rotation = rep.distribution.uniform((0, 0, -180),(0, 0, 180)))
            rep.randomizer.materials(mat)
rep.randomizer.register(mat_change)
with rep.trigger.on_frame(max_execs = 100, interval =5):
    rep.randomizer.mat_change()