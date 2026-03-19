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