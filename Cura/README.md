# New Printer Setup
Create a new non-networked printer using the new printer wizard and select 'Custom FFF printer'.  Give it a name such as 'FlashForge Adventurer 4' and click next.  Enter all the information requested by copying the screenshots provided.  For G-Code you can simply copy the contents of the provided G-Code text files and paste them in their respective windows.

* Files are located within Setup/

# Post Processing
Insert the following Search and Replace Script within Modify G-Code:

* Fan Speed
  * Search:  `M106 S([0-9]*)(.*)`
  * Replace: `M106 S\1`
  * Use Regular Expressions `Checked`

* Extruder Temperature
  * Search:  `M104 S([0-9]*)(.*)`
  * Replace: `M104 S\1 T0`
  * Use Regular Expressions `Checked`
 
* Bed Temperature
  * Search:  `M140 S([0-9]*)(.*)`
  * Replace: `M140 S\1 T0`
  * Use Regular Expressions `Checked`
 
* Layer Count 
  * Search `;LAYER_COUNT:`
  * Search `;layer_count:`
  * Use Regular Expressions `NOT Checked`

* Perimeter Type
  * Search `;TYPE:`
  * Search `;structure:`
  * Use Regular Expressions `NOT Checked`

* Outer Shell
  * Search `:WALL-OUTER`
  * Search `:shell-outer`
  * Use Regular Expressions `NOT Checked`

* Inner Shell
  * Search `:WALL-INNER`
  * Search `:shell-inner`
  * Use Regular Expressions `NOT Checked`

* Infill Sparse
  * Search `:SKIN`
  * Search `:infill-sparse`
  * Use Regular Expressions `NOT Checked`

* Infill Solid
  * Search `:FILL`
  * Search `:infill-solid`
  * Use Regular Expressions `NOT Checked`

# Marketplace
Search for and install `GXWriter` from Ronaoald Consulting as this will allow you to save a FlashForge formatted GX file.  Simply select GX as your file extension when saving your G-Code.

# Author
Paulo Cabral (SumolX) 

# Donation
If you enjoyed this work or would like to see additional tuned filaments please feel free to donate.

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/donate/?hosted_button_id=E4DSQMLR5JUXS)

# Support
[![discord](https://theme.zdassets.com/theme_assets/678183/cc59daa07820943e943c2fc283b9079d7003ff76.svg)](https://discord.gg/rRzp63MJtu_)
