import unittest
import uuid
from unittest.mock import MagicMock

from task_server import SimilaritySearchServiceServicer

class TestSimilaritySearch(unittest.TestCase):
    def setUp(self):
        self.search_service = SimilaritySearchServiceServicer()
        self.search_service.AddItem = MagicMock(return_value={"status": 200, "message": "OK"})


    def test_addItem(self):
        item_id = str(uuid.uuid4())
        item_description = "test item description"

        self.search_service.AddItem(item_id, item_description)
        self.search_service.AddItem.assert_called_with(item_id, item_description)


if __name__ == '__main__':
    unittest.main()