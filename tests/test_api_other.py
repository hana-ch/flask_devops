import json
import unittest

from tests.base import MyTestCase

class APIOtherTestCase(MyTestCase):

    def test_01_get_others(self):
        with self.app.test_request_context('/others/', method='GET', headers={}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 200, res)
            json_response = json.loads(res.data.decode('utf8'))
            for obj in json_response:
                self.assertTrue(obj.get("name"), res)
                self.assertTrue(obj.get("description"),res)


    def test_02_post_others(self):
        with self.app.test_request_context('/others/',
                                           #data={"name": "test",
                                            #     "description" : "test desc"
                                            #     },
                                           json=dict(name='test',description='test'),
                                           method='POST',
                                           headers={"Content-type":"application/json"}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 201, res)
            res = json.loads(res.data.decode('utf8'))
            self.assertTrue(res.get("name"), res)
            self.assertTrue(res.get("description"), res)


if __name__ == '__main__':
    unittest.main()
