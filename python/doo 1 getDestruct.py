import struct
import numpy as np

class Tileset:
    pass

with open('python\\war3map.doo', 'rb') as doo:
    doo.seek(0)  # Go to beginning
    fileID = doo.read(4)
    fileID = fileID.decode('utf-8')

    format_version = doo.read(4)
    format_version = int.from_bytes(format_version, byteorder='little')

    subversion = doo.read(4)
    subversion = int.from_bytes(subversion, byteorder='little')

    number_of_destruct = doo.read(4)
    number_of_destruct = int.from_bytes(number_of_destruct, byteorder='little')
    #print(number_of_destruct)

    table_values = []

    for i in range(number_of_destruct):
        treeID = doo.read(4).decode('utf-8')

        variation = doo.read(4)
        variation = int.from_bytes(variation, byteorder='little')

        x = doo.read(4)
        y = doo.read(4)
        z = doo.read(4)
        x = int(struct.unpack('f', x)[0])
        y = int(struct.unpack('f', y)[0])
        z = int(struct.unpack('f', z)[0])

        angle = doo.read(4)
        angle = struct.unpack('f', angle)[0]  # in radians
        angle = round(angle, 2)

        x_scale = doo.read(4)
        y_scale = doo.read(4)
        z_scale = doo.read(4)
        x_scale = struct.unpack('f', x_scale)[0]
        y_scale = struct.unpack('f', y_scale)[0]
        z_scale = struct.unpack('f', z_scale)[0]
        scale = min(x_scale, y_scale, z_scale)
        scale = round(scale, 2)
        
        #print(treeID, variation, (x, y, z), angle, (x_scale, y_scale, z_scale))

        tree_flags = doo.read(1)
        life = doo.read(1)

        item_table_pointer = doo.read(4)
        item_table_pointer = int.from_bytes(item_table_pointer, byteorder='little')

        item_sets_size = doo.read(4)
        item_sets_size = int.from_bytes(item_sets_size, byteorder='little')
        for j in range(item_sets_size):
            j_items_size = doo.read(4)
            j_items_size = int.from_bytes(j_items_size, byteorder='little')
            for k in range(j_items_size):
                k_item_id = doo.read(4).decode('utf-8')

                k_chance = doo.read(4)
                k_chance = int.from_bytes(k_chance, byteorder='little')
        
        world_editor_id = doo.read(4)
        world_editor_id = int.from_bytes(world_editor_id, byteorder='little')

        table_values.append([treeID, variation, [x, y, z], angle, scale])

with open('python\\temp\\destructs.txt', 'w') as file:
    for i in range(number_of_destruct):
        treeID = table_values[i][0]
        variation = table_values[i][1]
        x, y, z = table_values[i][2]
        angle = table_values[i][3]
        scale = table_values[i][4]
        file.write("{} {} {} {} {} {} {}\n".format(treeID, variation, x, y, z, angle, scale))