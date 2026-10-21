# Python SMIT – AIDS (Batch 27)

A shared repository containing all class material, lecture notebooks and assignments from our **Python course at SMIT**. Every student also adds their own practice work here, so that everyone can compare solutions, learn from each other and revise easily.

---

## Table of Contents

1. [Purpose](#purpose)
2. [Repository Structure](#repository-structure)
3. [Prerequisites](#prerequisites)
4. [Getting Started (Clone the Repo)](#getting-started-clone-the-repo)
5. [File Naming Convention](#file-naming-convention)
6. [Contribution Workflow (Pull Request)](#contribution-workflow-pull-request)
7. [Rules & Best Practices](#rules--best-practices)
8. [Troubleshooting](#troubleshooting)

---

## Purpose

- Keep **all class lectures** (date-wise) in one place.
- Keep **all assignments** in one place.
- Let every student **practice and submit their own work** inside the same folders, using their own name, so that it is clear who did what.
- Teach everyone a real-world workflow: **Git, GitHub, branches and Pull Requests**.

---

## Repository Structure

```
Python_SMIT_AIDS/
├── 1. 13-Aug-2026/            # Lecture 1  - Python Basics
├── 2. 18-Aug-2026/            # Lecture 2  - Python Basics 2
├── ...
├── 15. 13-Oct-2026/           # Lecture 15 - Strings 2
├── 16. 20-oct-2026/           # Lecture 16 - Functions
├── Assignments/
│   ├── Assignment 1 (29-Sep-2026)/
│   ├── Assignment 2 (08-Oct-2026)/
│   └── Assignment 3 (15-Oct-2026)/
└── README.md
```

- **Lecture folders** are named `<number>. <date>` and contain the teacher's notebook for that day.
- **Assignment folders** contain the assignment document and the solutions submitted by students.

---

## Prerequisites

Install the following **before** cloning the repository.

| Tool | Purpose | Download |
|------|---------|----------|
| **Git** | Version control, clone and push code | https://git-scm.com/downloads |
| **Python 3.10+** | Run `.py` files and notebooks | https://www.python.org/downloads/ |
| **VS Code** | Code editor | https://code.visualstudio.com/ |
| **GitHub account** | Host and collaborate on code | https://github.com/signup |

**VS Code extensions** (install from the Extensions tab):

- **Python** (Microsoft)
- **Jupyter** (Microsoft) – required to open and run `.ipynb` notebooks

> **Windows tip:** while installing Python, tick **"Add Python to PATH"**.

**Verify your installation** – open a terminal and run:

```bash
git --version
python --version
```

Both commands should print a version number.

**One-time Git setup** (use your own name and email):

```bash
git config --global user.name  "Your Name"
git config --global user.email "your-email@example.com"
```

---

## Getting Started (Clone the Repo)

1. **Open a terminal** (Git Bash / PowerShell / VS Code terminal) in the folder where you want the project.

2. **Clone the repository:**

   ```bash
   git clone https://github.com/FurqanRaza4343/Python_SMIT_AIDS.git
   ```

3. **Go into the project folder:**

   ```bash
   cd Python_SMIT_AIDS
   ```

4. **Open it in VS Code:**

   ```bash
   code .
   ```

5. **Before starting any new work, always get the latest changes:**

   ```bash
   git checkout main
   git pull origin main
   ```

---

## File Naming Convention

**Every file you add must start with your name**, followed by the topic name, then the extension (`.py` or `.ipynb`).

```
<yourname>_<topic>.<extension>
```

Use lowercase letters and underscores (no spaces) in the file name you create.

### Lecture practice

Put your file **inside the lecture folder you are practicing**.

| Lecture folder | Your file |
|----------------|-----------|
| `16. 20-oct-2026/` | `furqan_functions.ipynb` or `furqan_functions.py` |
| `15. 13-Oct-2026/` | `zain_strings.ipynb` |
| `9. 15-Sep-2026/`  | `maroof_while_loop.py` |

### Assignments

Put your file **inside that assignment's folder**, again starting with your name, then the task name.

| Assignment folder | Your file |
|-------------------|-----------|
| `Assignments/Assignment 1 (29-Sep-2026)/` | `furqan_task_1.py` |
| `Assignments/Assignment 1 (29-Sep-2026)/` | `zain_task_2.ipynb` |
| `Assignments/Assignment 2 (08-Oct-2026)/` | `maroof_strings_and_lists.ipynb` |

### Example result

```
16. 20-oct-2026/
├── HO Batch 27 20102026 Functions.ipynb   <- teacher's file (do not edit)
├── furqan_functions.ipynb
├── zain_functions.ipynb
└── maroof_functions.py
```

> Do **not** edit or delete the teacher's original files or anyone else's work. Only add or edit files that start with **your own name**.

---

## Contribution Workflow (Pull Request)

Nobody pushes directly to `main`. All work goes through a **Pull Request (PR)**.

### Step 1 – Update your local copy

```bash
git checkout main
git pull origin main
```

### Step 2 – Create your own branch

Branch name format: `<yourname>/<topic>`

```bash
git checkout -b furqan/functions
```

### Step 3 – Do your work

Create your file in the correct folder (see [File Naming Convention](#file-naming-convention)) and write your code.

### Step 4 – Stage and commit

```bash
git add .
git commit -m "Add furqan functions practice (Lecture 16)"
```

Write short, clear commit messages, for example:

- `Add zain strings practice (Lecture 15)`
- `Add maroof Task 1 solution (Assignment 1)`

### Step 5 – Push your branch

```bash
git push -u origin furqan/functions
```

> If you get a permission error, you don't have write access yet. Ask the repo owner to add you as a **collaborator**, or **Fork** the repo on GitHub, push to your fork and open the PR from there.

### Step 6 – Open a Pull Request

1. Go to the repository on GitHub.
2. Click **"Compare & pull request"** (it appears after you push).
3. Set the **base** branch to `main`.
4. Write a clear title and description, e.g.:
   - **Title:** `Furqan - Functions practice (Lecture 16)`
   - **Description:** what you added and in which folder.
5. Click **"Create pull request"**.

### Step 7 – Review and merge

The repo owner / teacher reviews your PR and merges it into `main`. If changes are requested, fix them on the same branch, commit and push again – the PR updates automatically.

### Step 8 – Clean up (after merge)

```bash
git checkout main
git pull origin main
git branch -d furqan/functions
```

---

## Rules & Best Practices

- ✅ Always **pull the latest `main`** before creating a new branch.
- ✅ One topic / assignment = one branch = one PR.
- ✅ File name **must start with your name**.
- ✅ Put files in the **correct lecture or assignment folder**.
- ✅ Make sure your notebook **runs top to bottom** without errors before you push.
- ✅ Write code on your own – copying is not learning. Looking at others' solutions to understand is fine.
- ❌ Don't push directly to `main`.
- ❌ Don't edit or delete other people's files.
- ❌ Don't commit unnecessary files (e.g. `__pycache__/`, `.ipynb_checkpoints/`, personal documents).

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `git` / `python` is not recognized | Reinstall and make sure it is added to PATH, then restart the terminal. |
| Notebook won't open or run in VS Code | Install the **Jupyter** and **Python** extensions and select a Python kernel (top-right of the notebook). |
| `Permission denied` on push | Ask to be added as a collaborator, or use a Fork. |
| Merge conflict | Run `git pull origin main`, resolve the marked conflicts in the file, then `git add .` and `git commit`. |
| Pushed to the wrong folder or name | Rename/move the file with `git mv`, commit and push again. |

---

## Maintainer

Repository owner: **Furqan Raza** – [FurqanRaza4343](https://github.com/FurqanRaza4343)

Happy coding! 🚀
