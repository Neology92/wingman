from git import Repo
from args import use_args
import os

DEFAULT_REPO_NAME = "wingman-cellar"
CURR_WORKING_DIR = os.path.abspath(os.getcwd())





def main():
    print("Let's go!")
    args = use_args()
    print(args)

    # ---------------- #
    #   Action plan!   #
    # ---------------- #



    # Define mode:
    # For MVP only Mon-Fri (work-days mode)

    # Define range (how many days backwards)

    # Try to create separate repo

    # path = os.path.join(CURR_WORKING_DIR, DEFAULT_REPO_NAME)
    # repo = Repo.init(path, bare=True)

    # Try to create commit

    # Try to create commit for the past

    # Calculate week days

    # Create commit for every week day



    # ---------------- #
    #     Later...     #
    # ---------------- #

    # Use some github API to get only non-filled days

    # Maybe add mode for filling just "alone" days



if __name__ == "__main__":
    main()
