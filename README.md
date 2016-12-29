"# functests"

# install
python -m pip install pytest
python -m pip install pytest-html
python -m pip install pytest-pythonpath

pytest -v

pytest test_class.py  --resultlog=./log.txt
pytest -v test_class.py --html=./report.html


# run single test suite
pytest youdao

# run single test case
pytest youdao/test_youdao_1.py::test_baidu_1_case1

# list test cases
pytest --collect-only
pytest --collect-only youdao

# get in pdb when case failed
pytest --pdb

# python library path set up
install pytest-pythonpath
add "python_paths = path1 path2" to pytest.ini

# print logging in real time
py.test --capture=no XXX.py
