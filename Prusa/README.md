# Import Configuration Bundle
* Bundles/FlashForge_Adventurer_4.ini
* Configuration has been tuned for the Adventurer 4 printer. All post-processing is done within PrusaSlicer and there is no external script dependencies. You will be able to immediately slice and upload the generated g-code to your printer via FlashPrint or USB.

# FlashForge GX File Supported (optional)
* Scripts/FlashForgeAdapter.py
* Scripts/gx.py
* Requires python >= 3.10 and both files above are required

## Linux/macOS
PrusaSlicer -> Print Settings-> Output options -> Post-processing scripts:
```
python /path/to/script/FlashForgeAdapter.py
```

## Windows (Python Environment)
PrusaSlicer -> Print Settings-> Output options -> Post-processing scripts:
```
c:\path\to\executable\python.exe c:\path\to\script\FlashForgeAdapter.py
```

## Windows (No Python Environment)
Download and extract scripts/FlashForgeAdapter.zip
PrusaSlicer -> Print Settings-> Output options -> Post-processing scripts:
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

# Author
* Paulo Cabral (SumolX)
