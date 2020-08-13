import sys

try:
    if sys.version_info[0] > 2:
        from scripts.accipyter3 import main
    else:
        from scripts.accipyter2 import main
except ImportError:
    print('Import error')

main()
