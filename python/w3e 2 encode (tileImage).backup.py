import numpy as np
from functools import cmp_to_key

DIAG_UP_LEFT = 2
DIAG_UP_RIGHT = 3
DIAG_DOWN_LEFT = 5
DIAG_DOWN_RIGHT = 9
UP = 4
LEFT = 6
RIGHT = 11
DOWN = 13
DIAG_UP = 7
DIAG_DOWN = 10
BOUND_UP_LEFT = 8
BOUND_DOWN_LEFT = 14
BOUND_UP_RIGHT = 12
BOUND_DOWN_RIGHT = 15
CENTER_VAR0 = 17
CENTER_VAR1 = 18
CENTER_VAR2 = 19
CENTER_VAR3 = 20
CENTER_VAR4 = 21
CENTER_VAR5 = 22
CENTER_VAR6 = 23
CENTER_VAR7 = 24
CENTER_VAR8 = 25
CENTER_VAR9 = 26
CENTER_VAR10 = 27
CENTER_VAR11 = 28
CENTER_VAR12 = 29
CENTER_VAR13 = 30
CENTER_VAR14 = 31
CENTER_VAR15 = 32
CENTER_VAR16 = 16
CENTER_VAR17 = 1
WIDTH = 97
HEIGHT = 97



# terrain ids
ICE_TURNING_TILE_ID = 'Nice'
ICE_NONTURNING_TILE_ID = 'Idki'
ICE_REVERSETURNING_TILE_ID = 'Glav'
ICE_ACCELERATING_TURNING_TILE_ID = 'Iice'
SNOW_TILE_ID = 'Nsnw'
SNOWY_ROCKS_TILE_ID = 'Nsnr'
NORTH_ROCKS_ID = 'Nrck'
OUTLAND_ABYSS_ID = 'cOc1'
DALARAN_BLACK_MARBLE_ID = 'Xblm'
DALARAN_GRASS_TRIM_ID = 'Xhdg'
DALARAN_WHITE_MARBLE_ID = 'Xwmb'
TILE_SIZE = 135
GLAVA = "GLava"
EMPTY = "Empty"
minZ = 512.

######################
######################

def isTerrain32BLP(terrainType):
    if terrainType == OUTLAND_ABYSS_ID:
        return False
    if terrainType == SNOW_TILE_ID:
        return True
    if terrainType == SNOWY_ROCKS_TILE_ID:
        return False
    if terrainType == ICE_TURNING_TILE_ID:
        return True
    if terrainType == ICE_NONTURNING_TILE_ID:
        return False
    if terrainType == ICE_REVERSETURNING_TILE_ID:
        return False
    if terrainType == ICE_ACCELERATING_TURNING_TILE_ID:
        return True
    if terrainType == DALARAN_BLACK_MARBLE_ID:
        return False
    if terrainType == DALARAN_GRASS_TRIM_ID:
        return False
    if terrainType == DALARAN_WHITE_MARBLE_ID:
        return False
    if terrainType == NORTH_ROCKS_ID:
        return True
    return False

def getTileVariation(terrainType, variation):
    variation = int(variation)
    if not isTerrain32BLP(terrainType):
        if variation == 0:
            return CENTER_VAR17
        else:
            return CENTER_VAR16
    if variation == 0:
        return CENTER_VAR0
    if variation == 1:
        return CENTER_VAR1
    if variation == 2:
        return CENTER_VAR2
    if variation == 3:
        return CENTER_VAR3
    if variation == 4:
        return CENTER_VAR4
    if variation == 5:
        return CENTER_VAR5
    if variation == 6:
        return CENTER_VAR6
    if variation == 7:
        return CENTER_VAR7
    if variation == 8:
        return CENTER_VAR8
    if variation == 9:
        return CENTER_VAR9
    if variation == 10:
        return CENTER_VAR10
    if variation == 11:
        return CENTER_VAR11
    if variation == 12:
        return CENTER_VAR12
    if variation == 13:
        return CENTER_VAR13
    if variation == 14:
        return CENTER_VAR14
    if variation == 15:
        return CENTER_VAR15
    if variation == 16:
        return CENTER_VAR16
    if variation == 17:
        return CENTER_VAR17
    return 0


# level1 < level 2 <-> picture of level2 overlaps picture of level1
def getTerrainTypeLevel(terrainType):
    if terrainType == OUTLAND_ABYSS_ID:
        return 0
    if terrainType == SNOW_TILE_ID:
        return 1
    if terrainType == ICE_TURNING_TILE_ID:
        return 2
    if terrainType == ICE_NONTURNING_TILE_ID:
        return 3
    if terrainType == ICE_REVERSETURNING_TILE_ID:
        return 4
    if terrainType == DALARAN_BLACK_MARBLE_ID:
        return 5
    if terrainType == SNOWY_ROCKS_TILE_ID:
        return 6
    if terrainType == DALARAN_WHITE_MARBLE_ID:
        return 7
    if terrainType == DALARAN_GRASS_TRIM_ID:
        return 8
    if terrainType == ICE_ACCELERATING_TURNING_TILE_ID:
        return 9
    if terrainType == NORTH_ROCKS_ID:
        return 10
    if terrainType == -1:
        return 100
    return 0

######################

class Square:
    up_left_var = 0
    up_right_var = 0
    down_left_var = 0
    down_right_var = 0
    variation = 0
    terrainType = OUTLAND_ABYSS_ID
    level = 0  #level1 < level 2 <-> picture of level2 overlaps picture of level1

    isEmpty = False
    width = 0
    height = 0

    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.x = 128 * self.width - WIDTH * 128 / 2
        self.y = 128 * self.height - HEIGHT * 128 / 2

    def setUpLeftVar(self, a):
        self.up_left_var = a

    def setUpRightVar(self, a):
        self.up_right_var = a
        
    def setDownLeftVar(self, a):
        self.down_left_var = a

    def setDownRightVar(self, a):
        self.down_right_var = a

    def setTerrainType(self, ttype):
        self.terrainType = ttype

    def getTerrainType(self):
        return self.terrainType

    def setTerrainVariation(self, a):
        self.variation = a

    def getTerrainVariation(self):
        return self.variation

tileImage = []
for w in np.arange(WIDTH):
    tileImage_w = []
    for h in np.arange(HEIGHT):
        tileImage_w.append(Square(w, h))
    tileImage.append(tileImage_w)


def setTerrainTypeBLP(x, y, terrainType, variation):
    i = int((x + WIDTH * 128 / 2) / 128)
    j = int((y + HEIGHT * 128 / 2) / 128)
    square = tileImage[i][j]
    square_up = tileImage[i][j+1]
    square_left = tileImage[i-1][j]
    square_down = tileImage[i][j-1]
    square_right = tileImage[i+1][j]
    square_upLeft = tileImage[i-1][j+1]
    square_upRight = tileImage[i+1][j+1]
    square_downLeft = tileImage[i-1][j-1]
    square_downRight = tileImage[i+1][j-1]

    # squares = [square, square_up, square_left, square_down, square_right, 
    #             square_upLeft, square_upRight, square_downLeft, square_downRight]

    square.setTerrainType(terrainType)
    square.setTerrainVariation(variation)

    # *********************
    # *********************
    # TILE
    # *********************
    # UP + UPRIGHT + RIGHT
    if      terrainType == square_up.getTerrainType() and \
            terrainType != square_upRight.getTerrainType() and \
            terrainType != square_right.getTerrainType():
        # if getTerrainTypeLevel(terrainType) < getTerrainTypeLevel(square_right.getTerrainType()):
        #     square.setUpRightVar(getTileVariation(terrainType, square.getTerrainVariation()))
        #     square_up.setDownRightVar(getTileVariation(terrainType, square.getTerrainVariation()))
        # else:
        square.setUpRightVar(RIGHT)
        square_up.setDownRightVar(RIGHT)
    elif terrainType != square_up.getTerrainType() and \
            terrainType == square_upRight.getTerrainType() and \
            terrainType != square_right.getTerrainType():
        
        square.setUpRightVar(DIAG_UP)
        square_upRight.setDownLeftVar(DIAG_UP)
    elif terrainType != square_up.getTerrainType() and \
            terrainType != square_upRight.getTerrainType() and \
            terrainType == square_right.getTerrainType():
        # if getTerrainTypeLevel(terrainType) < getTerrainTypeLevel(square_up.getTerrainType()):
            # square.setUpRightVar(getTileVariation(terrainType, square.getTerrainVariation()))
            # square_right.setUpLeftVar(getTileVariation(terrainType, square.getTerrainVariation()))
        # else:
        square.setUpRightVar(UP)
        square_right.setUpLeftVar(UP)
    elif terrainType == square_up.getTerrainType() and \
            terrainType == square_upRight.getTerrainType() and \
            terrainType != square_right.getTerrainType():
        
        square.setUpRightVar(BOUND_DOWN_RIGHT)
        square_up.setDownRightVar(BOUND_DOWN_RIGHT)
        square_upRight.setDownLeftVar(BOUND_DOWN_RIGHT)
    elif terrainType != square_up.getTerrainType() and \
            terrainType == square_upRight.getTerrainType() and \
            terrainType == square_right.getTerrainType():
        
        square.setUpRightVar(BOUND_UP_LEFT)
        square_upRight.setDownLeftVar(BOUND_UP_LEFT)
        square_right.setUpLeftVar(BOUND_UP_LEFT)
    elif terrainType == square_up.getTerrainType() and \
            terrainType != square_upRight.getTerrainType() and \
            terrainType == square_right.getTerrainType():

        square.setUpRightVar(BOUND_UP_RIGHT)
        square_up.setDownRightVar(BOUND_UP_RIGHT)
        square_right.setUpLeftVar(BOUND_UP_RIGHT)

    elif terrainType == square_up.getTerrainType() and \
            terrainType == square_upRight.getTerrainType() and \
            terrainType == square_right.getTerrainType():

        square.setUpRightVar(getTileVariation(terrainType, square.getTerrainVariation()))
        square_up.setDownRightVar(getTileVariation(terrainType, square.getTerrainVariation()))
        square_upRight.setDownLeftVar(getTileVariation(terrainType, square.getTerrainVariation()))
        square_right.setUpLeftVar(getTileVariation(terrainType, square.getTerrainVariation()))

    elif terrainType != square_up.getTerrainType() and \
            terrainType != square_upRight.getTerrainType() and \
            terrainType != square_right.getTerrainType():
        square.setUpRightVar(DIAG_UP_RIGHT)

    

    # *********************
    # *********************
    # ********************* 
    # UP + UPLEFT + LEFT
    if      terrainType == square_up.getTerrainType() and \
            terrainType != square_upLeft.getTerrainType() and \
            terrainType != square_left.getTerrainType():
        # if getTerrainTypeLevel(terrainType) < getTerrainTypeLevel(square_upLeft.getTerrainType()):
            # square.setUpLeftVar(getTileVariation(terrainType, square_left.getTerrainVariation()))
            # square_up.setDownLeftVar(getTileVariation(terrainType, square_left.getTerrainVariation()))
        # else:
        square.setUpLeftVar(LEFT)
        square_up.setDownLeftVar(LEFT)
            # square_upLeft.setDownRightVar(getTileVariation(terrainType, square_left.getTerrainVariation()))
            # square_left.setUpRightVar(getTileVariation(terrainType, square_left.getTerrainVariation()))
    elif terrainType != square_up.getTerrainType() and \
            terrainType == square_upLeft.getTerrainType() and \
            terrainType != square_left.getTerrainType():
        
        square.setUpLeftVar(DIAG_DOWN)
        square_upLeft.setDownRightVar(DIAG_DOWN)
    elif terrainType != square_up.getTerrainType() and \
            terrainType != square_upLeft.getTerrainType() and \
            terrainType == square_left.getTerrainType():
        # if getTerrainTypeLevel(terrainType) < getTerrainTypeLevel(square_up.getTerrainType()):
            # square.setUpLeftVar(getTileVariation(terrainType, square_left.getTerrainVariation()))
            # square_left.setUpRightVar(getTileVariation(terrainType, square_left.getTerrainVariation()))
        # else:
        square.setUpLeftVar(UP)
        square_left.setUpRightVar(UP)
    elif terrainType == square_up.getTerrainType() and \
            terrainType == square_upLeft.getTerrainType() and \
            terrainType != square_left.getTerrainType():
        
        square.setUpLeftVar(BOUND_DOWN_LEFT)
        square_up.setDownLeftVar(BOUND_DOWN_LEFT)
        square_upLeft.setDownRightVar(BOUND_DOWN_LEFT)
    elif terrainType != square_up.getTerrainType() and \
            terrainType == square_upLeft.getTerrainType() and \
            terrainType == square_left.getTerrainType():
        
        square.setUpLeftVar(BOUND_UP_RIGHT)
        square_upLeft.setDownRightVar(BOUND_UP_RIGHT)
        square_left.setUpRightVar(BOUND_UP_RIGHT)
    elif terrainType == square_up.getTerrainType() and \
            terrainType != square_upLeft.getTerrainType() and \
            terrainType == square_left.getTerrainType():

        square.setUpLeftVar(BOUND_UP_LEFT)
        square_up.setDownLeftVar(BOUND_UP_LEFT)
        square_left.setUpRightVar(BOUND_UP_LEFT)

    elif terrainType == square_up.getTerrainType() and \
            terrainType == square_upLeft.getTerrainType() and \
            terrainType == square_left.getTerrainType():

        square.setUpLeftVar(getTileVariation(terrainType, square_left.getTerrainVariation()))
        square_up.setDownLeftVar(getTileVariation(terrainType, square_left.getTerrainVariation()))
        square_upLeft.setDownRightVar(getTileVariation(terrainType, square_left.getTerrainVariation()))
        square_left.setUpRightVar(getTileVariation(terrainType, square_left.getTerrainVariation()))

    elif terrainType != square_up.getTerrainType() and \
            terrainType != square_upLeft.getTerrainType() and \
            terrainType != square_left.getTerrainType():
        square.setUpLeftVar(DIAG_UP_LEFT)

    # *********************
    # *********************
    # ********************* 
    # DOWN + DOWNLEFT + LEFT
    if      terrainType == square_down.getTerrainType() and \
            terrainType != square_downLeft.getTerrainType() and \
            terrainType != square_left.getTerrainType():
        
        # if getTerrainTypeLevel(terrainType) < getTerrainTypeLevel(square_downLeft.getTerrainType()):
            # square.setDownLeftVar(getTileVariation(terrainType, square_downLeft.getTerrainVariation()))
            # square_down.setUpLeftVar(getTileVariation(terrainType, square_downLeft.getTerrainVariation()))
        # else:
        square.setDownLeftVar(LEFT)
        square_down.setUpLeftVar(LEFT)
            # square_downLeft.setUpRightVar(getTileVariation(terrainType, square_downLeft.getTerrainVariation()))
            # square_left.setDownRightVar(getTileVariation(terrainType, square_downLeft.getTerrainVariation()))
    elif terrainType != square_down.getTerrainType() and \
            terrainType == square_downLeft.getTerrainType() and \
            terrainType != square_left.getTerrainType():
        
        square.setDownLeftVar(DIAG_UP)
        square_downLeft.setUpRightVar(DIAG_UP)
    elif terrainType != square_down.getTerrainType() and \
            terrainType != square_downLeft.getTerrainType() and \
            terrainType == square_left.getTerrainType():
        # if getTerrainTypeLevel(terrainType) < getTerrainTypeLevel(square_down.getTerrainType()):
            # square.setDownLeftVar(getTileVariation(terrainType, square_downLeft.getTerrainVariation()))
            # square_left.setDownRightVar(getTileVariation(terrainType, square_downLeft.getTerrainVariation()))
        # else:
        square.setDownLeftVar(DOWN)
        square_left.setDownRightVar(DOWN)
    elif terrainType == square_down.getTerrainType() and \
            terrainType == square_downLeft.getTerrainType() and \
            terrainType != square_left.getTerrainType():
        
        square.setDownLeftVar(BOUND_UP_LEFT)
        square_down.setUpLeftVar(BOUND_UP_LEFT)
        square_downLeft.setUpRightVar(BOUND_UP_LEFT)
    elif terrainType != square_down.getTerrainType() and \
            terrainType == square_downLeft.getTerrainType() and \
            terrainType == square_left.getTerrainType():
        
        square.setDownLeftVar(BOUND_DOWN_RIGHT)
        square_downLeft.setUpRightVar(BOUND_DOWN_RIGHT)
        square_left.setDownRightVar(BOUND_DOWN_RIGHT)
    elif terrainType == square_down.getTerrainType() and \
            terrainType != square_downLeft.getTerrainType() and \
            terrainType == square_left.getTerrainType():

        square.setDownLeftVar(BOUND_DOWN_LEFT)
        square_down.setUpLeftVar(BOUND_DOWN_LEFT)
        square_left.setDownRightVar(BOUND_DOWN_LEFT)

    elif terrainType == square_down.getTerrainType() and \
            terrainType == square_downLeft.getTerrainType() and \
            terrainType == square_left.getTerrainType():

        square.setDownLeftVar(getTileVariation(terrainType, square_downLeft.getTerrainVariation()))
        square_down.setUpLeftVar(getTileVariation(terrainType, square_downLeft.getTerrainVariation()))
        square_downLeft.setUpRightVar(getTileVariation(terrainType, square_downLeft.getTerrainVariation()))
        square_left.setDownRightVar(getTileVariation(terrainType, square_downLeft.getTerrainVariation()))

    elif terrainType != square_down.getTerrainType() and \
            terrainType != square_downLeft.getTerrainType() and \
            terrainType != square_left.getTerrainType():
        square.setDownLeftVar(DIAG_DOWN_LEFT)

    # *********************
    # *********************
    # ********************* 
    # DOWN + DOWNRIGHT + RIGHT
    if      terrainType == square_down.getTerrainType() and \
            terrainType != square_downRight.getTerrainType() and \
            terrainType != square_right.getTerrainType():
        # if getTerrainTypeLevel(terrainType) < getTerrainTypeLevel(square_right.getTerrainType()):
            # square.setDownRightVar(getTileVariation(terrainType, square_down.getTerrainVariation()))
            # square_down.setUpRightVar(getTileVariation(terrainType, square_down.getTerrainVariation()))
        # else:
        square.setDownRightVar(RIGHT)
        square_down.setUpRightVar(RIGHT)
    elif terrainType != square_down.getTerrainType() and \
            terrainType == square_downRight.getTerrainType() and \
            terrainType != square_right.getTerrainType():
        square.setDownRightVar(DIAG_DOWN)
        square_downRight.setUpLeftVar(DIAG_DOWN)
    elif terrainType != square_down.getTerrainType() and \
            terrainType != square_downRight.getTerrainType() and \
            terrainType == square_right.getTerrainType():
        # if getTerrainTypeLevel(terrainType) < getTerrainTypeLevel(square_down.getTerrainType()):
            # square.setDownRightVar(getTileVariation(terrainType, square_down.getTerrainVariation()))
            # square_right.setDownLeftVar(getTileVariation(terrainType, square_down.getTerrainVariation()))
        # else:
        square.setDownRightVar(DOWN)
        square_right.setDownLeftVar(DOWN)
    elif terrainType == square_down.getTerrainType() and \
            terrainType == square_downRight.getTerrainType() and \
            terrainType != square_right.getTerrainType():
        square.setDownRightVar(BOUND_UP_RIGHT)
        square_down.setUpRightVar(BOUND_UP_RIGHT)
        square_downRight.setUpLeftVar(BOUND_UP_RIGHT)
    elif terrainType != square_down.getTerrainType() and \
            terrainType == square_downRight.getTerrainType() and \
            terrainType == square_right.getTerrainType():
        square.setDownRightVar(BOUND_DOWN_LEFT)
        square_downRight.setUpLeftVar(BOUND_DOWN_LEFT)
        square_right.setDownLeftVar(BOUND_DOWN_LEFT)
    elif terrainType == square_down.getTerrainType() and \
            terrainType != square_downRight.getTerrainType() and \
            terrainType == square_right.getTerrainType():
        square.setDownRightVar(BOUND_DOWN_RIGHT)
        square_down.setUpRightVar(BOUND_DOWN_RIGHT)
        square_right.setDownLeftVar(BOUND_DOWN_RIGHT)

    elif terrainType == square_down.getTerrainType() and \
            terrainType == square_downRight.getTerrainType() and \
            terrainType == square_right.getTerrainType():
        square.setDownRightVar(getTileVariation(terrainType, square_down.getTerrainVariation()))
        square_down.setUpRightVar(getTileVariation(terrainType, square_down.getTerrainVariation()))
        square_downRight.setUpLeftVar(getTileVariation(terrainType, square_down.getTerrainVariation()))
        square_right.setDownLeftVar(getTileVariation(terrainType, square_down.getTerrainVariation()))

    elif terrainType != square_down.getTerrainType() and \
            terrainType != square_downRight.getTerrainType() and \
            terrainType != square_right.getTerrainType():
        square.setDownRightVar(DIAG_DOWN_RIGHT)

##################


filename = 'python\\temp\\tiles.txt'

with open('python\\temp\\tiles.txt', 'r') as f:
    i = 0
    j = 0
    for line in f:
        tileset, variation = line.split()
        x = 128 * i - (WIDTH-1) * 128 / 2
        y = 128 * j - (HEIGHT-1) * 128 / 2
        i += 1
        if i == WIDTH:
            i = 0
            j += 1

        if not (i - 1 < 0 or i + 1 == WIDTH or j - 1 < 0 or j + 1 == HEIGHT):
            setTerrainTypeBLP(x, y, tileset, variation)

def squareComparator(sq1, sq2):
    if getTerrainTypeLevel(sq1.terrainType) < getTerrainTypeLevel(sq2.terrainType):
            return -1
    elif getTerrainTypeLevel(sq1.terrainType) > getTerrainTypeLevel(sq2.terrainType):
            return 1
    else:
            return 0


tileImage = np.array(tileImage).ravel().tolist()
tileImage = sorted(tileImage, key=cmp_to_key(squareComparator))

with open('python\\temp\\tilesBLP.txt', 'w') as file:
    with open('python\\temp\\encoded_tilesBLP.txt', 'w') as file2:
        for square in tileImage:
            i = str(square.width)
            j = str(square.height)
            terraintype = str(square.getTerrainType())
            variation = str(square.getTerrainVariation())
            up_left_var = str(square.up_left_var)
            up_right_var = str(square.up_right_var)
            down_left_var = str(square.down_left_var)
            down_right_var = str(square.down_right_var)
            if len(i) == 1:
                i = "0" + i
            if len(j) == 1:
                j = "0" + j
            if len(variation) == 1:
                variation = "0" + variation
            if len(up_left_var) == 1:
                up_left_var = "0" + up_left_var
            if len(up_right_var) == 1:
                up_right_var = "0" + up_right_var
            if len(down_left_var) == 1:
                down_left_var = "0" + down_left_var
            if len(down_right_var) == 1:
                down_right_var = "0" + down_right_var
            file.write("{} {} {} {} {} {} {} {}\n".format(i, j, terraintype, variation, 
                                                up_left_var, up_right_var, 
                                                down_left_var, down_right_var))
            file2.write("{}{}{}{}{}{}{}{}".format(i, j, terraintype, variation, 
                                                up_left_var, up_right_var, 
                                                down_left_var, down_right_var))
