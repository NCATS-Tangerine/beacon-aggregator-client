# coding: utf-8

"""
    Translator Knowledge Beacon Aggregator API

    This is the Translator Knowledge Beacon Aggregator web service application programming interface (API) that provides integrated access to a pool of knowledge sources publishing concepts and relations through the Translator Knowledge Beacon API. This API is similar to that of the latter mentioned API with the addition of some extra informative endpoints plus session identifier and beacon indices. These latter identifiers are locally assigned numeric indices provided to track the use of specific registered beacons within the aggregator API itself.   # noqa: E501

    OpenAPI spec version: 1.1.3
    Contact: richard@starinformatics.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ServerBeaconConceptCategory(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'uri': 'str',
        'category': 'str',
        'frequency': 'int'
    }

    attribute_map = {
        'id': 'id',
        'uri': 'uri',
        'category': 'category',
        'frequency': 'frequency'
    }

    def __init__(self, id=None, uri=None, category=None, frequency=None):  # noqa: E501
        """ServerBeaconConceptCategory - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._uri = None
        self._category = None
        self._frequency = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if uri is not None:
            self.uri = uri
        if category is not None:
            self.category = category
        if frequency is not None:
            self.frequency = frequency

    @property
    def id(self):
        """Gets the id of this ServerBeaconConceptCategory.  # noqa: E501

        the 'local' CURIE-encoded identifier of the given concept category, as published by the given beacon   # noqa: E501

        :return: The id of this ServerBeaconConceptCategory.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ServerBeaconConceptCategory.

        the 'local' CURIE-encoded identifier of the given concept category, as published by the given beacon   # noqa: E501

        :param id: The id of this ServerBeaconConceptCategory.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def uri(self):
        """Gets the uri of this ServerBeaconConceptCategory.  # noqa: E501

        the 'local' URI of the given concept category, as published by the given beacon   # noqa: E501

        :return: The uri of this ServerBeaconConceptCategory.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ServerBeaconConceptCategory.

        the 'local' URI of the given concept category, as published by the given beacon   # noqa: E501

        :param uri: The uri of this ServerBeaconConceptCategory.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def category(self):
        """Gets the category of this ServerBeaconConceptCategory.  # noqa: E501

        the 'local' human readable label of the given concept category, as published by the given beacon   # noqa: E501

        :return: The category of this ServerBeaconConceptCategory.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ServerBeaconConceptCategory.

        the 'local' human readable label of the given concept category, as published by the given beacon   # noqa: E501

        :param category: The category of this ServerBeaconConceptCategory.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def frequency(self):
        """Gets the frequency of this ServerBeaconConceptCategory.  # noqa: E501

        the number of instances of the specified concept category is used in statements within the given beacon   # noqa: E501

        :return: The frequency of this ServerBeaconConceptCategory.  # noqa: E501
        :rtype: int
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this ServerBeaconConceptCategory.

        the number of instances of the specified concept category is used in statements within the given beacon   # noqa: E501

        :param frequency: The frequency of this ServerBeaconConceptCategory.  # noqa: E501
        :type: int
        """

        self._frequency = frequency

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ServerBeaconConceptCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
