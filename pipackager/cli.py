import os
import shutil
import subprocess
import sys

def show_menu():
    clear()
    print("***********************************")
    print("*        PyPI Package Manager     *")
    print("***********************************")
    print("1. Clean old distributions")
    print("2. Build new distributions")
    print("3. Upload distributions to PyPI")
    print("4. Increment version number (patch)")
    print("5. Increment version number (minor)")
    print("6. Increment version number (major)")
    print("7. Advanced options")
    print("8. Help")
    print("9. Exit")


def show_advanced_menu():
    clear()
    print("***********************************")
    print("*        Advanced Options         *")
    print("***********************************")
    print("1. Create/update .github workflow")
    print("2. Run tests using Pytest")
    print("3. Lint and format code")
    print("4. Check and update dependencies")
    print("5. Generate start command")
    print("6. Back to main menu")


def show_help():
    clear()
    print("***********************************")
    print("*           Help Overview         *")
    print("***********************************")
    print("This tool provides various options to manage your PyPI package:")
    print("")
    print("Main Menu Options:")
    print("1. Clean old distributions: Removes old distribution files.")
    print(
        "2. Build new distributions: Builds new distribution files (source and wheel)."
    )
    print("3. Upload distributions to PyPI: Uploads the built distributions to PyPI.")
    print("4. Increment version number (patch): Increments the patch version number.")
    print("5. Increment version number (minor): Increments the minor version number.")
    print("6. Increment version number (major): Increments the major version number.")
    print("7. Advanced options: Provides advanced management options.")
    print("8. Help: Displays this help overview.")
    print("9. Exit: Exits the tool.")
    print("")
    print("Advanced Menu Options:")
    print(
        "1. Create/update .github workflow: Creates or updates a GitHub Actions workflow."
    )
    print("2. Run tests using Pytest: Runs tests using Pytest.")
    print("3. Lint and format code: Lints and formats code using flake8 and black.")
    print("4. Check and update dependencies: Checks and updates package dependencies.")
    print("5. Generate start command: Generates a start command for your library.")
    print("6. Back to main menu: Returns to the main menu.")
    print("")
    input("Press any key to return to the main menu...")


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def clean_dists():
    dist_dir = 'dist'
    if os.path.exists(dist_dir):
        for filename in os.listdir(dist_dir):
            file_path = os.path.join(dist_dir, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')
        print("🗑️  Old distributions cleaned.")
    else:
        print(f'No dist directory found at {dist_dir}')

def build_dists():
    subprocess.run([sys.executable, "setup.py", "sdist", "bdist_wheel"])
    print("📦 New distributions built.")


def upload_dists():
    subprocess.run(["twine", "upload", "dist/*"])
    print("🚀 Distributions uploaded to PyPI.")

def increment_version(part):
    with open('setup.py', 'r') as file:
        setup_contents = file.read()

    version_line = [line for line in setup_contents.split('\n') if 'version=' in line][0]
    version = version_line.split('=')[1].strip().strip("'\", ")
    print(f"Parsed version: {version}")  # Debug print

    major, minor, patch = map(int, version.split('.'))

    if part == 'patch':
        patch += 1
    elif part == 'minor':
        minor += 1
        patch = 0
    elif part == 'major':
        major += 1
        minor = 0
        patch = 0

    new_version = f"{major}.{minor}.{patch}"
    new_setup_contents = setup_contents.replace(version, new_version)

    with open('setup.py', 'w') as file:
        file.write(new_setup_contents)

    print(f"🔢 Version incremented to {new_version}.")

def check_packages():
    print("🔍 Checking required Python packages...")
    required_packages = [
        "twine",
        "setuptools",
        "wheel",
        "flake8",
        "black",
        "pytest",
        "pip-upgrader",
    ]
    for package in required_packages:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "show", package], capture_output=True
        )
        if result.returncode != 0:
            print(f"⚠️  Package {package} is not installed. Installing...")
            subprocess.run([sys.executable, "-m", "pip", "install", package])
            print(f"✅ Package {package} installed.")
        else:
            print(f"✅ Package {package} is already installed.")


def check_env_vars():
    print("🔍 Checking required environment variables...")
    required_vars = ["TWINE_USERNAME", "TWINE_PASSWORD"]
    env_file = ".env"

    if os.path.exists(env_file):
        with open(env_file) as f:
            for line in f:
                var, value = line.strip().split("=")
                os.environ[var] = value

    with open(env_file, "a") as f:
        for var in required_vars:
            if os.getenv(var) is None:
                value = input(
                    f"⚠️  Environment variable {var} is not set. Please enter value: "
                )
                os.environ[var] = value
                f.write(f"{var}={value}\n")
                print(f"✅ Exported {var}={value}")
            else:
                print(f"✅ Environment variable {var} is already set.")


def create_update_workflow():
    os.makedirs(".github/workflows", exist_ok=True)
    with open(".github/workflows/python-package.yml", "w") as file:
        file.write(
            """name: Python package

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Lint with flake8
      run: |
        # stop the build if there are Python syntax errors or undefined names
        flake8 .
    - name: Test with pytest
      run: |
        pytest
"""
        )
    print("⚙️  GitHub workflow created/updated.")


def run_tests():
    subprocess.run([sys.executable, "-m", "pytest"])
    print("✅ Tests completed.")


def lint_format_code():
    subprocess.run([sys.executable, "-m", "flake8", "."])
    subprocess.run([sys.executable, "-m", "black", "."])
    print("✅ Code linted and formatted.")


def check_update_dependencies():
    if os.getenv("VIRTUAL_ENV") is None:
        choice = input(
            "⚠️  It seems you haven't activated a virtualenv.\nDo you want to skip the virtualenv check and install packages anyway? (y/n): "
        )
        if choice.lower() != "y":
            print("❌ Dependency check canceled. Please activate your virtualenv.")
            return
    subprocess.run([sys.executable, "-m", "pip-upgrader"])
    print("✅ Dependencies checked and updated.")


def generate_start_command():
    command_name = input("Enter the name for the command (e.g., mycommand): ")
    module_name = input("Enter the module to execute (e.g., pipackager.cli): ")
    function_name = input("Enter the function to execute (e.g., main): ")

    # Read the current setup.py
    with open("setup.py", "r") as file:
        setup_contents = file.readlines()

    # Find the entry_points section or add it if it doesn't exist
    entry_points_index = -1
    for i, line in enumerate(setup_contents):
        if "entry_points=" in line:
            entry_points_index = i
            break

    if entry_points_index == -1:
        # Add entry_points section
        setup_contents.insert(-1, "    entry_points={\n")
        setup_contents.insert(-1, '        "console_scripts": [\n')
        setup_contents.insert(
            -1, f'            "{command_name}={module_name}:{function_name}",\n'
        )
        setup_contents.insert(-1, "        ],\n")
        setup_contents.insert(-1, "    },\n")
    else:
        # Check for duplicate entry before adding
        entry_exists = False
        for j in range(entry_points_index, len(setup_contents)):
            if f'"{command_name}=' in setup_contents[j]:
                entry_exists = True
                break
            if "]" in setup_contents[j]:
                break

        if not entry_exists:
            # Add the new command to the existing entry_points section
            for k in range(entry_points_index, len(setup_contents)):
                if "]" in setup_contents[k]:
                    setup_contents.insert(
                        k,
                        f'            "{command_name}={module_name}:{function_name}",\n',
                    )
                    break

    # Write the updated setup.py
    with open("setup.py", "w") as file:
        file.writelines(setup_contents)

    print(f"🔧 Start command '{command_name}' added. To use it, reinstall the package.")


def source_env_file():
    env_file = ".env"
    if os.path.exists(env_file):
        with open(env_file) as f:
            for line in f:
                var, value = line.strip().split("=")
                os.environ[var] = value


def initial_checks():
    check_packages()
    check_env_vars()


def main_menu():
    while True:
        show_menu()
        choice = input("Select an option: ")

        if choice == "1":
            clean_dists()
        elif choice == "2":
            build_dists()
        elif choice == "3":
            upload_dists()
        elif choice == "4":
            increment_version("patch")
        elif choice == "5":
            increment_version("minor")
        elif choice == "6":
            increment_version("major")
        elif choice == "7":
            advanced_menu()
        elif choice == "8":
            show_help()
        elif choice == "9":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid option, please try again.")

        input("\nPress any key to continue...")


def advanced_menu():
    while True:
        show_advanced_menu()
        adv_choice = input("Select an advanced option: ")

        if adv_choice == "1":
            create_update_workflow()
        elif adv_choice == "2":
            run_tests()
        elif adv_choice == "3":
            lint_format_code()
        elif adv_choice == "4":
            check_update_dependencies()
        elif adv_choice == "5":
            generate_start_command()
        elif adv_choice == "6":
            break
        else:
            print("❌ Invalid option, please try again.")

        input("\nPress any key to continue...")


def main():
    source_env_file()
    initial_checks()
    main_menu()


if __name__ == "__main__":
    main()
