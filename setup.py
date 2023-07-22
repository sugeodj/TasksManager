from setuptools import setup, find_packages

setup(
    name="task-manager",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "tasks=task_manager.cli:main"
        ]
    },
)
