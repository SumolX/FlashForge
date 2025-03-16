# Firmware Compatibility
Latest tested firmware is from Feburary 2023 and works without issue.
* Firmware/FlashForge-Adventurer-4-Firmware-V2.2.4-2.3.zip

# Import Configuration Bundle
* Bundles/FlashForge_Adventurer_4.ini
* Configuration, print and filament profiles have been tuned for the Adventurer 4 printer.
* All post-processing is done within PrusaSlicer and there is no external script dependencies.
* Export G-Code can directly forward gcode to FlashPrint in order to upload file to printer via network.

# FlashForge GX File Generation (Required Step with Latest Firmware)
Adventurer 4 built-in display is capable in displaying full color PNG images via the .gx file format.  This plugin allows for PrusaSlicer to generate GX compatible file which is supported by both FlashPrint and the Adventurer 4 printer.  Thumbnail previews are only available in the GX File Format.
### Dependencies
* Scripts/FlashForgeAdapter.zip
* Scripts/FlashForgeAdapter.py
* Scripts/gx.py
* Requires python >= 3.10 and both Python scripts above are required

### Replace Default G-Code Filename Extension (.gcode -> .gx)
* PrusaSlicer -> Print Settings-> Output options -> Output file:
```
Output filename format: [input_filename_base].gx
```

### Linux/Windows (Python Environment)
* PrusaSlicer -> Print Settings-> Output options -> Post-processing scripts:
```
python /path/to/script/FlashForgeAdapter.py
```

### macOS (Python or MiniConda Environment)
* PrusaSlicer -> Print Settings-> Output options -> Post-processing scripts:
```
/path/to/script/FlashForgeAdapter.osx
```

### Windows (No Python Environment)
* Download and extract: *Scripts/FlashForgeAdapter.zip*
* PrusaSlicer -> Print Settings-> Output options -> Post-processing scripts:
```
c:\path\to\executable\FlashForgeAdapter\FlashForgeAdapter.exe
```

### Auto load FlashPrint Upon G-Code Export (Windows Example)
* PrusaSlicer -> Print Settings-> Output options -> Post-processing scripts:
```
c:\path\to\executable\FlashForgeAdapter\FlashForgeAdapter.exe --ffslicer="C:\Program Files\FlashForge\FlashPrint 5\FlashPrint.exe"
```

# Note
* Legacy Adventurer 4 configuration bundle can be found within Archive/

# PrusaSlicer Dload Link:
* https://www.prusa3d.com/page/prusaslicer_424/ 

# Angus on Makers Muse
* How to Control EVERY setting using Prusa Slicer 2.4.1
* https://www.youtube.com/watch?v=Z7eKL7AhzNg&t=255s 

# Special Thanks
* Don deCourcelle
* https://www.youtube.com/watch?v=Kz5Kc8BMcpo&t=7s
* For coming up with the original G-Code and Adventure 4 PrucaSlicer bundle.

# Author
* Paulo Cabral (SumolX)

# Donation
If you enjoyed this work or would like to see additional tuned filaments please feel free to donate or join my patreon.

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://www.paypal.com/donate/?hosted_button_id=E4DSQMLR5JUXS)

[<img src="https://brandlogos.net/wp-content/uploads/2021/12/Patreon_logo_old-1536x352.png" width="88" height="20"/>](https://patreon.com/sumolx?utm_medium=unknown&utm_source=join_link&utm_campaign=creatorshare_creator&utm_content=copyLink)

# Support
[![discord](https://theme.zdassets.com/theme_assets/678183/cc59daa07820943e943c2fc283b9079d7003ff76.svg)](https://discord.gg/rRzp63MJtu)
