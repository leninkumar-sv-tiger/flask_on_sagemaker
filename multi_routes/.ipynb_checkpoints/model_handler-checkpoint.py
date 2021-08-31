"""
ModelHandler defines an example model handler for load and inference requests for MXNet CPU models
"""
import glob
import json
import logging
import os
import re
from collections import namedtuple

import numpy as np


class ModelHandler(object):
    """
    A sample Model handler implementation.
    """

    def __init__(self):
        self.initialized = False
        print("sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")
        

    def get_model_files_prefix(self, model_dir):
        """
        Get the model prefix name for the model artifacts (symbol and parameter file).
        This assume model artifact directory contains a symbol file, parameter file,
        model shapes file and a synset file defining the labels

        :param model_dir: Path to the directory with model artifacts
        :return: prefix string for model artifact files
        """
        sym_file_suffix = ".py"
        checkpoint_prefix_regex = "{}/*{}".format(
            model_dir, sym_file_suffix
        )  # Ex output: /opt/ml/models/resnet-18/model/*-symbol.json
        checkpoint_prefix_filename = glob.glob(checkpoint_prefix_regex)[
            0
        ]  # Ex output: /opt/ml/models/resnet-18/model/resnet18-symbol.json
        checkpoint_prefix = os.path.basename(checkpoint_prefix_filename).split(sym_file_suffix)[
            0
        ]  # Ex output: resnet18
        logging.info("Prefix for the model artifacts: {}".format(checkpoint_prefix))
        return checkpoint_prefix

    
    def initialize(self, context):
        """
        Initialize model. This will be called during model loading time
        :param context: Initial context contains model server system properties.
        :return:
        """
        print("ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
        self.initialized = True
        properties = context.system_properties
        # Contains the url parameter passed to the load request
        model_dir = properties.get("model_dir")

        checkpoint_prefix = self.get_model_files_prefix(model_dir)
    
        # Load model
        try:
            self.mod = __import__(checkpoint_prefix, fromlist=[''])
            print("~~~~~~~~~~~~~~~~~~ Loaded Model ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        except Exception as e:
            print(e)
            raise
            

    def handle(self, data, context):
        """
        Call preprocess, inference and post-process functions
        :param data: input data
        :param context: mms context
        """
        print("(((((((((((((((((((((((  Preprocess  )))))))))))))))))))))))")
#         model_input = self.preprocess(data)
        
#         print("~~~~~~~~~~~~~~~~~~ Calling Prediction ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#         model_out = self.inference(model_input)
        
#         print("~~~~~~~~~~~~~~~~~~ Postprocess ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#         return self.postprocess(model_out)
        return self.mod.run_dataframe(data).to_json()


_service = ModelHandler()


def handle(data, context):
    if not _service.initialized:
        _service.initialize(context)

    if data is None:
        return None

    return _service.handle(data, context)
