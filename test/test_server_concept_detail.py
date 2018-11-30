# coding: utf-8

"""
    Translator Knowledge Beacon Aggregator API

    This is the Translator Knowledge Beacon Aggregator web service application programming interface (API) that provides integrated access to a pool of knowledge sources publishing concepts and relations through the Translator Knowledge Beacon API. This API is similar to that of the latter mentioned API with the addition of some extra informative endpoints plus session identifier and beacon indices. These latter identifiers are locally assigned numeric indices provided to track the use of specific registered beacons within the aggregator API itself.   # noqa: E501

    OpenAPI spec version: 1.1.3
    Contact: richard@starinformatics.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import kba
from kba.models.server_concept_detail import ServerConceptDetail  # noqa: E501
from kba.rest import ApiException


class TestServerConceptDetail(unittest.TestCase):
    """ServerConceptDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testServerConceptDetail(self):
        """Test ServerConceptDetail"""
        # FIXME: construct object with mandatory attributes with example values
        # model = kba.models.server_concept_detail.ServerConceptDetail()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
