import numpy as np
import trimesh

# load a file by name or from a buffer
scene = trimesh.load('proba_smpl.obj')

# is the current mesh watertight?
scene.is_watertight

# what's the euler number for the mesh?
scene.euler_number

# the convex hull is another Trimesh object that is available as a property
# lets compare the volume of our mesh with the volume of its convex hull
np.divide(scene.volume, scene.convex_hull.volume)

# since the mesh is watertight, it means there is a
# volumetric center of mass which we can set as the origin for our mesh
scene.vertices -= scene.center_mass

# what's the moment of inertia for the mesh?
scene.moment_inertia

# if there are multiple bodies in the mesh we can split the mesh by
# connected components of face adjacency
# since this example mesh is a single watertight body we get a list of one mesh
# mesh.split()

# preview mesh in a pyglet window from a terminal, or inline in a notebook
scene.show()

# facets are groups of coplanar adjacent faces
# set each facet to a random color
# colors are 8 bit RGBA by default (n,4) np.uint8
# for facet in scene.facets:
#     scene.visual.face_colors[facet] = trimesh.visual.random_color()

# transform method can be passed a (4,4) matrix and will cleanly apply the transform
scene.apply_transform(trimesh.transformations.random_rotation_matrix())

# an axis aligned bounding box is available
scene.bounding_box.primitive.extents

# a minimum volume oriented bounding box is available
scene.bounding_box_oriented.primitive.extents

scene.bounding_box_oriented.primitive.transform

# the bounding box is a trimesh.primitives.Box object, which subclasses
# Trimesh and lazily evaluates to fill in vertices and faces when requested
scene.bounding_box_oriented.show()

# bounding spheres and bounding cylinders of meshes are also
# available, and will be the minimum volume version of each
# except in certain degenerate cases, where they will be no worse
# than a least squares fit version of the primitive.
(scene.bounding_box_oriented.volume, scene.bounding_cylinder.volume, scene.bounding_sphere.volume)