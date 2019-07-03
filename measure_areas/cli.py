# -*- coding: utf-8 -*-

"""Console script for measure_areas."""

import click
from measure_areas.measure_areas import measure_areas


@click.command()
@click.argument('filenames', type=click.Path(exists=True), nargs=-1)
def main(filenames):
    """Console script for measure_areas."""
    if not filenames:
        print("No files specified")
        return
    for fn in filenames:
        measure_areas(fn)


if __name__ == "__main__":
    main()
