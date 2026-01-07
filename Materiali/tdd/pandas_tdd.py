import pandas as pd

def get_shape(df):
    pass

def test_get_shape():
    df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    assert get_shape(df) == (2, 2)


def test_get_shape_with_empty_df():
    df = pd.DataFrame()
    assert get_shape(df) == (0, 0)

def test_get_shape_with_one_column():
    df = pd.DataFrame({'col1': [1, 2]})
    assert get_shape(df) == (2, 1)

import pandas as pd

def get_shape(df):
    return df.shape
