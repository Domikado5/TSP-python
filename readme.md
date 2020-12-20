# To run application:
## 1. Make your virtual environment.
   - ``python -m venv venv``
## 2. Install required packages.
   - ``pip install -r requirements.txt``
## 3. Compile ant-colony
   - ``g++ ./ants-cpp/Ant.cpp ./ants-cpp/Colony.cpp ./ants-cpp/main.cpp -o ./aco.exe -std=c++11``
   > If you want to test aco you can type i.e. ``aco.exe ./data/input.txt 20 100 1.0 3.0 0.1``
## 4. Run flask app.
   > On lLinux and Mac
   - ``export FLASK_APP=run.py``
   - ``flask run``
   > On Windows cmd
   - ``set FLASK_APP=run.py``
   - ``flask run``
   > If you want to run the application in debug mode type before typing ``flask run``
   - ``export FLASK_ENV=development``
   - ``set FLASK_ENV=development``
   > Your app should be running on [localhost](http://127.0.0.1:5000/)