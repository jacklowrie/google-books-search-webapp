# google books search webapp

This is a simple Python app that takes in a search query and then returns a list of results from the google books api. Each result includes the title (and subtitle if applicable), author(s), and publisher. It also provides a link to view each result on GoodReads.com. It was built primarily using Flask and the requests library.

## Local Installation, running the app, testing, and debugging
### Installation
  1. Make sure you have python and pip installed on your machine (pip is built into python 3.4 and later),as well as the virtualenv module. you can install python from [python.org](https://www.python.org/downloads/). . Once you have python, you can install virtualenv from the terminal with `$ python3 pip install virtualenv` `$ py pip install virtualenv` on a windows. If you added python to your path during installation, you can simply type `$ pip install virtualenv`.
  2. Download a copy of my app from this repository (master branch if you want the latest stable version) and extract it.
  3. navigate to that folder in your terminal (or command prompt) and within that folder, create your new virtual environment with the command `$ virtualenv venv` (this command will create and populate a new folder where your environment settings are stored.)
  4. activate your virtual environment On a windows, `$ venv\Scripts\activate`, and on a mac, `$ source venv/bin/activate`. This will ensure that the next step only installs the app's dependencies in your virtual environment.
  5. Now, you can install all of the modules the app requires using the requirements.txt file. use the command `$ pip install -r requirements.txt` At this point, you should have everything installed that you need to run the app. If you plan to run the included unit tests, you'll also need to install pytest with `pip install pytest` (I don't include pytest in requirements.txt because it is not needed for the app to function as intended)
### Running the app
To run the app, make sure you're in your virtual environment and use the command `$ python3 app.py` (`$ py app.py` on windows). You will now be able to access the app from a browser on your local host, port 5000 (type `localhost:5000` into the address bar of your browser).


### Testing
The installation instructions above will allow you to run this app. I've included unit tests with this app that are written with pytest, so in order to run those you will need to make sure pytest is installed in your virtual environment as well (while running your virtual environment, use the command `$ pip install pytest`). To run the unit tests, run the `pytest` command. It will automatically run all unit tests found in the directory.

### Debugging. In addition to the unit tests described above, you can also use Flask's debugger. To turn it on, in app.py, pass debug=True into app.run() on the last line of the file. line 30-31  should read:
```python
if __name__ == '__main__':
    app.run(debug=True)
```
