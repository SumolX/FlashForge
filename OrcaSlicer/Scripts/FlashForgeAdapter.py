#!/usr/bin/env python3
# Author:   Paulo Cabral (SumolX)
# Date:     June 22, 2022
# Description:  This module implements the conversion from gcode to xgcode files.
# License:  GPLv3

from gx import GX

from PIL import Image
from io import BytesIO

import os
import sys
import base64
import shutil
import subprocess

def convertToImage(base64Thumbnail):
    im = Image.open(BytesIO(base64.b64decode(base64Thumbnail)))
    buffer = BytesIO()
    im.save(buffer, 'PNG')
    im.close()
    return buffer.getvalue()

def parseGCode(filename):
    gx = GX()
    gcode = ""
    thumbnail = ""
    inThumbnailSection = False
    

    file = open(filename, encoding='utf-8', errors='ignore')
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

        if line.startswith("; estimated printing time (normal mode)"):
            hhmmss = line.split(" = ")[1].split(" ")
            size = len(hhmmss)
            dd, hh, mm, ss = int(0), int(0), int(0), int(0)
            if size > 3:
                dd = int(hhmmss[0].split("d")[0]) * 86400
                hh = int(hhmmss[1].split("h")[0]) * 3600
                mm = int(hhmmss[2].split("m")[0]) * 60
                ss = int(hhmmss[3].split("s")[0])
            elif size > 2:
                hh = int(hhmmss[0].split("h")[0]) * 3600
                mm = int(hhmmss[1].split("m")[0]) * 60
                ss = int(hhmmss[2].split("s")[0])
            elif size > 1:
                mm = int(hhmmss[0].split("m")[0]) * 60
                ss = int(hhmmss[1].split("s")[0])
            else:
                ss = int(hhmmss[0].split("s")[0])
            gx.print_time = dd + hh + mm + ss

        if line.startswith('; filament used [mm]'):
            gx.filament_usage = int(line.split(' = ')[1].split('.')[0].strip())
            
        if line.startswith('; layer_height'):
            gx.layer_height = int(float(line.split(' = ')[1]) * 1000)

        if line.startswith('; hot_plate_temp'):
            gx.bed_temperature = int(line.split(' = ')[1])

        if line.startswith('; nozzle_temperature'):
            gx.print_temperature = int(line.split(' = ')[1])
            
        if line.startswith('; wall_loops'):
            gx.shells = int(line.split(' = ')[1])
            
        if line.startswith('; outer_wall_speed'):
            gx.print_speed = int(line.split(' = ')[1])
            
    file.close()
    
    gx.gcode = gcode.encode('latin-1', errors='ignore')
    gx.bmp = convertToImage(thumbnail)
    gx.gcode_start = gx.bitmap_start + len(gx.bmp)
    gx_file = open(filename, 'wb')
    gx_file.write(gx.encode())
    gx_file.close()

if __name__ == "__main__":
    parseGCode(sys.argv[1])
