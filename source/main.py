from typing import List

import PyPDF2 as pydf
import os
import glob


def getFileName():
    path = '../inputData'

    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.pdf' in file:
                files.append(os.path.join(r, file))
    return files


if __name__ == '__main__':
    files = getFileName()

