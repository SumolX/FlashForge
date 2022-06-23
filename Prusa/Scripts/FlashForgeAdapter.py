#!/usr/bin/env python3
# Author:   Paulo Cabral (SumolX)
# Date:     June 22, 2022
# Description:  This module implements the conversion from gcode to xgcode files.
# License:  GPLv3

from gx import GX

from PIL import Image
from io import BytesIO

import sys
import base64

def convertToImage(base64Thumbnail):
    im = Image.open(BytesIO(base64.b64decode(base64Thumbnail)))
    buffer = BytesIO()
    im.save(buffer, 'PNG')
    im.close()
    return buffer.getvalue()

def main(filename):
    gx = GX()
    gcode = ""
    thumbnail = ""    
    inThumbnailSection = False

    file = open(filename, 'r')
    lines = file.readlines()
    
    for line in lines:
        if line.startswith('; thumbnail begin'):
            inThumbnailSection = True
            continue
        
        if line.startswith('; thumbnail end'):
            inThumbnailSection = False
            continue
            
        if inThumbnailSection:
            thumbnail = thumbnail + line[2:]
        else:
            gcode = gcode + line

        if line.startswith('; estimated printing time (normal mode)'):
            hhmmss = line.split(' = ')[1].split(' ')
            gx.print_time = (int(hhmmss[0].split('h')[0]) * 3600) + \
                            (int(hhmmss[1].split('m')[0]) * 60) + \
                            (int(hhmmss[2].split('s')[0]))

        if line.startswith('; filament used [mm]'):
            gx.filament_usage = int(line.split(' = ')[1].split('.')[0].strip())
            
        if line.startswith('; layer_height'):
            gx.layer_height = int(float(line.split(' = ')[1]) * 1000)

        if line.startswith('; bed_temperature'):
            gx.bed_temperature = int(line.split(' = ')[1])

        if line.startswith('; temperature'):
            gx.print_temperature = int(line.split(' = ')[1])
            
        if line.startswith('; perimeters ='):
            gx.shells = int(line.split(' = ')[1])
            
        if line.startswith('; max_print_speed'):
            gx.print_speed = int(line.split(' = ')[1])
            
        if line.startswith(';output_filename_format'):
            gcode_filename = line.split(' = ')[1]
            
    file.close()
    
    gx.gcode = gcode.encode('latin-1')
    gx.bmp = convertToImage(thumbnail)
    gx.gcode_start = gx.bitmap_start + len(gx.bmp)

    gx_file = open(filename, 'wb')
    gx_file.write(gx.encode())
    gx_file.close()

if __name__ == "__main__":
    main(sys.argv[1])
    