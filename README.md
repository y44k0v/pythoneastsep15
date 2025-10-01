# pythoneastsep15
Autograded exercises for ComIT Web Development with Python (Django)

### About this repo


Here you will find code challenges to polish up your python skills. These exercises will imitate early stages in the Software Development Life Cycle (SDLC) for real life developer activities (on a small scale). After you write and test your code and do a PR (pull request), GitHub Actions will launch a Virtual Machine that runs your code against a battery of tests. If all is good you will see a green check mark otherwise it will show you a red X. You can explore what went wrong and what passed. 

checkout the `tests` folder to have a better idea of what you code has to accomplish.


---
### Order of exercises

You can complete any exercise you want, but to submit a pull request you have to complete the exercises in order, since tests are sequencial. If one fails the next ones don't execute. Test your code locally as noted below. 
 
1. fibonacci.py
2. bmi_calculator.py
3. test_two_number_sum.py
4. sorted_square_array.py
5. validate_subsequence.py

To get the new exercises: `sync fork`  button on GitHub or `git pull` in your CLI. Use Slack for your questions, and paste screenshots in case of errors in the `#practice` channel.

---


### Test your local repo

After Part 3 below, you can check your code locally before pushing with:

```BASH
$ python -m unittest ./tests/test_fibonacci.py -v
$ python -m unittest ./tests/test_bmi_calculator.py -v
$ python -m unittest ./tests/test_two_number_sum.py -v 
$ python -m unittest ./tests/test_sorted_square_array.py -v
$ python -m unittest ./tests/test_validate_subsequence.py -v
```

If all tests pass you can continue with Part 4.


Additionally, some tests are written inside the exercise files at the end as print statements. Execute the files directly:

```BASH
$ python two_number_sum.py 
$ python sorted_square_array.py 
$ python validate_subsequence.py
```

---

Here's a step-by-step guide to fork, clone, edit, and push changes to this GitHub repository, then create a pull request:

**Goal:** Get your changes into the original repository.

---

### **Part 1: Fork the Repository (on GitHub)**

1.  **Go to the Repository:** Open your web browser and navigate to the repository you want to fork: `https://github.com/y44k0v/pythoneastsep15.git`
2.  **Click "Fork":** In the top right corner of the page, you'll see a button labeled "Fork." Click it. 
3.  **Create Fork:** GitHub will ask you where you want to fork it. Choose your own GitHub account. This creates a *copy* of the repository under your GitHub account. This is now *your* version that you can freely change.

---

### **Part 2: Clone Your Fork to Your Local Computer**

Now you'll bring your copy of the repository from GitHub to your computer.

1.  **Go to Your Fork:** On GitHub, go to *your* forked repository (e.g., `https://github.com/YOUR_USERNAME/pythoneastsep15`).
2.  **Click "Code":** Look for a green button labeled "Code." Click it.
3.  **Copy the URL:** Make sure "HTTPS" is selected, then click the clipboard icon to copy the URL. It will look something like `https://github.com/YOUR_USERNAME/pythoneastsep15.git`.
4.  **Open Terminal/Command Prompt:**
    *   **Windows:** Search for "Command Prompt" or "Git Bash" (if you installed Git for Windows).
    *   **Mac/Linux:** Open the "Terminal" application.
5.  **Navigate to Desired Directory:** Use the `cd` command to go to where you want to save your project. For example:
    ```bash
    cd Documents/GitHub
    ```
    (If these folders don't exist, you can create them first.)
6.  **Clone the Repository:** Type `git clone` followed by the URL you copied.
    ```bash
    git clone https://github.com/YOUR_USERNAME/pythoneastsep15.git
    ```
    Press Enter. This will download your forked repository to your computer.
7.  **Enter the Directory:**
    ```bash
    cd pythoneastsep15
    ```

---

### **Part 3: Make Your Changes (Edit a File)**

1.  **Open the Project:** Use your favorite text editor (like VS Code, Sublime Text, Atom, or even Notepad/TextEdit) to open the `pythoneastsep15` folder you just cloned.
2.  **Find a File to Edit:** For this exercise, let's assume there's a file called `fibonacci.py`. Open it.
3.  **Make an Edit:** Add your code to the function following the instructions.
    
    *   *Example for `fibonacci.py`:* Add `print("Hello from my fork!")`, of course will fail the tests.
4.  **Save the File:** Save your changes in your text editor.

---

### **Part 4: Stage, Commit, and Push Your Changes**

Now you'll tell Git about your changes and send them to your GitHub fork.

1.  **Check Status:** Go back to your Terminal/Command Prompt (make sure you're still in the `pythoneastsep15` directory). See what changes Git has noticed:
    ```bash
    git status
    ```
    You should see your modified file listed in red, indicating it's not yet staged.
2.  **Stage Your Changes:** Tell Git you want to include this file in your next "commit" (a snapshot of your changes).
    ```bash
    git add .
    ```
    The `.` means "all changes in the current directory." You can also specify a file: `git add README.md`
3.  **Check Status Again:**
    ```bash
    git status
    ```
    Now your file should be listed in green, meaning it's "staged" and ready to be committed.
4.  **Commit Your Changes:** Create a snapshot of your changes with a descriptive message.
    ```bash
    git commit -m "Add my first contribution message"
    ```
    Replace `"Add my first contribution message"` with a clear summary of what you changed.
5.  **Push to GitHub:** Send your committed changes from your local computer to *your forked repository on GitHub*.
    ```bash
    git push origin main
    ```
    (Or `git push origin master` if your branch is named `master`.)
    *   You might be asked for your GitHub Personal Access Token.

---

### **Part 5: Create a Pull Request (on GitHub)**

Finally, you'll ask the original repository owner to merge your changes.

1.  **Go to Your Fork on GitHub:** Open your web browser and go to `https://github.com/YOUR_USERNAME/pythoneastsep15`.
2.  **Click "Contribute" or "Pull request":**
    *   You should see a message at the top saying "This branch is 1 commit ahead of y44k0v:main." with a "Contribute" button. Click "Contribute," then "Open pull request."
    *   Alternatively, click the "Pull requests" tab, then click the green "New pull request" button.
3.  **Review Changes:** GitHub will show you a comparison of the changes between your fork and the original repository. Make sure everything looks correct.
    
