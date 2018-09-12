import os
import re
import sys
import stat
from setuptools import find_packages, setup


## Python 3.5 or greater version is required.
print('>>> Check python version.')

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 5)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("""
==========================
Unsupported Python version
==========================
This version of openlavaMonitor requires Python {}.{} (or greater version), 
but you're trying to install it on Python {}.{}.
""".format(*(REQUIRED_PYTHON + CURRENT_PYTHON)))
    sys.exit(1)
else:
    print('    Required python version : ' + str(REQUIRED_PYTHON))
    print('    Current  python version : ' + str(CURRENT_PYTHON))


## Generate config file.
print('\n>>> Generate config file.')

installPath = os.getcwd()
dbPath = str(installPath) + '/db'
tempPath = str(installPath) + '/temp'
configFile = str(installPath) + '/monitor/conf/config.py'
print('    Config file : ' + str(configFile))

if os.path.exists(configFile):
    print('*Warning*: config file "' + str(configFile) + '" already exists, will not update it.')
else:
    try:
        with open(configFile, 'w') as CF:
            print('        installPath = "' + str(installPath) + '"')
            CF.write('installPath = "' + str(installPath) + '"\n')
            print('        dbPath      = "' + str(dbPath) + '"')
            CF.write('dbPath      = "' + str(dbPath) + '"\n')
            print('        tempPath    = "' + str(tempPath) + '"')
            CF.write('tempPath    = "' + str(tempPath) + '"\n')
        os.chmod(configFile, stat.S_IRWXU+stat.S_IRWXG+stat.S_IRWXO)
        os.chmod(dbPath, stat.S_IRWXU+stat.S_IRWXG+stat.S_IRWXO)
        os.chmod(tempPath, stat.S_IRWXU+stat.S_IRWXG+stat.S_IRWXO)
    except Exception as error:
        print('*Error*: Failed on opening config file "' + str(configFile) + '" for write: ' + str(error))
        sys.exit(1)


## Replace string "PYTHONPATH" into the real python path on all of the python files.
print('>>> Update python path for main executable programs.')

pythonFiles = ['monitor/bin/bsample.py', 'monitor/bin/bmonitor.py', 'monitor/bin/bmonitorGUI.py']
currentPython = sys.executable
currentPythonEscaping = re.sub('/', '\/', currentPython)

for pythonFile in pythonFiles:
    try:
        command = "sed -i 's/PYTHONPATH/" + str(currentPythonEscaping) + "/g' " + str(pythonFile)
        os.system(command)
    except Exception as error:
        print('*Error*: Failed on replacing real python path on file "' + str(pythonFile) + '": ' + str(error))
        sys.exit(1)


## Set setup settings.
print('\n>>> For setup settings.')

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()

setup(
    name='openlavaMonitor',
    version='1.2',
    author='yanqing.li',
    author_email='liyanqing1987@163.com',
    url='https://github.com/liyanqing1987/openlavaMonitor/',
    description=('openlavaMonitor is an open source software for openlava '
                 'data-collection, date-analysis and information display.'),
    long_description=read('README'),
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    scripts=[],
    entry_points={},
    install_requires=[],
    zip_safe=False,
    classifiers=[],
    project_urls={},
)
