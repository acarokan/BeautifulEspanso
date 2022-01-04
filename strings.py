import os

giris = """# espanso configuration file

# This is the default configuration file, change it as you like it
# You can refer to the official documentation:
# https://espanso.org/docs/

# Matches are the substitution rules, when you type the "trigger" string
# it gets replaced by the "replace" string.
matches:
  # Simple text replacement
  - trigger: ":espanso"
    replace: "Hi there!"

  # Dates
  - trigger: ":date"
    replace: "{{mydate}}"
    vars:
      - name: mydate
        type: date
        params:
          format: "%d/%m/%Y"

  # Shell commands
  - trigger: ":shell"
    replace: "{{output}}"
    vars:
      - name: output
        type: shell
        params:
          cmd: "echo Hello from your shell"

#bizimkiler"""

ekle ='\n\n  - trigger: ":{}"\n    replace: \"{}"'
biz = "#bizimkiler"
trg = "  - trigger: "
rep = "    replace: "

path = os.path.join(os.environ['HOMEPATH'],"AppData","Roaming","espanso")
path_yedek = os.path.join(os.environ['USERPROFILE'],"OneDrive","Masaüstü")
anadosya = os.path.join(path, "default.yml")
yedekdosya = os.path.join(path_yedek, "default_yedek.yml")
