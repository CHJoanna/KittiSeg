# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 11:50:47 2015

@author: teichman
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os.path
import time
import numpy as np
import scipy as scp
import scipy.misc
import sys
from random import shuffle
import zipfile


import logging
# import utils
reload(logging)

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.DEBUG,
                    stream=sys.stdout)


def make_val_split():
    """
    Splits the Images in train and test.
    Assumes a File all.txt in data_folder.
    """

    all_file = "all.txt"
    train_file = "train.txt"
    test_file = "val.txt"
    test_num = 200

    filename = os.path.join(all_file)
    assert os.path.exists(filename), ("File not Found %s"
                                      % filename)

    files = [line for line in open(filename)]

    shuffle(files)

    train = files[:-test_num]
    test = files[-test_num:]

    train_file = os.path.join(train_file)
    test_file = os.path.join(test_file)

    with open(train_file, 'w') as file:
        for label in train:
            file.write(label)

    with open(test_file, 'w') as file:
        for label in test:
            file.write(label)


def main():
    make_val_split()


if __name__ == '__main__':
    main()
