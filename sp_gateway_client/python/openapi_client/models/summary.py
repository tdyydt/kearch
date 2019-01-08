# coding: utf-8

"""
    Kearch specialist search engine gateway API

    Kearch specialist search engine gateway API  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Summary(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'sp_host': 'str',
        'engine_name': 'str',
        'dump': 'dict(str, int)'
    }

    attribute_map = {
        'sp_host': 'sp_host',
        'engine_name': 'engine_name',
        'dump': 'dump'
    }

    def __init__(self, sp_host=None, engine_name=None, dump=None):  # noqa: E501
        """Summary - a model defined in OpenAPI"""  # noqa: E501

        self._sp_host = None
        self._engine_name = None
        self._dump = None
        self.discriminator = None

        if sp_host is not None:
            self.sp_host = sp_host
        if engine_name is not None:
            self.engine_name = engine_name
        if dump is not None:
            self.dump = dump

    @property
    def sp_host(self):
        """Gets the sp_host of this Summary.  # noqa: E501


        :return: The sp_host of this Summary.  # noqa: E501
        :rtype: str
        """
        return self._sp_host

    @sp_host.setter
    def sp_host(self, sp_host):
        """Sets the sp_host of this Summary.


        :param sp_host: The sp_host of this Summary.  # noqa: E501
        :type: str
        """

        self._sp_host = sp_host

    @property
    def engine_name(self):
        """Gets the engine_name of this Summary.  # noqa: E501


        :return: The engine_name of this Summary.  # noqa: E501
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        """Sets the engine_name of this Summary.


        :param engine_name: The engine_name of this Summary.  # noqa: E501
        :type: str
        """

        self._engine_name = engine_name

    @property
    def dump(self):
        """Gets the dump of this Summary.  # noqa: E501


        :return: The dump of this Summary.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._dump

    @dump.setter
    def dump(self, dump):
        """Sets the dump of this Summary.


        :param dump: The dump of this Summary.  # noqa: E501
        :type: dict(str, int)
        """

        self._dump = dump

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, Summary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other