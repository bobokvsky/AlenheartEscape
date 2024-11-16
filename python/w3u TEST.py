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
    print(number_of_destruct)

    for i in range(1):
        treeID = doo.read(4).decode('utf-8')
        print(treeID)

        variation = doo.read(4)
        variation = int.from_bytes(variation, byteorder='little')
        print(variation)

        x = doo.read(4)
        y = doo.read(4)
        z = doo.read(4)
        x = struct.unpack('f', x)[0]
        y = struct.unpack('f', y)[0]
        z = struct.unpack('f', z)[0]

        angle = doo.read(4)
        angle = struct.unpack('f', angle)[0]  # in radians

        x_scale = doo.read(4)
        y_scale = doo.read(4)
        z_scale = doo.read(4)
        x_scale = struct.unpack('f', x_scale)[0]
        y_scale = struct.unpack('f', y_scale)[0]
        z_scale = struct.unpack('f', z_scale)[0]
        
        print((x, y, z), angle, (x_scale, y_scale, z_scale))

        flags = doo.read(1)

        player = doo.read(4)
        player = int.from_bytes(player, byteorder='little')

        unknown1 = doo.read(1)
        unknown2 = doo.read(1)

        health = doo.read(4)
        health = int.from_bytes(health, byteorder='little')
        mana = doo.read(4)
        mana = int.from_bytes(mana, byteorder='little')

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

        gold = doo.read(4)
        gold = int.from_bytes(gold, byteorder='little')
        
        target_acquisition = doo.read(4)
        target_acquisition = struct.unpack('f', target_acquisition)[0]
        
        level = doo.read(4)
        level = int.from_bytes(level, byteorder='little')
        
        strength = doo.read(4)
        strength = int.from_bytes(strength, byteorder='little')

        agility = doo.read(4)
        agility = int.from_bytes(agility, byteorder='little')

        intelligence = doo.read(4)
        intelligence = int.from_bytes(intelligence, byteorder='little')

        i_items_size = doo.read(4)
        i_items_size = int.from_bytes(i_items_size, byteorder='little')
        for j in range(i_items_size):
            j_slot = doo.read(4)
            j_id = doo.read(4).decode('utf-8')
        

'''
for (auto&& i : units) {
		i.id = reader.read_string(4);
		i.variation = reader.read<uint32_t>();
		i.position = (reader.read<glm::vec3>() - glm::vec3(terrain.offset, 0)) / 128.f;
		i.angle = reader.read<float>();
		i.scale = reader.read<glm::vec3>() / 128.f;
		
		i.flags = reader.read<uint8_t>();

		i.player = reader.read<uint32_t>();

		i.unknown1 = reader.read<uint8_t>();
		i.unknown2 = reader.read<uint8_t>();

		i.health = reader.read<uint32_t>();
		i.mana = reader.read<uint32_t>();

		if (version >= 8) {
			i.item_table_pointer = reader.read<uint32_t>();
		}

		i.item_sets.resize(reader.read<uint32_t>());
		for (auto&& j : i.item_sets) {
			j.items.resize(reader.read<uint32_t>());
			for (auto&&[id, chance] : j.items) {
				id = reader.read_string(4);
				chance = reader.read<uint32_t>();
			}
		}

		i.gold = reader.read<uint32_t>();
		i.target_acquisition = reader.read<float>();

		i.level = reader.read<uint32_t>();

		if (version >= 8) {
			i.strength = reader.read<uint32_t>();
			i.agility = reader.read<uint32_t>();
			i.intelligence = reader.read<uint32_t>();
		}

		i.items.resize(reader.read<uint32_t>());
		for (auto&& [slot, id] : i.items) {
			slot = reader.read<uint32_t>();
			id = reader.read_string(4);
		}

		i.abilities.resize(reader.read<uint32_t>());
		for (auto&&[id, autocast, level] : i.abilities) {
			id = reader.read_string(4);
			autocast = reader.read<uint32_t>();
			level =  reader.read<uint32_t>();
		}

		i.random_type = reader.read<uint32_t>();
		switch (i.random_type) {
			case 0:
				i.random = reader.read_vector<uint8_t>(4);
				break;
			case 1:
				i.random = reader.read_vector<uint8_t>(8);
				break;
			case 2:
				i.random = reader.read_vector<uint8_t>(reader.read<uint32_t>() * 8);
				break;
		}

		i.custom_color = reader.read<uint32_t>();
		i.waygate = reader.read<uint32_t>();
		i.creation_number = reader.read<uint32_t>();
	}
'''


'''
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
        if (i == width - 1):
            continue
        bottom_left = tiles[i][j]
        #bottom_right = tiles[i+1][j]
        #top_left = tiles[i][j+1]
        #top_right = tiles[i+1][j+1]

        #x = 128 * i - (width-1) * 128 / 2
        #y = 128 * j - (height-1) * 128 / 2
        terraintype = ground_tilesets_IDs[bottom_left.ground_type]
        variation = bottom_left.ground_variation
        file.write("{} {}\n".format(terraintype, variation))'''