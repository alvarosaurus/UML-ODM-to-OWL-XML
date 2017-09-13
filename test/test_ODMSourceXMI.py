'''
Created on 13 Sep 2017

export PYTHONPATH=${PYTHONPATH}:../src
python test_ODMSourceXMI.py

@author: alvaro
'''
import unittest
from odm2owl.ODMSourceXMI import ODMSourceXMI


class test_ODMSourceXMI(unittest.TestCase):
	profilePath = "../profiles/ODM.xmi"
	testModelPath = "testdata/empty.xmi"

	def setUp(self):
		pass


	def tearDown(self):
		pass


	def test_create(self):
		"""
		Can an ODMSourceXMI object be instantiated at all?
		"""
		src = ODMSourceXMI()
		self.assertFalse( src is None, "Could not create ODMSourceXMI object")


	def test_loafProfile(self):
		"""
		Can a UML profile stored in a XMI file be loaded?
		"""
		src = ODMSourceXMI()
		profile = src.loadProfile( test_ODMSourceXMI.profilePath )
		self.assertFalse( profile is None, "Could not parse XMI file %s" % test_ODMSourceXMI.profilePath )
		# check that tree contains XMI
		root = profile.getroot()
		self.assertEqual( root.tag, "XMI", "Root element is not XMI")
		self.assertEqual( root.nsmap['UML'], 'org.omg.xmi.namespace.UML', "Namespace is not XMI" ) 


	def test_loadModel(self):
		"""
		Can a UML model stored in a XMI file be loaded?
		"""
		src = ODMSourceXMI()
		profile = src.loadProfile( test_ODMSourceXMI.profilePath )
		model = src.loadModel( test_ODMSourceXMI.testModelPath, profile )
		self.assertFalse( model is None, "Could not parse XMI file %s" % test_ODMSourceXMI.testModelPath )
		

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()