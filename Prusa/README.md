# Import Configuration Bundle
* Bundles/FlashForge_Adventurer_4.ini
* Configuration has been tuned for the Adventurer 4 printer. All post-processing is done within PrusaSlicer and there is no external script dependencies. You will be able to immediately slice and upload the generated g-code to your printer via FlashPrint or USB.
* Print Settings include both a Fine and Standard preset.
* Filament Settings include a tuned FlashForge PLA filament preset.

# FlashForge GX File Generation (optional)
* Scripts/FlashForgeAdapter.zip
* Scripts/FlashForgeAdapter.py
* Scripts/gx.py
* Requires python >= 3.10 and both Python scripts above are required
* Enjoy your Adventurer 4 built-in display, which supports full color PNG images and PrusaSlicer generated GX Files will be gray and orange instead of black and gray produced by FlashPrint.

## Replace Default G-Code Filename Extension (.gcode -> .gx)
* PrusaSlicer -> Print Settings-> Output options -> Output file:
```
Output filename format: [input_filename_base].gx
```

## Linux/macOS/Windows (Python Environment)
* PrusaSlicer -> Print Settings-> Output options -> Post-processing scripts:
```
python /path/to/script/FlashForgeAdapter.py
```

## Windows (No Python Environment)
* Download and extract scripts/FlashForgeAdapter.zip
* PrusaSlicer -> Print Settings-> Output options -> Post-processing scripts:
```
c:\path\to\executable\FlashForgeAdapter\FlashForgeAdapter.exe
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
If you enjoyed this work or would like to see additional tuned filaments please feel free to donate.

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/donate/?hosted_button_id=E4DSQMLR5JUXS)
