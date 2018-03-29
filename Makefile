clean:
    rm -rf venv
    rm -rf dist
    rm -rf build
    rm -rf *.egg-info
    rm -f MANIFEST
 
package: clean
    python setup.py bdist_egg
 
init-env: package
    /home/christoph/.local/bin/virtualenv venv
    venv/bin/python --version
    venv/bin/pip list
 
install-local: init-env
    venv/bin/easy_install dist/*.egg
    venv/bin/pip list
 
run-local: install
    venv/bin/python -m mywebserver
