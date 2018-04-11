import pyarrow as pa

def read_csv(filepath, *args, **kwargs):
    """Parser function for reading a csv file"""

    try:
        read_file = pa.OSFile(filepath, *args, **kwargs)
    except:
        print('failed')