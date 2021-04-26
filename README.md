# GUI

## Setup & Installtion

Make sure you have the latest version of Python installed.

```bash
git clone <repo-url>
```

```bash
pip install -r requirements.txt
```

## Files description
- The form.db file is the database that contain the password and user name of whoever registered an accoun. Data here depends
on the registration app
- The Dim_mich.xlsx file contains the dimensions for the manufactoring that is run in the gui 
- The gui.py contains the code for the gui window 
- The login.py is the file that must be run as follow

## Running The App, make sure you are in the right directory
- This is toac
```bash
python Login.py
```
## This code must be optimized 
- Optimaze the registration, for example add user name etc.
- gui code has repetitive if/else statements but you can definately try to use dictionaries (I tried it, but I couldn't figured out how to organized the data from excel to be called correctly)

## What neeeds to be Done  
- Make this gui a website
  -  To do this you could use flask library, and make a connection with tkinter, but you probably will need to convert all the code into html (You can always find a better way to do it)
