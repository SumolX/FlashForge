@echo off

REM For Windows Users... add this line to the POST PROCESSING SCRIPTS field
REM     bottom of Print Settings - Output Options.  The full path name
REM     shown here is where I put this file.  Change the path 
REM            \users\don\desktop\3d print
REM     with the correct path for your PC.
REM "c:\users\don\desktop\3d print\FixGCODE.bat";

REM This Batch script uses the SED Stream editor which comes standard on Linux
REM and I think on the Mac, but for PC Windows users can be downloaded and
REM installed from:  https://sourceforge.net/projects/gnuwin32/files/sed/4.2-1/ 

Echo *** WORKING ***

REM NOTE: SED needs to run in a read/writable folder because it creates temporary files.
REM      By default it runs from the folder where Prusa Slicer is installed, which is
REM      NOT read/writable.  To correct this issue, CD (change directory) to a
REM     folder that is read/writable
REM     Failure to do this will result in Prusa Slicer generating 0 length GCODE files.
REM     Below is my read/write folder location... please change this for your PC.
cd \Users\Paulo\Documents\FlashPrint\Prusa Slicer
echo Current directory: %CD%

REM Convert blank lines to Comments by adding ";"
"c:\program files (x86)\GnuWin32\bin\sed.exe"  -i " s/^ *$/;/g"  %1

	REM These indented lines are disabled and left for Historical purposes.  Each
	REM    of these changes were how I originally debugged the Prusa GCode, one
	REM    step at a time.  I have since moved the equivalent of these over to the 
	REM    Prusa Output Options section.
	
	REM Comment out M107 (cooling fan off) cmds... actually fixes a bug in PrusaSlicer layer 1
	REM    which refuses to have the cooling fan running for 1st layer.  I wanted 10%
	REM    for my PETG so I comment out the M107 (cooling fan off) and add 10%
	REM    in my Start GCode (Printer Settings tab - Custom GCode)
	REM "c:\program files (x86)\GnuWin32\bin\sed.exe"  -i " s/^ *M107 *$/; &/g"  %1

	REM Change Z height F values to F420 like FF slicer, any add'l text move
	REM    as a comment on the next line
	REM "c:\program files (x86)\GnuWin32\bin\sed.exe"  -i " s/^ *G1 *Z[.0-9]* *F/&420\n;  was /1"  %1

	REM Change Cooling Fan fractional values to Integer (comment out decimal on next line)
	REM "c:\program files (x86)\GnuWin32\bin\sed.exe"  -i " s/^ *M106 \+S[0-9]\+/&\n;  was /g"  %1

	REM Fix Bed Temp Change (add T0 to the M140 cmd), and move inline comments on same line
	REM    if any, to next line as a comment
	REM "c:\program files (x86)\GnuWin32\bin\sed.exe"  -i " s/^ *M140 \+S[0-9]\+/& T0\n;  was /g"  %1

	REM FIX Extruder Temp (add T0 after M104 cmd) and have no inline comments after
	REM     moved to the next line.  
	REM     NOTE: only works for a Single Extruder printer and when there is no
	REM     M104 T1 command in your Start GCODE
	REM "c:\program files (x86)\GnuWin32\bin\sed.exe"  -i " s/^ *M104 \+S[0-9]\+/& T0\n;  was /g"  %1

REM To make the Adventurer 4 Touch Pannel correctly display what layer its currently
REM    printing.  We need 2 changes.  First, insert a Comment GCODE line for layercount
REM    which the user must enter from the keyboard (reading the value off the PrusaSlicer
REM    display (top of the preview slider).

set /p layercount="Enter number of layers: "

REM Generate the layercount GCODE as 1st line in a temporary file called tempjumk
echo ;layer_count: %layercount% > .\tempjunk.txt

REM Copy the rest of the Prusa Generated GCODE after that
type %1 >> .\tempjunk.txt

REM Now copy our temp file back into the Prusa GCODE, essentially replacing it
REM     with our inserted changes
type .\tempjunk.txt >%1
REM Optimization, we can copy the temp file and replace all Z: cmds in one step
REM    by doing this PIPE into sed (saves copying the file a 2nd time).  Unfortunately
REM    this also creates a temporary file named sed in the current directory
type .\tempjunk.txt | "c:\program files (x86)\GnuWin32\bin\sed.exe" " s/^ *;Z:/;layer:/g"  > %1

REM We can safely delete our temp file now
del .\tempjunk.txt

REM SED also creates temporary files with the first 3 letter of the file name being "sed"
REM     and having no 3 letter extent (like sed.exe) So delete those files now.
del .\sed????????

REM If you disable the Optimization just above, uncomment the sed code below.
REM Now here's the 2nd part.  Replace Prusa's ;Z:0.2 height comments to FF style ;layer:0.2
REM    The value after Z:___ (above 0.2) is preserved in our generated ;layer:___ comment
REM Replace Prusa GCODE that begins with ;Z: to a comment that the Adventurer 4
REM    firmware reads to display what layer you're on.  This change, and the 
REM    layer_count comment we added above will make the Adventurer 4 correctly
REM    display what layer its currently printing.
REM NOTE... see optimization above, saves copying the GCode file a 2nd time
REM    Since it was done up there... no longer need it here.
REM "c:\program files (x86)\GnuWin32\bin\sed.exe"  -i " s/^ *;Z:/;layer:/g"  %1


