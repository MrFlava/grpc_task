import uuid
import unittest

import mock

import task_client
from task_server import SimilaritySearchServiceServicer

class SimilaritySearchServiceTests(unittest.TestCase):

    def setUp(self):
        self.itemId = str(uuid.uuid4())
        self.description = "test-description"


    @mock('SimilaritySearchServiceServicer.AddItem')
    def test_add_item(self):
        pass