import pytest
from unittest.mock import Mock, patch

from apiquery import APIQuery

# test can set base base_url
def test_can_create_apiquery():
    test_url = 'https://www.example.com/'
    new_apiquery = APIQuery(test_url)
    assert new_apiquery.base_url == test_url
