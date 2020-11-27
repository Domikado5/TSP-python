# To run application:
## 1. Make your virtual environment.
   - ``python -m venv venv``
## 2. Install required packages.
   - ``pip install -r requirements.txt``
## 3. Run flask app.
   - ``export FLASK_APP=run.py``
   - ``flask run``
   > If you want to run the application in debug mode type before typing ``flask run``
   - `export FLASK_ENV=development`
   > Your app should be running on [localhost](http://127.0.0.1:5000/)