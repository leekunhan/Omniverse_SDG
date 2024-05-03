# Add A distance light  
# Add a ground plane  
# Add Cardbox_A1

import omni.replicator.core as rep
import numpy as np

with rep.new_layer():
    rep.set_global_seed(np.random.randint(0, 1000))
    # get box
    def rand_box():
        box = rep.get.xform (path_pattern = "/World/Cardbox_A1") # only can be mesh
        with box :
            rep.modify.pose(position=rep.distribution.uniform((-25, -25, 0), (25, 25, 0)),
                            rotation = rep.distribution.uniform((-15, -15, 0),(15, 15, 0)))
    rep.randomizer.register(rand_box)
    with rep.trigger.on_frame(max_execs = 10, interval =50):
        rep.randomizer.rand_box()