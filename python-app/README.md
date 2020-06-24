Simple python app template
===

This is basically a template for building simple python application.

Code to build the app:

```console
$ python setup.py sdist bdist_wheel
```

Installing the app:
```console
$ python -m pip install dist/myapp-*.tar.gz
```

Running:
```console
$ myapp
```