# mypy-test

Sandbox for testing mypy. Specifically, mypy linting of external packages.

## Sandboxing

### Building `package`

From the package directory (`./package`), create a binary distribution:

```python setup.py sdist bdist_wheel```

### Installing `package`

From the top-level directory:

- Uninstall any pre-existing install

```pip uninstall package```

- Install the new distribution

```pip install package/dist/package-0.0.1-py3-none-any.whl```

### Running mypy

Then just run mypy on `script.py`, the expected output is:

```
script.py:5: error: Incompatible types in assignment (expression has type "str", variable has type "int")
script.py:6: error: Incompatible types in assignment (expression has type "int", variable has type "str")
Found 2 errors in 1 file (checked 1 source file)
```
