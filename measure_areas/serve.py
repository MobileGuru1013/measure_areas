# -*- coding: utf-8 -*-

"""Console script to start a bottle server for measure_areas."""

from bottle import route, run, request
from tempfile import NamedTemporaryFile
from measure_areas import measure_areas


def main():
    """Server for measure_areas."""
    run()

@route('/', method='POST')
def measure():
    upload = request.files.get('upload', None)
    if not upload:
        return "No files specified"
    tmpfile = NamedTemporaryFile()
    upload.save(tmpfile.name)
    return measure_areas(tmpfile.name)


if __name__ == "__main__":
    main()

