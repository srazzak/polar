import pyarrow as pa

class DataFrame(pa.Table):
    """Standard dataframe object"""

    def sum(self):
        """Sum of a certain value"""