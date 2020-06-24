Simple python container app template
===

This is basically a template for building simple python container application.

Code to build the app:

```console
$ python setup.py sdist bdist_wheel
```

Building app img:
```console
$ docker build -t myimg .
```
Running a container:
```console
docker run -d --name mycontainer myimg
```