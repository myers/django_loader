# django_loader

I found myself writing the same code at the top of script to load the django
env.  I extracted that into this module.  As long as the script is in a
subdir of your django project it should find the settings file and load up
the env.



## example

in `myproject/scripts/foo.py`

    #!/usr/bin/env python
    import django_loader
    
    from myapp.models import Foo
    print Foo.objects.all()

