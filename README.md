# 1. HackerRank

Repository for code developed while building solutions for challenges in HackerRank

## 1.1. Index

- [1. HackerRank](#1-hackerrank)
  - [1.1. Index](#11-index)
  - [1.2. Description](#12-description)
  - [1.3. Used Versions](#13-used-versions)
  - [1.4. Used Languages](#14-used-languages)
    - [1.4.1. Java](#141-java)
    - [1.4.2. Python](#142-python)
    - [1.4.3. Javascript](#143-javascript)

## 1.2. Description

- Challenges are separated by folders named in the format `[challenge number] - [challenge name]`
- For each challenge there is a file named *description.md* which describes the challenge, inputs and expected outputs
- Each solution uses a single file, named `Solution.[language]`
- All commands listed in the following must be executed inside the challenge's folder

## 1.3. Used Versions

- Java 17.0.3
- Python 3.9.6
- Node 18.12.1

## 1.4. Used Languages

### 1.4.1. Java

Before executing Java program, we need to **compile**. For that, run the following command:

`javac Solution.java`

This command creates the *.class* files, needed for the program execution. With the files created, simply run the following to execute the Java program:

`java Solution`

Console will wait for the entries and show the outputs specified in the file *description.md*

### 1.4.2. Python

To execute the programs in Python, just run the following command:

`py Main.py` - for Windows based Operational Systems

`python3 Main.py` - for Linux based Operational Systems

Console will wait for the entries and show the outputs specified in the file *description.md*

### 1.4.3. Javascript

Due to the way Javascript handles program input, it would take several changes to run the code on Windows operating systems, so the Javascript code can only run on Linux or Mac operating systems.

To execute the programs in Javascript, just run the following command:

`node Solution.js`

Entries must be terminated with the command `Ctrl + D`. After executing this command, the program will compute the inputs and present the outputs specified in the *description.md* file
