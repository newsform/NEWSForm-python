# ./newsform-python.py: Main module file for the NEWSForm python parser. 
# 
# Copyright (C) 2019, NEWSForm Contributors.
# 
# Released under GPLv3 license

import json
import datetime

class NFDataEntity:
    """Data entity for NEWSForm objects and instances. Instances are directly used to create JSON files."""
    

class NFObject (NFDataEntity):
    """Class describing a NEWSForm Object. The instance would describe a single NEWSForm file/object."""

    def __init__(self, string = None, isDecentralized = None, decentralizationAlgo = None, metaData = None):
        if string is not None:
            pass

        if isDecentralized is not None:
            # Safety check
            if decentralizationAlgo is None:
                raise ValueError("If isDecentralized is set to true, you must specify decentralizationAlgo.")
            if decentralizationAlgo is not None:
                raise NotImplementedError("Sorry :(")
            pass

        if metaData is None:
            raise Warning("You must specify MetaData to complete this NEWSForm object.")

        if metaData is not None:
            self.setMetaData(metaData)
            

    # Queries
    def isDecentralized (self) :
        # TODO
        return True
        
    def getLatest (self):
        # Returns a NFEntry object. This is the simplist returning option if you want to show something to frontend.
        # TODO
        return None


    # Manipulation
    def setMetaData (self, metaData):
        # TODO: Set MetaData
        pass

    def update (self, data = None, timestamp = None):
        # Safety check
        if data is None:
            raise Warning("You cannot update the object if no data is specified. This operation is not performed.")
            return None
        if timestamp is None:
            if self.isDecentralized():
                raise Warning("You cannot update the object without a timestamp if decentralized is on for safety reasons. This operation is not performed.")
                return None
            timestamp = datetime.datetime.now().timestamp()