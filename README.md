## Introduction to Unit Testing

Unit testing is a software testing technique that involves testing individual units is the smallest testable part of an application, such as a function, method, or class. By testing units in isolation from the rest of the application, developers can catch and fix bugs earlier in the development process and ensure that the code is reliable and maintainable.

![image](https://github.com/user-attachments/assets/a244664f-74c2-4682-b211-7dc216dc636d)


## Why Unit Testing is important

There are several reasons why unit testing is important:

**Early Bug Detection**: By testing units in isolation, developers can catch and fix bugs earlier in the developement process, before they have a chance to propagate throughout the application and cause more significant issues.

**Improved Code Quality**: Unit testing helps ensure that code is reliable, maintainable, and meets the requirements of the application.

**Faster Development Cycles**: By catching and fixing bugs earlier in the development process, developers can avoid costly delays and shorten development cycles.

**Better Collaboration**: Unit Testing helps improve collaboration between developers and testers by providing a common framework for testing and verifying the functionlity of the code.


## Types of Tesing

There are various types of testing that are used in software development. Here are some of the most common types:

**Unit Testing**: Testing individual  units or components of the code to ensure they are working as expected.

**Integration Testing**: Testing how different modules or components of the system work together.

**System Testing**: Testing the entire system as a whole, to ensure it meets the specified requirements.

**Acceptance Testing**: Testing to ensure that the system meets the business or user requirements.

**Regression Testing**: Testing to ensure that previously working functionality is still working as expected after changes or updates.

**Performance Testing**: Testing to ensure that the system meets performance requirements and can handle expected levels of traffic.


## Bash Environment Commands

- To Create a file

```bash

touch <file_name>
# Example: touch Test_Excercise.py
```

- Run python (.py) file:

```bash
python file_name.py

```

- To Create a virtual environment

```bash

python -m venv <env_name>
# Example: python -m venv unittest
```

- Activate the virtual environment

```bash

source <env_name>/bin/activate  # for macos
source <env_name>/Scripts/activate
# Example for macos: source unittest/bin/activate
# Example for window bash: source unittest/Scripts/activate
```
- Deactivate the virtual environment

```bash

deactivate
```

- Delete the environment

```bash

rm -rf <env_name>
# Example: rm -rf unittest
```

- Useful Bash Tips for Environment Management

List Python virtual environments if stored in a folder (e.g., `~/venvs`)

```bash

ls ~/venvs
```

Find all virtual environments on your system (search for `activate` scripts)

```bash

find ~ -type f -name "activate"
```

Quick script to list venv env names inside `~/venvs`

```bash

for dir in ~/venvs/*; do
  if [ -f "$dir/bin/activate" ]; then
    echo "$(basename "$dir")"
  fi
done
```

## Pip Commands

- To install requirements.txt = `pip install -r requirements.txt`
- To check install packages = `pip list`
- To check detailed about package = `pip show package_name`
- To install package = `pip install package_name`
- To uninstall package = `pip uninstall package_name`
- To save all packages of env to a requirements.txt file = `pip freeze > requirements.txt`

## Git commands

- To add all file = `git add .`
- To add any particular file = `git add <file_name>`
- To commit = `git commit -m "commit message"`
- To push the code = `git push origin main`
