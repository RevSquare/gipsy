#######
Install
#######


.. code-block::  shell-session

    pip install -r requirements.txt
    python manage.py syncdb
    python manage.py loaddata fixtures/gispy.dashboard.json
    python manage.py loaddata fixtures/gispy.toolbar.json

Activate or deactivate gipsy apps in the settings & urls for testing components separately.
