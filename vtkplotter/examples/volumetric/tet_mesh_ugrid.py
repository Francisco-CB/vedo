"""Read a tetrahedral mesh from a
vtkUnstructuredGrid object and visualize it
as either a Volume (left) or a Mesh (right)
"""
from vtkplotter import *

ug = loadUnStructuredGrid(datadir+'limb_ugrid.vtk')

cmap = 'nipy_spectral'

vol = Volume(ug).color(cmap)

################################
# if False will only show the outer surface:
settings.visibleGridEdges = True

mesh = Mesh(ug).color(cmap).alpha(0.2).addScalarBar(c='w')

show([(vol,__doc__), mesh], N=2, bg='bb')
