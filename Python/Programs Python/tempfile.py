import tempfile
import shutil
def main():
    dirpath=tempfile.mkdtemp()
    print dirpath
    print shutil.rmtree(dirpath)

if __name__ == '__main__':
    main()
