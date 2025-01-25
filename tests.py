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
        bad_req_reply = {"status": 400, "message": "Bad Request"}

        self.search_service.AddItem  = MagicMock(return_value=bad_req_reply)

        self.assertEqual(
            bad_req_reply,
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
        item_description = 2343243
        search_id_reply = {"search_id": "Not Found"}
        self.search_service.SearchItem = MagicMock(return_value=search_id_reply)

        self.assertEqual(
            search_id_reply,
            self.search_service.SearchItem(item_description)
        )

    def test_getSearchResults(self):
        search_items_id = str(uuid.uuid4())
        search_results_reply = [
            {"itemID": search_items_id, "description": "test item description"},
            {"itemID": search_items_id, "description": "test item description1"},
            {"itemID": search_items_id, "description": "test item description2"},
            {"itemID": search_items_id, "description": "test item description3"},
        ]

        self.search_service.GetSearchResults = MagicMock(return_value=search_results_reply)

        self.assertEqual(
            search_results_reply,
            self.search_service.GetSearchResults(search_items_id)
        )

    def test_getSearchResults_not_found(self):
        search_items_id = str(uuid.uuid4())
        search_results_reply = [
            {"itemID": "-", "description": "-"},
        ]

        self.search_service.GetSearchResults = MagicMock(return_value=search_results_reply)

        self.assertEqual(
            search_results_reply,
            self.search_service.GetSearchResults(search_items_id)
        )


if __name__ == '__main__':
    unittest.main()