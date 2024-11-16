import struct
import numpy as np

class Tileset:
    pass

with open('python\\war3map.w3e', 'rb') as w3e:
    w3e.seek(0)  # Go to beginning

    # int = 4 bytes
    fileID = w3e.read(4)
    fileID = fileID.decode('utf-8')

    format_version = w3e.read(4)
    format_version = int.from_bytes(format_version, byteorder='little')
    
    main_tileset = w3e.read(1)
    main_tileset = main_tileset.decode('utf-8')

    custom_tilesets_flag = w3e.read(4)
    custom_tilesets_flag = int.from_bytes(custom_tilesets_flag, byteorder='little')

    number_of_ground_tilesets = w3e.read(4)
    number_of_ground_tilesets = int.from_bytes(number_of_ground_tilesets, byteorder='little')

    ground_tilesets_IDs = []
    for i in range(number_of_ground_tilesets):
        ground_tilesets_IDs.append(w3e.read(4).decode('utf-8'))
    
    number_of_cliff_tilesets = w3e.read(4)
    number_of_cliff_tilesets = int.from_bytes(number_of_cliff_tilesets, byteorder='little')

    cliff_tilesets_IDs = []
    for i in range(number_of_cliff_tilesets):
        cliff_tilesets_IDs.append(w3e.read(4).decode('utf-8'))

    width = w3e.read(4)
    width = int.from_bytes(width, byteorder='little')

    height = w3e.read(4)
    height = int.from_bytes(height, byteorder='little')

    center_offeset_X = w3e.read(4)
    center_offeset_X = struct.unpack('f', center_offeset_X)[0]

    center_offeset_Y = w3e.read(4)
    center_offeset_Y = struct.unpack('f', center_offeset_Y)[0]
    
    # tile = 7 bytes
    tiles = [[x for x in range(width)] for y in range(height)]
    for j in range(height):
        for i in range(width):
            tileset = Tileset()
            height_tile = w3e.read(2)
            height_tile = int.from_bytes(height_tile, byteorder='little')
            height_tile = (height_tile - 8192.) / 512.
            tileset.height_tile = height_tile

            water_level_and_map_edge = w3e.read(2)
            water_level_and_map_edge = int.from_bytes(water_level_and_map_edge, 
                                                            byteorder='little')
            tileset.water_level = water_level_and_map_edge & 0x3FFF
            tileset.water_level = (tileset.water_level - 8192.) / 512.
            tileset.map_edge = water_level_and_map_edge & 0x4000

            flags_AND_ground_type = w3e.read(1)
            flags_AND_ground_type = int.from_bytes(flags_AND_ground_type, 
                                                            byteorder='little')
            tileset.ramp = flags_AND_ground_type & 0b00010000
            tileset.blight = flags_AND_ground_type & 0b00100000
            tileset.water = flags_AND_ground_type & 0b01000000
            tileset.boundary = flags_AND_ground_type & 0b10000000
            tileset.ground_type = flags_AND_ground_type & 0b00001111 

            variation = w3e.read(1)
            variation = int.from_bytes(variation, byteorder='little')
            tileset.ground_variation = variation & 0b00011111
            tileset.cliff_variation = (variation & 0b11100000) >> 5 

            cliff_type_AND_layer_height = w3e.read(1)
            cliff_type_AND_layer_height = int.from_bytes(cliff_type_AND_layer_height, 
                                                            byteorder='little')
            tileset.cliff_type = (cliff_type_AND_layer_height & 0b11110000) >> 4
            tileset.layer_height = cliff_type_AND_layer_height & 0b00001111

            tiles[i][j] = tileset

with open('python\\temp\\tiles.txt', 'w') as file:
    for j in range(height):
        for i in range(width):
            bottom_left = tiles[i][j]
            #bottom_right = tiles[i+1][j]
            #top_left = tiles[i][j+1]
            #top_right = tiles[i+1][j+1]

            #x = 128 * i - (width-1) * 128 / 2
            #y = 128 * j - (height-1) * 128 / 2
            terraintype = ground_tilesets_IDs[bottom_left.ground_type]
            variation = bottom_left.ground_variation
            file.write("{} {}\n".format(terraintype, variation))