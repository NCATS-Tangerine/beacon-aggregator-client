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


class ServerClique(object):
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
        'clique_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'clique_id': 'cliqueId'
    }

    def __init__(self, id=None, clique_id=None):  # noqa: E501
        """ServerClique - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._clique_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if clique_id is not None:
            self.clique_id = clique_id

    @property
    def id(self):
        """Gets the id of this ServerClique.  # noqa: E501

        CURIE identifying the concept whose concept clique is being resolved   # noqa: E501

        :return: The id of this ServerClique.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ServerClique.

        CURIE identifying the concept whose concept clique is being resolved   # noqa: E501

        :param id: The id of this ServerClique.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def clique_id(self):
        """Gets the clique_id of this ServerClique.  # noqa: E501

        CURIE identifying the equivalent concept clique to which the  input concept CURIE belongs.   # noqa: E501

        :return: The clique_id of this ServerClique.  # noqa: E501
        :rtype: str
        """
        return self._clique_id

    @clique_id.setter
    def clique_id(self, clique_id):
        """Sets the clique_id of this ServerClique.

        CURIE identifying the equivalent concept clique to which the  input concept CURIE belongs.   # noqa: E501

        :param clique_id: The clique_id of this ServerClique.  # noqa: E501
        :type: str
        """

        self._clique_id = clique_id

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
        if not isinstance(other, ServerClique):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
