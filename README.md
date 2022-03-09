## Click Tools

A set of commands to automate some processes.  
The commands were built using the **[click](https://click.palletsprojects.com/en/8.0.x/)** Python package.

### Setup

- Clone the repository to a location on your computer.
- Change directory into the **_click_tools_** directory.
- Type `pip install -e .` to install the required packages and set up the commands on your machine.

### Commands

- `concat_files`:

  - Takes multiple text files and joins the contents into an output file.
  - The output file should be specified last and does not need to exist.
  - _[Implementation](https://github.com/maryjonah-turntabl/mary-python-automation/blob/main/click_tools/file_concat.py)_

- `confirm_ttlbr`:

  - A command to confirm a if a user works at turntabl using their email address.
  - Displays a welcome message with the user's name in title case else informs user the service is available to staff only.
  - _[Implementation](https://github.com/maryjonah-turntabl/mary-python-automation/blob/main/click_tools/confirm_ttlbrr.py)_

### Demo

- `concat_files`:  
  <img src="https://github.com/maryjonah-turntabl/Mary-Python-Automation/blob/main/img/concat_file_img.PNG" width="600" height="300">

- `confirm_ttlbr`:  
  <img src="https://github.com/maryjonah-turntabl/Mary-Python-Automation/blob/main/img/confirm_ttlbr.PNG" width="600" height="200">

### Running Tests

- Was written with **[pytest](https://docs.pytest.org/en/6.2.x/contents.html)** package.
- Tests for the commands are available in the _tests_ folder.
- One can run them by typing `pytest tests/` if you are in the root of the folder.
