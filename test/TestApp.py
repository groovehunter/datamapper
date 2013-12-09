from TestBase import TestBase


class TestApp(TestBase):
    
    def testLoadConfig():
        
        self.assertTrue( self.dm.config )

