# Exercise 6
from pathlib import Path
main_dir = Path ("./")
output_dir = main_dir / "results"
import utils as uts
# 1. Read the Scene that you downloaded from the data directory using SatPy. [2P]
import satpy as satpy
files = satpy.find_files_and_readers(base_dir="./data", reader="seviri_l1b_nc")
scn = satpy.Scene(filenames=files) #save it as a satpy scene
scn.available_composite_names() #to check which composites are aviable
# 2. Load the composites "natural_color" and "convection" [2P]
scn.load(["natural_color"]) # can be skipped thanks to function printSatImg
scn.load(["convection"]) # can be skipped thanks to function printSatImg
# 3. Resample the fulldisk to the Dem. Rep. Kongo and its neighbours [4P] 
#    by defining your own area in Lambert Azimuthal Equal Area. 
#    Use the following settings:
#      - lat and lon of origin: -3/23
#      - width and height of the resulting domain: 500px
#      - projection x/y coordinates of lower left: -15E5
#      - projection x/y coordinates of upper right: 15E5 
# see function printSatImg in Task 4
# 4. Save both loaded composites of the resampled Scene as simple png images. [2P]
uts.dirCreate(output_dir) 
uts.printSatImg(scn=scn,scene="natural_color",proj="laea",lat_or=-3,lon_or=23,
                width=500,height=500, llx=-15E5,lly=-15E5,urx=15E5,ury=15E5,
                saveName="natural_color.png",save_path="results")
                #please give me feedback (see utils)!
uts.printSatImg(scn=scn,scene="convection",proj="laea",lat_or=-3,lon_or=23,
                width=500,height=500, llx=-15E5,lly=-15E5,urx=15E5,ury=15E5,
                saveName="convection.png",save_path="results")
                #please give me feedback (see utils)!