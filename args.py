import argparse



# params:
# - repo_name
# - mode (week, weekend, all)
# - backrange

def use_args():
    parser = argparse.ArgumentParser(prog="Wingman", description='Take care of your git activity log')

    parser.add_argument('backrange', metavar='RANGE', type=int, help='influence backrange in days')
    parser.add_argument('-n', metavar="REPO_NAME", dest='repo_name', help='set the cellar repo name')
    parser.add_argument('-m', dest='mode', help='set the cellar repo name')

    return parser.parse_args()
