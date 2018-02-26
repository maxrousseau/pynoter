import unittest 
import filecmp 
from os.path import expanduser
import sys, os
path = expanduser('~/.local/lib/python2.7/site-packages/pynoter/')
sys.path.insert(0, path)
import conv_raw

class TestPowerpoint(unittest.TestCase):
    ''' Tests for the Powerpoint class '''

    def setUp(self):
        ''' create a powerpoint object for test methods '''

        self.test_ppt_latex = conv_raw.Powerpoint('testpres.pptx', 'test2', 'latex')
        self.test_ppt_org = conv_raw.Powerpoint('testpres.pptx', 'test2', 'org')

    def test_slide_note(self):
        ''' test that slides are extracted and placed in the list '''
        self.test_ppt_latex.slide_note()
        self.assertIn('%Slide 1\n\nTest \n\n',self.test_ppt_latex.raw_text)

    def test_note_file_latex(self):
        ''' test that files are written correctly in latex'''
        self.test_ppt_latex.slide_note()
        self.test_ppt_latex.note_file()
        success = filecmp.cmp('test1.tex', 'test2.tex', shallow=False)
        self.assertTrue(success)
        
    def test_note_file_org(self):
        ''' test that files are written correctly in latex'''
        self.test_ppt_org.slide_note()
        self.test_ppt_org.note_file()
        success = filecmp.cmp('test1.org', 'test2.org', shallow=False)
        self.assertTrue(success)
        
unittest.main()

