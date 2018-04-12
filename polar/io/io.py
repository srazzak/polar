from itertools import chain
from io import BytesIO
import os
import pyarrow as pa


def _create_schema():
    """Create a schema based on arrays"""

def _infer_type(bytestream: bytearray):
    """Infer the data type of bytes object"""


def _cast_type():
    """Cast data type for entire array"""

def _create_batch():
    """Create a record batch from arrays"""

def _get_array_count(osFile: pa.OSFile):
    """Get offsets for csv file"""

    offsets = []

    start = 0
    total_size = osFile.size()

    for line in bytes.splitlines(osFile):
        osFile.seek(0)


def _read_csv_with_offset(fn, start, end, header=b'', kwargs={}):
    """Read csv with offsets"""

def read_csv(filepath, sep=','):
    """Read csv and load to frame obj"""

    csv_file = pa.OSFile(filepath)
