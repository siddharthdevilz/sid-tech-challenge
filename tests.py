import pytest
import pandas as pd
import helper_modules as hp
import os

mandatory = ['purchase_id', 'customer_id', 'price', 'quantity', 'product_name']

@pytest.mark.parametrize("test_input,expected", [("file", "File is wrong format !!"), 
("filename.txt", "File is wrong format !!"), 
("filename.json", "The file does not exist !!")])
## Test wrong file name/path/extensions
def test_file_error(test_input, expected, caplog):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        hp.open_file(test_input)
        assert pytest_wrapped_e.type == SystemExit
        assert expected in caplog.text

## Test bad data in file + data load
def test_bad_data():
    f = hp.open_file('data/error1.json')
    df_org = hp.load_data(f)
    df, df_product, df_po, df_pos_total, df_error = hp.transform_data(df_org, mandatory)
    assert df_org.shape[0] == 10
    assert df.shape[0] == 6
    assert df_error.shape[0] == 4

## Test malformed json
def test_malformed_json(caplog):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        f = hp.open_file('data/error2.json')
        df_org = hp.load_data(f)
        assert pytest_wrapped_e.type == SystemExit
        assert "There was an error loading data from the file !!" in caplog.text

## Test happy path
def test_main(capfd):
    expected_output = "{\"Total volume of spend \": 3837.0, \"Average purchase value\": 1918.5, \"Maximum purchase value\": 2856.0, \"Median purchase value\": 1918.5, \"Number of unique products purchased\": 4}"
    result = os.system("python3 main.py data/error1.json")
    out, err = capfd.readouterr()
    assert result == 0 
    assert expected_output in out