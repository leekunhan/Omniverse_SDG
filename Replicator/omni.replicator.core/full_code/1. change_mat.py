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
    
    mat1 = rep.create.material_omnipbr(
        diffuse=rep.distribution.uniform((0, 0, 0), (1, 1, 1)),
        roughness=rep.distribution.uniform(0, 1),
        metallic=rep.distribution.choice([0, 1]),
        emissive_color=rep.distribution.uniform((0, 0, 0.5), (0, 0, 1)),
        emissive_intensity=rep.distribution.uniform(0, 1000),
        )

    mat2 = rep.create.material_omnipbr(
        diffuse_texture=rep.distribution.choice(rep.example.TEXTURES),
        roughness_texture=rep.distribution.choice(rep.example.TEXTURES),
        metallic_texture=rep.distribution.choice(rep.example.TEXTURES),
        emissive_texture=rep.distribution.choice(rep.example.TEXTURES),
        emissive_intensity=rep.distribution.uniform(0, 1000)
        )
    
    # Create torus
    torus = rep.create.torus(
        position=(0, 0, 0),
        count=1,
        scale = 10,
        material = mat1,
        semantics=[("shape", "torus")]
    )

    # Create cube
    cube = rep.create.cube(
        position=(0, -15, 5),
        count=1,
        scale = 10,
        material = mat2,
        semantics=[("shape", "cubes")]
    )

    