#!/usr/bin/env python
import unittest
from shutil import copy2
from os import remove
from discodos.models import *
from discodos.utils import *
import inspect
from pprint import pprint


class TestBrainz(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        log.handlers[0].setLevel("INFO") # handler 0 is the console handler
        log.handlers[0].setLevel("DEBUG") # handler 0 is the console handler
        conf = Config() # doesn't get path of test-db, so...
        empty_db_path = conf.discodos_root / 'tests' / 'fixtures' / 'discobase_empty.db'
        self.db_path = conf.discodos_root / 'tests' / 'discobase.db'
        self.clname = self.__name__ # just handy a shortcut, used in test output
        self.mb_user = conf.musicbrainz_user
        self.mb_pass = conf.musicbrainz_password
        self.mb_appid = conf.discogs_appid
        print('TestBrainz.setUpClass: test-db: {}'.format(copy2(empty_db_path, self.db_path)))
        print("TestBrainz.setUpClass: done\n")

    def test_get_mb_artist_by_id(self):
        name = inspect.currentframe().f_code.co_name
        print("\n{} - {} - BEGIN".format(self.clname, name))
        self.brainz = Brainz(False, self.db_path)
        if self.brainz.musicbrainz_connect(self.mb_user, self.mb_pass,
                    self.mb_appid):
            print('We are ONLINE')
            mb_return = self.brainz.get_mb_artist_by_id('952a4205-023d-4235-897c-6fdb6f58dfaa')
            #print(dir(mb_return))
            #print(mb_return)
            self.assertEqual(len(mb_return), 1) # should be single release in a list!
            self.assertEqual(mb_return['artist']['name'], 'Dynamo Go')
            self.assertEqual(mb_return['artist']['country'], 'NZ')
        else:
            print('We are OFFLINE, testing if we properly fail!')
            mb_return = self.brainz.get_mb_artist_by_id('952a4205-023d-4235-897c-6fdb6f58dfaa')
            self.assertFalse(mb_return)
        print("{} - {} - END".format(self.clname, name))

    def test_search_mb_releases(self):
        name = inspect.currentframe().f_code.co_name
        print("\n{} - {} - BEGIN".format(self.clname, name))
        self.brainz = Brainz(False, self.db_path)
        if self.brainz.musicbrainz_connect(self.mb_user, self.mb_pass,
                    self.mb_appid):
            print('We are ONLINE')
            mb_return = self.brainz.search_mb_releases("Source Direct",
                "The Crane", "NONPLUS034")
            #print(dir(mb_return))
            #print(mb_return)
            #pprint(mb_return)
            self.assertEqual(len(mb_return), 2) # keys: release-list, release-count
            self.assertEqual(
                mb_return['release-list'][0]['artist-credit'][0]['artist']['name'],
                'Source Direct')
            self.assertEqual(
                mb_return['release-list'][0]['label-info-list'][0]['catalog-number'],
                'NONPLUS034')
            # we don't get url-rels with a release search
        else:
            print('We are OFFLINE, testing if we properly fail!')
            mb_return = self.brainz.search_mb_releases("Source Direct",
                "The Crane")
            self.assertFalse(mb_return)
        print("{} - {} - END".format(self.clname, name))

    def test_get_mb_release_by_id(self):
        name = inspect.currentframe().f_code.co_name
        print("\n{} - {} - BEGIN".format(self.clname, name))
        self.brainz = Brainz(False, self.db_path)
        if self.brainz.musicbrainz_connect(self.mb_user, self.mb_pass,
                    self.mb_appid):
            print('We are ONLINE')
            mb_return = self.brainz.get_mb_release_by_id(
                'c4b619f1-5ae2-45e5-b848-71290e97eb69')
            #print(dir(mb_return))
            #pprint(mb_return)
            #print(mb_return.items())
            self.assertEqual(len(mb_return), 1) # should be single release in a list!
            self.assertEqual(
                mb_return['release']['artist-credit'][0]['artist']['name'],
                'Source Direct')
            self.assertEqual(
                mb_return['release']['label-info-list'][0]['catalog-number'],
                'NONPLUS034')
            self.assertEqual(
                mb_return['release']['url-relation-list'][0]['type'], 'discogs')
            self.assertEqual(
                mb_return['release']['url-relation-list'][0]['type-id'],
                '4a78823c-1c53-4176-a5f3-58026c76f2bc')
            self.assertEqual(
                mb_return['release']['url-relation-list'][0]['target'],
                'https://www.discogs.com/release/8633263')
        else:
            print('We are OFFLINE, testing if we properly fail!')
            mb_return = self.brainz.get_mb_release_by_id(
                'c4b619f1-5ae2-45e5-b848-71290e97eb69')
            self.assertFalse(mb_return)
        print("{} - {} - END".format(self.clname, name))

    def test_get_mb_recording_by_id(self):
        name = inspect.currentframe().f_code.co_name
        print("\n{} - {} - BEGIN".format(self.clname, name))
        self.brainz = Brainz(False, self.db_path)
        if self.brainz.musicbrainz_connect(self.mb_user, self.mb_pass,
                    self.mb_appid):
            print('We are ONLINE')
            mb_return = self.brainz.get_mb_recording_by_id(
                'fa9b7b2d-e9bb-4122-a725-4f865dd4648a')
            #print(dir(mb_return))
            #pprint(mb_return)
            #print(mb_return.items())
            self.assertEqual(len(mb_return), 1) # should be single release in a list!
            self.assertEqual(mb_return['recording']['id'],
                'fa9b7b2d-e9bb-4122-a725-4f865dd4648a')
            self.assertEqual(mb_return['recording']['title'], 'The Crane')
            self.assertEqual(mb_return['recording']['length'], '401000')
        else:
            print('We are OFFLINE, testing if we properly fail!')
            mb_return = self.brainz.get_mb_recording_by_id(
                'fa9b7b2d-e9bb-4122-a725-4f865dd4648a')
            self.assertFalse(mb_return)
        print("{} - {} - END".format(self.clname, name))

    @classmethod
    def tearDownClass(self):
        os.remove(self.db_path)
        print("\nTestBrainz.teardownClass: done")

if __name__ == '__main__':
    loader = unittest.TestLoader()
    ln = lambda f: getattr(TestCollection, f).im_func.func_code.co_firstlineno
    lncmp = lambda _, a, b: cmp(ln(a), ln(b))
    loader.sortTestMethodsUsing = lncmp
    unittest.main(testLoader=loader, verbosity=2)