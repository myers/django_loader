""" 
Put this in your python path.  At the top of your script put 'import
django_loader'.  This will start with the directory your file is in and
search thru the parent directories until it finds a file named
'settings.py'.  It will then add that directory and it's parent to your
sys.path, and set DJANGO_SETTINGS env var.  
"""

import os, sys, traceback

class CouldNotFindSettings(StandardError):
    pass
def find_settings(current_dir):
    if current_dir == '/':
        raise CouldNotFindSettings
    if 'settings.py' in os.listdir(current_dir):
        return current_dir
    return find_settings(os.path.dirname(current_dir))
def load(filepath):
    django_project_dir = find_settings(os.path.dirname(filepath))
    django_project_name = os.path.basename(django_project_dir)

    sys.path.append(os.path.dirname(django_project_dir))
    sys.path.append(django_project_dir)
    os.environ['DJANGO_SETTINGS_MODULE']='%s.settings' % (django_project_name,)

current_filepath = os.path.realpath(os.path.normpath(os.path.join(os.getcwd(), traceback.extract_stack(limit=2)[0][0])))
load(current_filepath)
