# utility functions
def printSatImg(scn, scene, proj, lat_or, lon_or, width, height, llx, lly, 
                urx, ury, saveName, save_path, 
                area_id = "NAN", description = "NAN", proj_id = "NAN"):
    """
    Creates an Image (.png) of a selected area from a .nc satellite format.
    Requires satpy loaded!
    
    sorry no param & return args maybe in 1.1 
    
    Parameters
    ----------
    
    Returns
    -------
    
    """
    scn.load([scene])
    from pyresample.geometry import AreaDefinition
    proj_dict = {"proj": proj, "lat_ts": lat_or, "lon_0": lon_or}
    area_extent = (llx,lly,urx,ury)
    area_def = AreaDefinition(area_id, proj_id, description, proj_dict, width, 
                              height, area_extent)
    local_scn = scn.resample(area_def)
    local_scn.save_dataset(dataset_id =scene,
                           writer="simple_image",
                           filename=saveName, 
                           base_dir=save_path)

#Questions:
    #a) how can I create a dynamical (like paste0 command in R) 
        #path for filename and base_dir?
    #b) do I actually need to classify area_id etc. or can it be blank in the function?

def dirCreate(x):
    """
    Creates a subdirectory.
    
    Parameters
    ----------
    
    Return
    ------
    
    """
    subdir = x.exists()
    if subdir:
        print("All good! Filepath {} already exists.".format(x))
    
    else:
        x.mkdir(parents = True, exist_ok = True)
        


    # Use this file for all functions you create and might want to reuse later.
# Import them in the `main.py` script
