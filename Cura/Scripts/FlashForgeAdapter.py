# Copyright (c) 2022 Paulo Cabral (SumolX)
# This PostProcessingPlugin is released under the terms of the MIT License.

from ..Script import Script
from typing import List
from UM.Application import Application

import re

class Regex():
    def __init__(self, searchText, replaceText):
        self.searchText = searchText
        self.replaceText = replaceText

class FlashForgeAdapter(Script):
    def __init__(self):
        super().__init__()

    def getSettingDataString(self):
        return """{
            "name": "FlashForge Adapter",
            "key": "FlashForgeAdapter",
            "metadata": {},
            "version": 2,
            "settings":
            {
                "machine_type":
                {
                    "label": "Machine Type",
                    "description": "FlashForge machine specific g-code modifier.",
                    "type": "enum",
                    "options":
                    {
                        "ADV4": "Adventurer 4 Series"
                    },
                    "default_value": "ADV4"
                }
            }
        }"""
  
    def initRegex(self):
        self.machineType = self.getSettingValueByKey("machine_type")
        self.layerHeight = str(Application.getInstance().getGlobalContainerStack().getProperty("layer_height", "value"))
        
        self.common = []
        self.common.append(Regex(r'M104 S(.*)\.[0-9]', r'M104 S\1'))
        self.common.append(Regex(';LAYER_COUNT:', ';layer_count:'))
        self.common.append(Regex(';LAYER:(.*)', ';layer:' + self.layerHeight))
        self.common.append(Regex(';TYPE:', ';structure:'))
        self.common.append(Regex(':WALL-OUTER', ':shell-outer'))
        self.common.append(Regex(':WALL-INNER', ':shell-inner'))
        self.common.append(Regex(':SKIN', ':infill-sparse'))
        self.common.append(Regex(':FILL', ':infill-solid'))

        self.adv4 = []
        self.adv4.append(Regex(r';Generated with Cura[\s\S]*?;ADV4', ';Generated with Cura\n;ADV4'))

        self.target = {
            'ADV4': self.adv4
        }

    def updateText(self, data, table):
        for item in table:
            searchRegex = re.compile(item.searchText)

            for layer in data:
                index = data.index(layer)
                lines = layer.split("\n")
                # Single-Line substitution
                for line in lines:
                    if re.match(searchRegex, line):                        
                        data[index] = re.sub(searchRegex, item.replaceText, layer)
                # Multi-Line substitution
                data[index] = re.sub(searchRegex, item.replaceText, layer)

        return data

    def execute(self, data):
        self.initRegex()
        
        data = self.updateText(data, self.target[self.machineType])
        data = self.updateText(data, self.common)

        return data
