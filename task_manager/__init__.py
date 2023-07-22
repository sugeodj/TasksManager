# task_manager/__init__.py

# Import the main functions from the tasks module so that users can access them directly
from .tasks import add_task, view_tasks, complete_task, delete_task

# Optionally, you can define any utility functions or classes that are relevant to the package
# and should be available at the package level
# from .utils import some_util_function, SomeUtilityClass

# Package-level initialization code (optional)
# This will be executed when the task_manager package is imported
# You can use this section for any initialization tasks specific to your package
# For example, initializing a global variable or setting up configuration parameters
# print("Initializing task_manager package...")

# You can also specify what symbols should be imported when someone uses 'from task_manager import *'
__all__ = ["add_task", "view_tasks", "complete_task", "delete_task"]
