RustPython
==============

A Python interpreter written in Rust

# Installation

```
virtualenv venv --python=python3
source venv/bin/activate
pip install bytecode
```

# Run

Given a python file `test.py`

```
python compile_code.py test.py > test.bytecode

cd RustPython
cargo run ../test.bytecode 
```

# TODOs
* Native types => Partial
* Control flow => if(v)
* assert => OK
* Structural types (list, tuple, object)
* Strings
* Function calls => Blocked by bytecode serializer
* Modules import
* Generators


# Goals
* Support all builtin functions
* Runs the [pybenchmark](https://pybenchmarks.org/) benchmark test
* Run famous/popular python modules (which?)
* Compatible with CPython 2.7

# Rust version
rustc 1.16.0-nightly (bf6d7b665 2017-01-15)

