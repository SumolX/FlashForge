# Firmware Compatibility
Latest tested firmware is from Feburary 2023 and works without issue.
* Firmware/FlashForge-Adventurer-4-Firmware-V2.2.4-2.3.zip

# FlashForge GX File Generation (Required Step with Latest Firmware)
Adventurer 4 built-in display is capable in displaying full color PNG images via the .gx file format.  This plugin allows for OrcaSlicer to generate GX compatible file which is supported by both FlashPrint and the Adventurer 4 printer.  Thumbnail previews are only available in the GX File Format.
### Dependencies
* Scripts/FlashForgeAdapter.zip
* Scripts/FlashForgeAdapter.py
* Scripts/gx.py
* Requires python >= 3.10 and both Python scripts above are required

### Replace Default G-Code Filename Extension (.gcode -> .gx)
* Orcaslicer -> Others-> G-code output -> Filename format:

From
```
{input_filename_base}.gcode
```
To
```
{input_filename_base}.gx
```

### Linux/Windows (Python Environment)
* Orcaslicer -> Post-processing scripts:
```
python /path/to/script/FlashForgeAdapter.py
```

### macOS (Python or MiniConda Environment)
* Orcaslicer -> Post-processing scripts:
```
/path/to/script/FlashForgeAdapter.osx
```

### Windows (No Python Environment)
* Download and extract: *Scripts/FlashForgeAdapter.zip*
* Orcaslicer -> Post-processing scripts:
```
c:\path\to\executable\FlashForgeAdapter\FlashForgeAdapter.exe
```

# Author
* Paulo Cabral (SumolX)

# Donation
If you enjoyed this work or would like to see additional tuned filaments please feel free to donate or join my patreon.

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://www.paypal.com/donate/?hosted_button_id=E4DSQMLR5JUXS)

[<img src="https://brandlogos.net/wp-content/uploads/2021/12/Patreon_logo_old-1536x352.png" width="88" height="20"/>](https://patreon.com/sumolx?utm_medium=unknown&utm_source=join_link&utm_campaign=creatorshare_creator&utm_content=copyLink)

# Support
[![discord](https://theme.zdassets.com/theme_assets/678183/cc59daa07820943e943c2fc283b9079d7003ff76.svg)](https://discord.gg/rRzp63MJtu)
