## Click Tools

A set of commands to automate some processes.  
The application uses **[click](https://click.palletsprojects.com/en/8.0.x/)** Python package.

### Setup

- Clone the repository to a location on your computer.
- Change directory into the **_click_tools_** directory.
- Type `pip install -e .` to install the required packages and set up the commands on your machine.

### Commands

- `concat-files`
  - Takes multiple text files and joins the contents into an output file.
  - The output file should be specified last and does not need to exist.

### Running Tests

- Was written with **[pytest](https://docs.pytest.org/en/6.2.x/contents.html)** package.
- Tests for the commands are available in the _tests_ folder.
- One can run them by typing `pytest tests/` if you are in the root of the folder.
