# PIAIC Class 13 – Batch 61, Q2  
**Instructor:** Wajahat Hussain  
**Topic:** Chat-Oriented Programming (CHOP) with Cursor AI & Building Flows with CrewAI 🚀

## 1. Chat-Oriented Programming (CHOP) and Cursor AI 📝

### What is CHOP? 🤔
- **CHOP** stands for **Chat-Oriented Programming**.
- It is a method of coding where you interact with an AI using natural language (text prompts) to generate, interpret, and debug your code.

### What is Cursor AI? 💻
- **Cursor AI** is a tool that acts as both a code interpreter and compiler.
- It has a user interface similar to Visual Studio Code (VS Code), so it feels familiar to many developers.
- **How it works:**
  - You type natural language prompts.
  - The AI uses Natural Language Processing (NLP) to understand your prompt and then generates or debugs code accordingly.
- **Note:** Cursor AI is a paid tool (around \$20). 💲

## 2. Opening Folders and Using Shortcuts in Cursor AI 🚀

### Opening a Folder 📂
- You can open a folder in Cursor AI by using the command:
  ```bash
  code .
  ```
  - This command is the same as in VS Code and opens the current directory.

### Keyboard Shortcuts in Cursor AI 🔑
- **CTRL + I:** Opens the **Composer** panel where you can type and manage your code prompts.
- **CTRL + L:** Opens the **Intelligence** panel, which provides suggestions or analyzes your code.
- **CTRL + K:** Opens the **Command Instructions** panel, giving you quick access to various commands.
- **CTRL + J:** Opens the **Terminal** within the tool.

*These shortcuts help streamline your workflow by giving quick access to different functionalities.* 👍

## 3. Integrating and Running Projects with UV in Cursor AI 🛠️

### Setting Up UV 📜
- **UV** is a tool integrated into Cursor AI that helps you run your projects.
- You can add project documentation and configure features within Cursor AI for UV.
- **Running a Project:**
  - You typically set up your project with a configuration file (like `pyproject.toml`).
  - Then, you run the project by using a script command defined in that file.
  - For example, if you add an entry like:
    ```toml
    math_demo = "project_flow01.hello:main"
    ```
    you can run the project by issuing a command such as:
    ```bash
    uv run math_demo
    ```

## 4. Demo: Creating a Python File with Maths Functions ➕➖✖️➗

### Creating the File 📝
- We created a file called `hello.py` in the folder `src/project_flow01`.
- This file defines a class `Maths` with static methods for common mathematical operations:
  - **Addition**
  - **Subtraction**
  - **Multiplication**
  - **Division** (with error handling for division by zero)
  - **Exponentiation**

### Example Code (`hello.py`) 📄
```python
class Maths:
    @staticmethod
    def add(a: float, b: float) -> float:
        """Add two numbers"""
        return a + b
    
    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Subtract b from a"""
        return a - b
    
    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers"""
        return a * b
    
    @staticmethod
    def divide(a: float, b: float) -> float:
        """Divide a by b, with error handling for zero division"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    @staticmethod
    def power(base: float, exponent: float) -> float:
        """Calculate base raised to the power of exponent"""
        return base ** exponent

def main():
    # Example usage of Maths class
    math = Maths()
    print("5 + 3 =", math.add(5, 3))
    print("10 - 4 =", math.subtract(10, 4))
    print("6 * 7 =", math.multiply(6, 7))
    print("15 / 3 =", math.divide(15, 3))
    print("2 ^ 3 =", math.power(2, 3))

if __name__ == "__main__":
    main()
```

### Updating the Project Configuration 🔧
- In the `pyproject.toml` file, add a script entry so that UV knows how to run your project:
  ```toml
  [tool.uv.scripts]
  math_demo = "project_flow01.hello:main"
  ```

### Expected Output 🎯
After running the project with:
```bash
uv run math_demo
```
You should see an output similar to:
```
5 + 3 = 8
10 - 4 = 6
6 * 7 = 42
15 / 3 = 5.0
2 ^ 3 = 8
```


## 5. Creating Flows with CrewAI 🤖

CrewAI is a framework that helps you design flows—structured sequences of functions that execute in order or based on events.

### A Simple Flow Example 📘

Here’s an example of a simple flow:
```python
from crewai.flow.flow import Flow, start, listen  # type: ignore
import time

class AuraFlow(Flow):
    @start()
    def function1(self):
        print("Pehle Main Chaloon Ga")
        time.sleep(3)

    @listen(function1)
    def function2(self):
        print("Ab main")
        time.sleep(3)
        
    @listen(function2)
    def function3(self):
        print("Aur Akhir Main Main")

def kickoff():
    obj = AuraFlow()
    obj.kickoff()
```

### Configuring the Flow in the Project 🛠️
- Add the following entry in the `pyproject.toml` file to run this flow easily:
  ```toml
  [tool.uv.scripts]
  simple_flow = "project_flow01.simple_flow:kickoff"
  ```


## 6. Example: A More Complex CrewAI Flow 🌟

Let’s create a more advanced flow that demonstrates branching based on conditions and multiple steps.

### Complex Flow Code Example 🔍
```python
from crewai.flow.flow import Flow, start, listen  # type: ignore
import time
import random

class ComplexFlow(Flow):
    @start()
    def initialize(self):
        print("Starting the complex flow...")
        time.sleep(1)
        # Generate a random number to decide the branch
        self.data = random.randint(1, 10)
        print(f"Generated number: {self.data}")

    @listen(initialize)
    def process_data(self):
        print("Processing data...")
        time.sleep(1)
        # Choose a branch based on whether the number is even or odd
        if self.data % 2 == 0:
            print(f"{self.data} is even. Proceeding with the even branch.")
            self.branch = "even"
        else:
            print(f"{self.data} is odd. Proceeding with the odd branch.")
            self.branch = "odd"

    @listen(process_data)
    def even_branch(self):
        # Execute only if the branch is even
        if getattr(self, 'branch', None) == "even":
            print("Executing operations for even data.")
            result = self.data * 2
            print(f"Result after doubling: {result}")
            self.final_result = result
        else:
            print("Skipping even branch.")

    @listen(process_data)
    def odd_branch(self):
        # Execute only if the branch is odd
        if getattr(self, 'branch', None) == "odd":
            print("Executing operations for odd data.")
            result = self.data ** 2
            print(f"Result after squaring: {result}")
            self.final_result = result
        else:
            print("Skipping odd branch.")

    @listen(even_branch, odd_branch)
    def finalize(self):
        print("Finalizing flow...")
        time.sleep(1)
        print(f"Final result: {self.final_result}")

def kickoff():
    flow = ComplexFlow()
    flow.kickoff()
```

### Updating the Project Configuration for the Complex Flow 🔧
- Add a script entry in your `pyproject.toml` file:
  ```toml
  [tool.uv.scripts]
  complex_flow = "project_flow01.complex_flow:kickoff"
  ```

---

## 7. Summary 📚

- **Cursor AI & CHOP:** We learned how to use natural language prompts to generate and debug code. Cursor AI offers an interface similar to VS Code and uses NLP to process commands.
- **Keyboard Shortcuts:** Shortcuts like CTRL + I, L, K, and J make navigation and command execution easier.
- **UV Integration:** By configuring our project (using `pyproject.toml`), we can run our scripts with UV.
- **CrewAI Flows:** We explored how to build simple and complex flows. The simple flow demonstrated sequential execution, while the complex flow showed branching based on conditions.

By understanding these tools and concepts, you can enhance your coding workflow and build more organized, interactive projects. Happy coding and keep experimenting! 😃👍

Instructor: Wajahat Hussain
