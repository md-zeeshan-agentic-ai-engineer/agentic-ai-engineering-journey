# Linux File Viewing Commands

## 1. cat (Concatenate)
- Use: View the entire file at once
- Command:
  cat test.txt
- Best for: Small files
- Drawback: Can flood the terminal with large files

---

## 2. less (Most Important)
- Use: Scroll and search through a file
- Command:
  less test.txt
- Features:
  - Scroll up and down
  - Search using: /word
  - Exit using: q
- Best for: Large files

---

## 3. head
- Use: View the beginning of a file
- Command:
  head test.txt
- Default: Shows first 10 lines
- Custom:
  head -n 5 test.txt

---

## 4. tail
- Use: View the last lines of a file
- Command:
  tail test.txt

---

## 5. tail -f (Real-time monitoring)
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

#  Linux Permissions (chmod)

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

### 1. Make file executable
chmod +x script.sh

### 2. Remove write permission
chmod -w script.sh

### 3. Give full permission (NOT SAFE)
chmod 777 script.sh

### 4. Best practice (recommended)
chmod 755 script.sh

### 5. Read-only file
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