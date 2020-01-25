# -*- coding: utf-8 -*-

from .context import pymiguel as pmig
import unittest
import os


class T(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\n === test_MA_Tools === ")
        cls.temppath = os.path.join("tests", "temp", "")
        # pmig.MakeNewDir(cls.temppath)
        cls.myfile_old = pmig.generate_root(cls.temppath, "old")
        open(cls.myfile_old, 'w+').close()
        # self.testimgpath = os.path.join(self.temppath,"MyTestImage.png")

    def test_MakeRoot(self):
        mynewfile = pmig.generate_root(self.temppath, "TEST")
        open(mynewfile, 'w+').close()
        self.assertTrue(os.path.isfile(os.path.join(self.temppath, "TEST")))

    def test_getFiles(self):
        file_name_list = ['firsttest', 'secondtest', 'thirdtest']
        for fn in file_name_list:
            fileloc = os.path.join(self.temppath, fn + ".myext")
            open(fileloc, 'w+').close()
        self.assertTrue([os.path.splitext(os.path.basename(x))[0] for x in
                         pmig.get_files(self.temppath, "myext")] == file_name_list)

    def test_IsNew(self):
        myfile_new = pmig.generate_root(self.temppath, "new")
        with open(myfile_new, 'w+') as fp:
            fp.write("example")
        self.assertFalse(pmig.isnew(self.myfile_old, myfile_new))
        self.assertTrue(pmig.isnew(myfile_new, self.myfile_old))

    @classmethod
    def tearDownClass(cls):
        pass
        # if os.path.isdir(cls.temppath): pmig.DeleteFolderTree(cls.temppath)


if __name__ == '__main__':
    unittest.main()
