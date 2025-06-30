 <br />
<p align="center">
  <a href="https://www.youtube.com/channel/UCX7oe66V8zyFpAJyMfPL9VA">
    <img width="250px" src="https://github.com/xiaowuc2/xiaowuc2/blob/master/source/qxr/bb.gif" alt="Logo">
  </a>

  <h3 align="center">Birthday Reminder</h3>

  <p align="center">
    Python Application | 10 lines of code + Video Explanation 🧭
    <br>
    <br />
  </p>
</p>

# 🎉 Birthday Reminder

A simple Python program to keep track of your friends' and loved ones' birthdays and show a greeting on their special day.

---

## 💡 What does it do?

- Stores a list of birthdays.
- Allows you to add new birthdays via input.
- Checks if today matches any birthday in the list.
- Prints a birthday message with the correct age and suffix (e.g., "21st", "22nd", etc.).

---

## 🛠 Requirements

- Python 3.x
- `datetime` library (built-in)

---

## 💻 Example code

```python
import datetime

current_date = datetime.date.today().strftime('%Y-%m-%d')
current_date_lst = current_date.split('-')

bday_log = [
    ('Ayushi', ('1999', '10', '19')),
    ('Yash', ('1999', '04', '21')),
]

add = input('To add birthday type y:').strip().lower()

if add[:1] == 'y':
    new = input('Add birthday in format yyyy-mm-dd:').strip()
    name = input('Whose bday?').strip()
    date = new.split('-')
    if len(date) == 3:
        bday_log.append((name, tuple(date)))
    else:
        print('Invalid date format. Skipping add.')

found = False

for birthday in bday_log:
    if current_date_lst[1] == birthday[1][1] and current_date_lst[2] == birthday[1][2]:
        age = int(current_date_lst[0]) - int(birthday[1][0])
        if 10 < age % 100 < 14:
            suffix = 'th'
        else:
            suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(age % 10, 'th')
        print(f"It's {birthday[0]}'s {age}{suffix} Birthday")
        found = True

if not found:
    print("No birthdays today.")

