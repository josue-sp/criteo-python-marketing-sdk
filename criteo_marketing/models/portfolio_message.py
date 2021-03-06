# coding: utf-8

"""
    Marketing API v.1.0

    IMPORTANT: This swagger links to Criteo production environment. Any test applied here will thus impact real campaigns.  # noqa: E501

    OpenAPI spec version: v.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PortfolioMessage(object):
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
        'advertiser_id': 'int',
        'advertiser_name': 'str'
    }

    attribute_map = {
        'advertiser_id': 'advertiserId',
        'advertiser_name': 'advertiserName'
    }

    def __init__(self, advertiser_id=None, advertiser_name=None):  # noqa: E501
        """PortfolioMessage - a model defined in OpenAPI"""  # noqa: E501

        self._advertiser_id = None
        self._advertiser_name = None
        self.discriminator = None

        if advertiser_id is not None:
            self.advertiser_id = advertiser_id
        if advertiser_name is not None:
            self.advertiser_name = advertiser_name

    @property
    def advertiser_id(self):
        """Gets the advertiser_id of this PortfolioMessage.  # noqa: E501


        :return: The advertiser_id of this PortfolioMessage.  # noqa: E501
        :rtype: int
        """
        return self._advertiser_id

    @advertiser_id.setter
    def advertiser_id(self, advertiser_id):
        """Sets the advertiser_id of this PortfolioMessage.


        :param advertiser_id: The advertiser_id of this PortfolioMessage.  # noqa: E501
        :type: int
        """

        self._advertiser_id = advertiser_id

    @property
    def advertiser_name(self):
        """Gets the advertiser_name of this PortfolioMessage.  # noqa: E501


        :return: The advertiser_name of this PortfolioMessage.  # noqa: E501
        :rtype: str
        """
        return self._advertiser_name

    @advertiser_name.setter
    def advertiser_name(self, advertiser_name):
        """Sets the advertiser_name of this PortfolioMessage.


        :param advertiser_name: The advertiser_name of this PortfolioMessage.  # noqa: E501
        :type: str
        """

        self._advertiser_name = advertiser_name

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
        if not isinstance(other, PortfolioMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
