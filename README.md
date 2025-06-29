# 🔐 Password Generator Tool

This project includes both a **Graphical Interface (GUI)** and a **Command Line Interface (CLI)** to generate secure passwords based on user preferences.

---

## 🚀 Features Comparison

| Feature                  | GUI Version ✅                      | CLI Version ✅                       |
|--------------------------|------------------------------------|-------------------------------------|
| Adjustable Length        | ✅                                  | ✅                                   |
| Include Digits           | ✅                                  | ✅                                   |
| Include Lowercase        | ✅                                  | ✅                                   |
| Include Uppercase        | ✅                                  | ✅                                   |
| Include Symbols          | ✅                                  | ✅                                   |
| Copy to Clipboard        | ✅                                  | ✅                                   |
| Save to File             | ✅                                  | ✅                                   |
| Show/Hide Toggle         | ✅                                  | ❌                                   |
| Strength Meter           | ✅ (based on length)                | ✅ (prints label)                    |
| Interactive UI           | ✅ (Tkinter-based)                  | ❌                                   |
| Generate with only length            | ✅ Yes (fallback defaults)                                  | ❌ No (needs char types)                                   |

---

## 📏 Password Strength Logic

Strength is based **only on password length**:

| Length Range | Strength      |
|--------------|----------------|
| 1 - 4        | Very Weak 🔴    |
| 5 - 7        | Weak 🟠         |
| 8 - 10       | Moderate 🟡     |
| 11 - 13      | Strong 🟢       |
| 14+          | Very Strong ✅  |

---

## 🖼 GUI Version (Tkinter)

- Clean and interactive window.
- Toggle visibility of generated password.
- Save password to a file.
- Strength bar with color and label.

![GUI](https://github.com/user-attachments/assets/c99b0421-8557-4485-bcdc-fe362f40ce12)

---

## 🖥 CLI Version

- Runs in terminal.
- Simple questions: length, digit/symbol/uppercase/lowercase choice.
- Generates a strong password and shows strength.
- Option to save to a `.txt` file.

![CLI](https://github.com/user-attachments/assets/2a3f0826-ad9d-4a46-8e28-08a3b50d2c24)

---

## 💡 Technologies Used

- Python 3 🐍
- `random`, `string`, `json`, `tkinter`, `pyperclip`

---

## 📃 License
This project is open-source and free to use for learning or demo purposes.

---

## Made with ❤️ by Shakyasimha Das.
