import omni.replicator.core as rep
with rep.new_layer():
    cubes = rep.create.cube(
        semantics=[("class", "cube")],
        position=(0, 0, 2),
        scale = 3,
        count=1,
    )
    cylinder_light = rep.create.light(
        position = (0, 0, 10),
        rotation=rep.distribution.uniform((0,-0,-180), (0,0,180)),
        intensity=rep.distribution.normal(300000, 2),
        temperature=rep.distribution.normal(6500, 4000),
        light_type="cylinder")
    plane = rep.create.plane(
        position=(0, 0, 0),
        rotation=(0, 0, 0),
        scale=50,
        semantics=[("class", "ground")]
    )