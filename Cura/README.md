# New Printer Setup:
Create a new non-networked printer using the new printer wizard and select 'Custom FFF printer'.  Give it a name such as 'FlashForge Adventurer 4' and click next.  Enter all the information requested by copying the screenshots provided.  For G-Code you can  simply copy the contents of the provided G-Code text files and pastethem in their respective windows.

# Printing Profiles:
A 0.2mm Draft profile has been included, simply import the profile via Manage Printer(s).  These profiles will be modified to reflect the capabilities of the printer.  Modifications such as print and travel speeds have been modified to 50mm/s and 70mms/ respectively.

# Post-Processing Scripts:
Initial script included is FlashForgeAdapter.py which allows for proper FlashPrint loading of G-Code as well as accurate real-time printing status via the display of the printer.  More enhancements are to come as proper thumbnail support, etc... stay tuned!

Copy FlashForgeAdapter.py -> C:\Users\[YOUR ACCOUNT NAME]\AppData\Roaming\cura\5.0\scripts\
Then restart Ultimate Cura 5.0 for script to become accessible.

Cura -> Extensions -> Post Processing -> Select 'Modify G-Code'
Select 'Add a script'
Select 'FlashForge Adapter' then click 'close'

Currently only one machine type is supported and that is the Adventurer 4.  However, I wrote the script in such a way we can extended it to support other printers in the future.

# Author
Paulo Cabral (SumolX) 
