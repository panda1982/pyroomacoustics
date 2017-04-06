'''
A simple example of using pyroomacoustics to generate
room impulse responses of shoebox shaped rooms in 2d.
'''
from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt

import pyroomacoustics as pra

# Room 4m by 6m
room_dim = [4, 6]

# source location
source = np.array([1, 4.5])

# create the room with sources and mics
room = pra.ShoeBox(
    room_dim,
    fs=16000,
    max_order=2)

# add mic and good source to room
room.addSource(source)

# place 1 microphone in the room
mics = pra.MicrophoneArray(np.array([[4,],
                                     [2,]]), room.fs)
room.addMicrophoneArray(mics)

# Run the image source model
room.image_source_model()

# Plot the result up to fourth order images
room.plot(img_order=4)
plt.show()
