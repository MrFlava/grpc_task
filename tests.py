import unittest
import uuid
from unittest.mock import MagicMock

from task_server import SimilaritySearchServiceServicer

class TestSimilaritySearch(unittest.TestCase):
    def setUp(self):
        self.search_service = SimilaritySearchServiceServicer()

    def test_addItem(self):
        item_id = str(uuid.uuid4())
        item_description = "test item description"

        self.search_service.AddItem = MagicMock(return_value={"status": 200, "message": "OK"})

        self.search_service.AddItem(item_id, item_description)
        self.search_service.AddItem.assert_called_with(item_id, item_description)

    def test_addItem_bad_request(self):
        item_id = str(uuid.uuid4())
        item_description = 312321

        self.search_service.AddItem  = MagicMock(return_value={"status": 400, "message": "Bad Request"})

        self.assertEqual(
            {"status": 400, "message": "Bad Request"},
            self.search_service.AddItem(item_id, item_description)
        )

    def test_searchItem(self):
        item_description = "test item"
        found_item = {"search_id": str(uuid.uuid4())}
        self.search_service.SearchItem = MagicMock(return_value=found_item)

        self.assertEqual(
            found_item,
            self.search_service.SearchItem(item_description)
        )

    def test_searchItem_bad_request(self):
        pass

if __name__ == '__main__':
    unittest.main()