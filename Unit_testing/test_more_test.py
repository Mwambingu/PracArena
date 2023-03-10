#!/usr/bin/env python3

from more_test import rm

import os.path
import tempfile
import unittest

class RmTestCase(unittest.TestCase):

  tmpfilepath = os.path.join(tempfile.gettempdir(), "tmp-testfile")

  def setUp(self):
    with open(self.tmpfilepath, "wb") as f:
      f.write("Delete me!".encode())
    
  def test_rm(self):
    rm(self.tmpfilepath)
    self.assertFalse(os.path.isfile(self.tmpfilepath), "Failed to remove the file.")

if __name__ == "__main__":
  unittest.main()