import argparse



# params:
# - repo_name
# - mode (week, weekend, all)
# - backrange

def use_args():
    parser = argparse.ArgumentParser(prog="Wingman", description='Take care of your git activity log')

    parser.add_argument('backrange', metavar='RANGE', type=int, help='Influence backrange in days')
    parser.add_argument('-n', metavar="REPO_NAME", dest='repo_name', help='Set the cellar repo name')
    parser.add_argument('-m', dest='mode', help='Set the mode. Use consts:')
    parser.add_argument('WEEK', action='store_const', const="week", help='Only Mon-Fri')
    parser.add_argument('WEEKEND', action='store_const', const="weekend", help='Only Sat-Sun')
    parser.add_argument('ALL', action='store_const', const="all", help='All days of the week')


    return parser.parse_args()
