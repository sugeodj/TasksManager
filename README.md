## Description

The CLI Task Manager Tool is a command-line application that helps you manage your tasks efficiently. With this tool, you can add tasks, view your task list, mark tasks as completed, and delete tasks when they are no longer needed.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Contributing](#contributing)
- [Screenshots](#screenshots)
- [Contact](#contact)

## Installation

To use the CLI Task Manager Tool, follow these steps:

1. Install Python 3 if you haven't already. You can download it from the official Python website: [python.org](https://www.python.org/downloads/)

2. Clone this repository to your local machine:

   ```bash
   $ git clone https://github.com/your_username/task-manager.git
   $ cd task-manager

1.  Create a virtual environment (optional):

    ```bash
    $ python -m venv venv

2.  Activate the virtual environment:

    -   Windows:

        ```bash
        $ venv\Scripts\activate

    -   macOS/Linux:

        ```bash
        $ source venv/bin/activate

3.  Install the required packages firest::

    ```bash
    $ pip install -r requirements.txt

4.  Install the CLI Task Manager Tool as a package:

    ```bash
    $ pip install .

5.  Now you can use the tool from anywhere in the terminal using the `tasks` command.

Commands
--------

-   `add`: Add a new task to the task list.

-   `view`: View all tasks in the task list.

-   `complete`: Mark a task as completed.

-   `delete`: Delete a task from the task list.

For more details and command options, use `tasks -h` or `tasks --help`.

Usage
-----

Here are the basic commands to use the CLI Task Manager Tool:

-   To add a task:

    ```bash
    $ tasks add "Task description"

-   To view all tasks:

    ```bash
    $ tasks view

-   To mark a task as completed:

    ```bash
    $ tasks complete <task_id>

-   To delete a task:

    ```bash
    $ tasks delete <task_id>

Contributing
------------

We welcome contributions! If you would like to contribute to the CLI Task Manager Tool, follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Commit your changes and push to your branch.
4.  Create a pull request to the main repository's `main` branch.

Please ensure that your code follows the project's coding style and includes appropriate tests.

Screenshots
-------

![Imgur](https://i.imgur.com/fASuv28.png)
![Imgur](https://i.imgur.com/XKqjlXw.png)
![Imgur](https://i.imgur.com/QRqSHJU.png)
![Imgur](https://i.imgur.com/sueLSKl.png)

Contact
-------

If you have any questions or suggestions, feel free to contact us:

-   Author Name: [Daniel Geovanovich](https://github.com/sugeodj)
-   Email: <dgeovanovich@gmail.com>

You can also [open an issue](https://github.com/sugeodj/TasksManager/issues) if you encounter any problems or have feature requests.
