=============
Measure Areas
=============

Measure areas of shapes in SVG


Install
-------

::

    git clone https://github.com/jean/measure_areas.git
    cd measure_areas
    virtualenv .
    . bin/activate
    pip install -e .

Usage
-----

Commandline usage::

        $ ./bin/measure_areas ~/Downloads/*.svg
        /home/john/Downloads/Bezier curve.svg: 3689.59938863
        /home/john/Downloads/drawing-edited.svg: 9920.76545859
        /home/john/Downloads/group(1).svg: 9920.76535806
        /home/john/Downloads/group(2).svg: 9920.76535806
        /home/john/Downloads/hexagon.svg: 6456.24459944

You can start up a server too::

        $ ./bin/measure_areas_serve
        Bottle v0.12.13 server starting up (using WSGIRefServer())...
        Listening on http://127.0.0.1:8080/
        Hit Ctrl-C to quit.

This accepts POSTs on port 8080, expecting a file under the key `upload`.

Features
--------

* Naively try and compute the total enclosed area in files given on the commandline

* Free software: MIT license

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

