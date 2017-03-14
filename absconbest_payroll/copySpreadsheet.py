import os
import shutil

# Moving absconbest_payroll.xlsx to the folder created
# in Desktop.

# The function parameter is just for convenience. It does
# not mean dir_home is moved. Instead, we will move dir_xlsx.
def main(dir_home):
    # Make the target directory.
    os.makedirs(dir_home)

    # Copy absconbest_payroll.xlsx into the desktop folder.
    shutil.copy2('absconbest_payroll.xlsx', dir_home)