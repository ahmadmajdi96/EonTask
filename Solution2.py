from stl import mesh 
import requests
from mpl_toolkits import mplot3d
from matplotlib import pyplot
import math



class ModelRotation:
    def __init__(self, fileName):
        self.fileName = fileName
        self.rotatedName = "raw_039_rotated.stl"
        self.openfile()
        
    def openfile(self):
        # Opening stl file 'raw_039.stl' using mesh
        self.retrievedModel = mesh.Mesh.from_file(self.fileName)
        
        # Rotating model 180 degrees around the y-axis
        self.retrievedModel.rotate([0, 1, 0], math.radians(180))
        
        # Saving model as 'raw_039_rotated.stl'
        self.retrievedModel.save("raw_039_rotated.stl")
        
        # Opening rotated model
        self.rotatedModel = mesh.Mesh.from_file(self.rotatedName)
        
        self.plotmodel()
        
        
    def plotmodel(self):
        #Creating plot
        figure = pyplot.figure()
        axes = mplot3d.Axes3D(figure)
        
        # Adding 3d model to the plot
        axes.add_collection3d(mplot3d.art3d.Poly3DCollection(self.rotatedModel.vectors))
        
        # Scaling 3d model to plot
        scale = self.rotatedModel.points.flatten()
        axes.auto_scale_xyz(scale-10, scale+10, scale)
        
        # Showing the plot
        pyplot.show()

        
ModelRotation('raw_039.stl')
