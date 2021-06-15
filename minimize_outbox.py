import bpy
import math
import numpy as np

minimization_steps = 180
obj = bpy.context.object

def align_axis(axis, minimize, steps):
    val = np.ones(steps)
    angle = (math.pi)/steps
    for i in range(steps):
        bpy.ops.transform.rotate(value=angle, orient_axis=axis)
        bpy.ops.object.transform_apply(rotation=True)
        min_val = obj.dimensions[minimize]
        val[i] = min_val

    min_angle = np.argmin(val)
    bpy.ops.transform.rotate(value=angle*min_angle, orient_axis=axis)
    bpy.ops.object.transform_apply(rotation=True)


def my_function():

    bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN', center='MEDIAN')
    #minimize outbox
    align_axis('X', 1, minimization_steps)
    align_axis('Y', 2, minimization_steps)
    align_axis('Z', 0, minimization_steps)
    align_axis('Y', 2, minimization_steps)


    #Orient correctly
    if(min(obj.dimensions) != obj.dimensions[2]):
        if(obj.dimensions[1] > obj.dimensions[0]):
            bpy.ops.transform.rotate(value=(math.pi/2), orient_axis='Y')
        else:
            bpy.ops.transform.rotate(value=(math.pi/2), orient_axis='X')
    if(obj.dimensions[0] < obj.dimensions[1]):
        bpy.ops.transform.rotate(value=(math.pi/2), orient_axis='Z')

    #move to origin
    bpy.ops.object.align(bb_quality=True, align_mode='OPT_1', relative_to='OPT_1', align_axis={'X'})
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    bpy.ops.object.align(bb_quality=True, align_mode='OPT_1', relative_to='OPT_1', align_axis={'Y'})
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    bpy.ops.object.align(bb_quality=True, align_mode='OPT_1', relative_to='OPT_1', align_axis={'Z'})
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)


my_function()