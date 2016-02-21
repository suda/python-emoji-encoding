from distutils.sysconfig import get_python_lib
from shutil import copyfile
from os import path

def main():
    here = path.abspath(path.dirname(__file__))
    print("Copying 'emoji.pth' to %s" % get_python_lib())
    copyfile(
        path.join(here, 'emoji.pth'),
        path.join(get_python_lib(), 'emoji.pth')
    )

if __name__ == '__main__':
    main()
