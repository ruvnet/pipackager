# pipackager
```
   ___ _____  ___           _                         
  / _ \\_   \/ _ \__ _  ___| | ____ _  __ _  ___ _ __ 
 / /_)/ / /\/ /_)/ _` |/ __| |/ / _` |/ _` |/ _ | '__|
/ ___/\/ /_/ ___| (_| | (__|   | (_| | (_| |  __| |   
\/   \____/\/    \__,_|\___|_|\_\__,_|\__, |\___|_|   
                                      |___/           
Created by rUv
```

```
***********************************
*        PyPI Package Manager     *
*              by rUv             *
***********************************
1. Initial Setup
2. Clean old distributions
3. Build new distributions
4. Upload distributions to PyPI
5. Increment version number (patch)
6. Increment version number (minor)
7. Increment version number (major)
8. Advanced options
9. Help
10. Exit
Select an option: 
```

`pipackager` is a comprehensive tool designed to manage your PyPI package, simplifying tasks such as cleaning old distributions, building new ones, uploading to PyPI, version incrementing, and more.

## Installation

To install `pipackager`, use pip:

```bash
pip install pipackager
```

## Usage

You can start the tool by running:

```bash
pipackager
```

This will launch an interactive menu that allows you to manage your PyPI packages with ease.

## Features

### Main Features

1. **Clean Old Distributions**:
   - Removes old distribution files from the `dist` directory.

2. **Build New Distributions**:
   - Builds new distribution files (source and wheel) using `setuptools`.

3. **Upload Distributions to PyPI**:
   - Uploads the built distributions to PyPI using `twine`.

4. **Increment Version Number**:
   - **Patch**: Increments the patch version number (e.g., 0.1.0 -> 0.1.1).
   - **Minor**: Increments the minor version number (e.g., 0.1.0 -> 0.2.0).
   - **Major**: Increments the major version number (e.g., 0.1.0 -> 1.0.0).

5. **Help Overview**:
   - Provides an overview of the features and options of the tool.

### Advanced Options

1. **Create/Update GitHub Actions Workflow**:
   - Creates or updates a GitHub Actions workflow configuration file to automate build, test, and deployment processes.

2. **Run Tests Using Pytest**:
   - Executes tests using `pytest` to ensure your package is working as expected.

3. **Lint and Format Code**:
   - Lints your code using `flake8` and formats it using `black`.

4. **Check and Update Dependencies**:
   - Checks for outdated dependencies and updates them to the latest versions.

5. **Generate Start Command**:
   - Generates a start command for your library, allowing you to execute it easily from the command line.

### Environment Variables

`pipackager` requires the following environment variables for uploading distributions to PyPI:

- `TWINE_USERNAME`: Your PyPI username.
- `TWINE_PASSWORD`: Your PyPI password or token.

If these variables are not set, `pipackager` will prompt you to enter them and will export them for you.

## Example Workflow

Here is an example workflow of using `pipackager` to manage your PyPI package:

1. **Clean Old Distributions**:
   - Select option `1` to remove old distribution files.

2. **Build New Distributions**:
   - Select option `2` to build new distribution files.

3. **Increment Version Number**:
   - Select option `4`, `5`, or `6` to increment the version number (patch, minor, or major).

4. **Upload Distributions to PyPI**:
   - Select option `3` to upload the new distribution files to PyPI.

5. **Advanced Options**:
   - Select option `7` to access advanced options such as creating/updating GitHub workflows, running tests, linting and formatting code, checking and updating dependencies, or generating a start command.

## Help

To view a detailed help overview, select option `8` from the main menu.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

---

`pipackager` is designed to streamline the process of managing and deploying your Python packages to PyPI, making it easier to maintain high-quality, well-tested, and properly versioned software.