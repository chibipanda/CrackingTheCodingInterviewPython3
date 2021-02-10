import time
import unittest
from datetime import datetime


class KV:
    def __init__(self):
        self.storage = {}

    def set(self, key, value):
        current_timestamp = datetime.now()
        if key not in self.storage:
            self.storage[key] = []
        self.storage[key].append((current_timestamp, value))
        return current_timestamp

    # [1,2,3,4,5,6,7] search for 2.5
    def search_for_timestamp(self, list_of_tuples, timestamp_to_search_for):
        number_of_tuples = len(list_of_tuples)
        if number_of_tuples <= 0:
            return None
        if number_of_tuples == 1:
            timest, val = list_of_tuples[0]
            if timest <= timestamp_to_search_for:
                return val
            else:
                return None
        median_timestamp, median_value = list_of_tuples[number_of_tuples // 2]
        if timestamp_to_search_for < median_timestamp:
            return self.search_for_timestamp(list_of_tuples[: number_of_tuples // 2], timestamp_to_search_for)
        elif timestamp_to_search_for == median_timestamp:
            return median_value
        else:
            return self.search_for_timestamp(list_of_tuples[(number_of_tuples // 2):], timestamp_to_search_for)

    def get(self, key, timestamp=None):
        if key in self.storage:
            if timestamp is None:
                time, val = self.storage[key][-1]
                return val
            else:
                all_values_for_key = self.storage[key]
                return self.search_for_timestamp(list(all_values_for_key), timestamp)
        else:
            return None


class KVTest(unittest.TestCase):
    def testKV(self):
        keyValueStorage = KV()
        timest = keyValueStorage.set('1', '123')
        keyValueStorage.set('1', '222')
        keyValueStorage.set('1', '223')
        timest4 = keyValueStorage.set('1', '224')
        time.sleep(1)
        timest_in_the_middle = datetime.now()
        keyValueStorage.set('1', '225')
        keyValueStorage.set('2', '234')
        self.assertEqual(keyValueStorage.get('1'), '225')
        self.assertEqual(keyValueStorage.get('1', timest), '123')
        self.assertEqual(keyValueStorage.get('1', timest_in_the_middle), '224')
        self.assertEqual(keyValueStorage.get('2', timest), None)
        self.assertEqual(keyValueStorage.get('2'), '234')
        self.assertEqual(keyValueStorage.get('3'), None)


if __name__ == '__main__':
    unittest.main()