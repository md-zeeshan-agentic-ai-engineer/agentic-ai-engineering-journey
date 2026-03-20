# Day 1 — Linux Introduction

## What is Linux?

Linux is an open-source operating system based on Unix.  
It is widely used in servers, cloud computing, and development environments.

### Key Features:
- Open-source (free to use)
- Secure and stable
- Highly customizable
- Used by developers and companies worldwide

---

## What is Terminal?

The terminal is a command-line interface (CLI) used to interact with the Linux system.

Instead of using a graphical interface (GUI), you type commands to perform tasks.

---

## Basic Commands

### pwd (Print Working Directory)
- Shows the current directory you are in
- Example:
```bash
pwd


# Day 2 — File Navigation

## What is File Navigation?

File navigation in Linux means moving between directories (folders) using terminal commands.

It is an essential skill for working efficiently in a Linux environment.

---

## Basic Navigation Commands

### cd (Change Directory)

The `cd` command is used to move between directories.

#### Examples:

```bash
cd folder_name

# Day 3 — File Operations

## What are File Operations?

File operations in Linux allow you to create, delete, copy, and move files and directories.

These commands are essential for managing files in a system.

---

## Basic File Commands

### touch

The `touch` command is used to create a new file.

#### Example:

```bash
touch file.txt
# Day 4 - Linux File Viewing Commands

## cat (Concatenate)
- Use: View the entire file at once
- Command:
  cat test.txt
- Best for: Small files
- Drawback: Can flood the terminal with large files

---

## less (Most Important)
- Use: Scroll and search through a file
- Command:
  less test.txt
- Features:
  - Scroll up and down
  - Search using: /word
  - Exit using: q
- Best for: Large files

---

## head
- Use: View the beginning of a file
- Command:
  head test.txt
- Default: Shows first 10 lines
- Custom:
  head -n 5 test.txt

---

## tail
- Use: View the last lines of a file
- Command:
  tail test.txt

---

## tail -f (Real-time monitoring)
- Use: Monitor live updates in a file
- Command:
  tail -f test.txt

---

## Real Examples

- Monitor logs:
  tail -f logs.txt

- Quickly view a small file:
  cat small_file.txt

- Read a large file:
  less big_file.txt

- View first few lines:
  head -n 5 file.txt

- View last few lines:
  tail -n 5 file.txt
  ---

#  Day 5 - Linux Permissions (chmod)

##  What is chmod?
`chmod` is used to change file permissions in Linux.

Permissions:
- r = read
- w = write
- x = execute

---

##  Permission Structure

Example:
-rwxr-xr-x

- Owner → rwx (read, write, execute)
- Group → r-x (read, execute)
- Others → r-x (read, execute)

---

##  Common chmod Commands

### Make file executable
chmod +x script.sh

### Remove write permission
chmod -w script.sh

### Give full permission (NOT SAFE)
chmod 777 script.sh

### Best practice (recommended)
chmod 755 script.sh

### Read-only file
chmod 644 file.txt

---

##  Meaning of Numbers

- 7 = read + write + execute
- 6 = read + write
- 5 = read + execute
- 4 = read only

Example:
- 755 → owner (full), others (read + execute)
- 644 → owner (read + write), others (read only)

---

##  Important Notes

- Avoid using 777 (security risk)
- Use 755 for scripts
- Use 644 for normal files
- Use 700 for private files

---

##  Practice Done

Commands used:
chmod +x script.sh
chmod -w script.sh
chmod 755 script.sh
chmod 777 script.sh

Checked using:
ls -l

---

# Day 6 - Package Management (APT) + Git

## Goal
- Learn how to install, update, upgrade, and remove software in Linux
- Understand basic package and dependency management
- Learn basic Git verification

---

## Core APT Commands

### Update Package List
```bash
sudo apt update

### Upgrade Installed Packages
```bash
sudo apt upgrade

### Install a Package
```bash
sudo apt install <package-name>

### Remove a Package
```bash
sudo apt remove <package-name>

### Check Installed Tool
```bash
tree

### Install Git
```bash
sudo apt install git

### Check Git Version
```bash
git --version

### Important Notes
- Always run `apt update` before installing packages
- Do not install unknown packages blindly
- Remove unused packages to keep system clean
- Git is essential for version control