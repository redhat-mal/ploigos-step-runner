"""`StepImplementer` for the `generate-metadata` step using Git.
Step Configuration
------------------
Step configuration expected as input to this step.
Could come from:
  * static configuration
  * runtime configuration
  * previous step results
Configuration Key     | Required? | Default | Description
----------------------|-----------|---------|-----------
TODO

Result Artifacts
----------------
Results artifacts output by this step.
Result Artifact Key | Description
--------------------|------------
TODO

"""
import os
import re
import sys
from distutils.util import strtobool
from io import StringIO

import sh
from ploigos_step_runner.step_implementer import StepImplementer, StepResult

DEFAULT_CONFIG = {
}

REQUIRED_CONFIG_OR_PREVIOUS_STEP_RESULT_ARTIFACT_KEYS = [
   'container-image-registry-uri'
]

class HelloWorld(StepImplementer):  
    """StepImplementer for the generate-and-publish-workflow-report step for HelloWorld.
    """

    @staticmethod
    def step_implementer_config_defaults():
        """Getter for the StepImplementer's configuration defaults.
        Returns
        -------
        dict
            Default values to use for step configuration values.
        Notes
        -----
        These are the lowest precedence configuration values.
        """
        return DEFAULT_CONFIG

    @staticmethod
    def _required_config_or_result_keys():
        """Getter for step configuration or previous step result artifacts that are required before
        running this step.
        See Also
        --------
        _validate_required_config_or_previous_step_result_artifact_keys
        Returns
        -------
        array_list
            Array of configuration keys or previous step result artifacts
            that are required before running the step.
        """
        return REQUIRED_CONFIG_OR_PREVIOUS_STEP_RESULT_ARTIFACT_KEYS

    def _run_step(self):
        """Runs the step implemented by this StepImplementer.
        Returns
        -------
        StepResult
            Object containing the dictionary results of this step.
        """
        step_result = StepResult.from_step_implementer(self)
        image_url = self.get_value('container-image-registry-uri').lower()
        print(f"\nTODO ************ Push Data to Nexus For Image: {image_url} ****************")
        return step_result

