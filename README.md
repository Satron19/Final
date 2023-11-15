# Byte Representation Project

This project includes a Python script that converts characters and words into their byte representations. It's designed to demonstrate basic operations with ASCII values and binary conversions in Python.

## Features

### Character to Byte Conversion
This function converts a single character into its byte representation using ASCII values.
- **Example**: The character 'A' is converted as follows:
  - ASCII value: 65
  - Byte representation: '01000001'

### Word to Byte Conversion
This function converts each character in a word to its byte representation and concatenates the results.
- **Example**: The word 'Cat' is converted as follows:
  - 'C' -> ASCII: 67, Byte: '01000011'
  - 'a' -> ASCII: 97, Byte: '01100001'
  - 't' -> ASCII: 116, Byte: '01110100'
  - Combined Byte representation: '01000011 01100001 01110100'

## Team Member

- Samuel David Troncoso - [@Satron19](https://github.com/Satron19)

## Repository Workflow

### Cloning the Repository
To clone the repository, use:

git clone https://github.com/Satron19/Final.git

This command creates a local copy of the repository on your machine.

### Creating a Branch
To create and switch to a new branch, use:

git checkout -b any-name-you-want


### Committing Changes
To commit your changes, use:

git add .
git commit -m "Your commit message"

This adds all changes to the staging area and then commits them with a descriptive message.

### Pushing Changes
To push your changes to GitHub, use:


git push origin [branch-name]

### Creating a Pull Request
To merge your changes into the main branch, create a pull request through the GitHub website. This allows for code review and collaboration before integrating changes.






