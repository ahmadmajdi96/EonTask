from stl import mesh 
import requests
from mpl_toolkits import mplot3d
from matplotlib import pyplot
import math

"""

--- In case of downloading file from url ands saving it locally --

#Storing url in a variable 
url = "https://nervous-mouse.s3.eu-central-1.amazonaws.com/raw_039.stl"

# Sending GET request and saving the response
requestedFile = requests.get(url, allow_redirects=True)

# Creating stl file from the content of the response
open('raw_039.stl', 'wb').write(requestedFile.content)

"""
try: 
    # Opening stl file 'raw_039.stl' using mesh
    retrievedModel = mesh.Mesh.from_file('raw_039.stl')

    # Rotating model 180 degrees around the y-axis
    retrievedModel.rotate([0, 1, 0], math.radians(180))

    # Saving model as 'raw_039_rotated.stl'
    retrievedModel.save("raw_039_rotated.stl")
    
    RotatedModel = mesh.Mesh.from_file('raw_039_rotated.stl')


    # Creating plot
    figure = pyplot.figure()
    axes = mplot3d.Axes3D(figure)
    
    # Adding 3d model to the plot
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(RotatedModel.vectors))
    
    # Scaling 3d model to plot
    scale = RotatedModel.points.flatten()
    axes.auto_scale_xyz(scale-10, scale+10, scale)
    
    # Opening the plot
    pyplot.show()
    
except Exception as e: 
    print(e)
