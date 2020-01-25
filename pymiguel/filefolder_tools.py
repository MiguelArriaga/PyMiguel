# -*- coding: utf-8 -*-
"""
File and folder manipulation tools.

A root is a combination of a folder and a file prefix (/path/to/file/filenameroot)

"""

import os
import inspect
import shutil
import glob


def gethome():
    """ Get Current Script folder """
    scriptf = os.path.abspath(inspect.stack()[-1][1])
    return os.path.dirname(scriptf)


def make_folder(folder, verbose=False):
    """Make folder if it does not already exist"""
    if not os.path.exists(folder):
        os.makedirs(folder)
        if verbose:
            print("folder created at: " + folder)


def rename(src, dest):
    """Rename that overwrites"""
    if os.path.isfile(dest):
        os.remove(dest)
    os.rename(src, dest)


def rm_folder_tree(folder):
    """ Deletes folder Tree (if it exists)"""
    if os.path.exists(folder):
        # TODO: add exception handling for read-only files
        shutil.rmtree(folder)


def make_root_folder(rootpath):
    """Make folder for a rootpath (FOLD/fileroot)"""
    make_folder(os.path.dirname(rootpath))


def generate_root(root_in, suffix=None):
    """ Combine root_in and suffix for a path. It's robust """

    fold, file = os.path.split(root_in)
    if suffix is None and file == "":
        name = fold
    else:
        if suffix is None:
            suffix = ""
        name = os.path.join(fold, file + suffix)
    make_root_folder(name)
    return name


def fix_ext(name, ext):
    """Add extension if it is missing"""
    if not ext[0] == '.':
        ext = '.' + ext
    if not name[-len(ext):].lower() == ext.lower():
        name = name + ext
    return name


#
def get_files(folder, extension=None, pre_name=None, mid_name=None, post_name=None):
    """Search folder and returns list of files that match name and/or extension. Equivalent to
    doing folder/pre_name*mid_name*post_name.extension

    input:
        folder -- folder to Search
        optional -- extension,pre_name,mid_name,post_name
    """

    name = "*"
    if pre_name:
        name = pre_name + "*"
    if mid_name:
        name += mid_name + "*"
    if post_name:
        name += post_name + "."

    ext = "*"
    if extension:
        if extension[0] == ".": extension = extension[1:]
        ext = extension
    name += ext

    vlist = glob.glob(os.path.join(folder, name))
    vlist.sort()

    return vlist


def any_isnew(l_input, f_output, force=False):
    """Check if any of the inputs in input list is newer than the output"""
    if force or (f_output is None) or (not os.path.isfile(f_output)):
        return True
    for f_input in l_input:
        if isnew(f_input, f_output, force=force):
            return True
    return False


def isnew(f_input, f_output, force=False):
    """Check if the input is newer than the output"""
    if force or (f_output is None) or (not os.path.isfile(f_output)):
        return True
    in_stat = os.stat(f_input).st_mtime
    out_stat = os.stat(f_output).st_mtime
    if in_stat > out_stat:
        return True
    return False
