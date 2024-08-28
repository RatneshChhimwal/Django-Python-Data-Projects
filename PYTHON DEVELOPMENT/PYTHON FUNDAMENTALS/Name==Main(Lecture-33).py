

"""
The if __name__ == "__main__" idiom is a common pattern used in Python scripts to determine
whether the script is being run directly or being imported as a module into another script.

"""

""" In Python, the __name__ variable is a built-in variable that is automatically set to the name of the current module.
When a Python script is run directly, the __name__ variable is set to the string __main__
When the script is imported as a module into another script, the __name__ variable is set to the name of the module."""

# Below is an example of how the 'if __name__ == __main__' idiom can be used:

def main():
    # Code to be run when the script is run directly
    print("Running script directly")
if __name__ == "__main__":
    main()


""" In this example, the main function contains the code that should be run when the script is run directly.
The if statement at the bottom checks whether the __name__ variable is equal to __main__. If it is, the main function is called."""


""" This idiom is useful because it allows you to reuse code from a script by importing it as a module into another script,
without running the code in the original script. For example, consider the following script:"""

def main():
    print("Running script directly")
if __name__ == "__main__":
    main()


""" If you run this script directly, it will output "Running script directly".
However, if you import it as a module into another script and call the main function from the imported module, it will not output anything:"""

import script

script.main()  # Output: "Running script directly"


""" This can be useful if you have code that you want to reuse in multiple scripts,
but you only want it to run when the script is run directly and not when it's imported as a module."""