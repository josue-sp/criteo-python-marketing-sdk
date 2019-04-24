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


class CreateSellerBudgetMapiMessage(object):
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
        'amount': 'str',
        'start_date': 'datetime',
        'end_date': 'str',
        'seller_id': 'int',
        'campaign_ids': 'list[int]',
        'budget_type': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'seller_id': 'sellerId',
        'campaign_ids': 'campaignIds',
        'budget_type': 'budgetType'
    }

    def __init__(self, amount=None, start_date=None, end_date=None, seller_id=None, campaign_ids=None, budget_type=None):  # noqa: E501
        """CreateSellerBudgetMapiMessage - a model defined in OpenAPI"""  # noqa: E501

        self._amount = None
        self._start_date = None
        self._end_date = None
        self._seller_id = None
        self._campaign_ids = None
        self._budget_type = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if seller_id is not None:
            self.seller_id = seller_id
        if campaign_ids is not None:
            self.campaign_ids = campaign_ids
        if budget_type is not None:
            self.budget_type = budget_type

    @property
    def amount(self):
        """Gets the amount of this CreateSellerBudgetMapiMessage.  # noqa: E501


        :return: The amount of this CreateSellerBudgetMapiMessage.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CreateSellerBudgetMapiMessage.


        :param amount: The amount of this CreateSellerBudgetMapiMessage.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def start_date(self):
        """Gets the start_date of this CreateSellerBudgetMapiMessage.  # noqa: E501


        :return: The start_date of this CreateSellerBudgetMapiMessage.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this CreateSellerBudgetMapiMessage.


        :param start_date: The start_date of this CreateSellerBudgetMapiMessage.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this CreateSellerBudgetMapiMessage.  # noqa: E501


        :return: The end_date of this CreateSellerBudgetMapiMessage.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this CreateSellerBudgetMapiMessage.


        :param end_date: The end_date of this CreateSellerBudgetMapiMessage.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def seller_id(self):
        """Gets the seller_id of this CreateSellerBudgetMapiMessage.  # noqa: E501


        :return: The seller_id of this CreateSellerBudgetMapiMessage.  # noqa: E501
        :rtype: int
        """
        return self._seller_id

    @seller_id.setter
    def seller_id(self, seller_id):
        """Sets the seller_id of this CreateSellerBudgetMapiMessage.


        :param seller_id: The seller_id of this CreateSellerBudgetMapiMessage.  # noqa: E501
        :type: int
        """

        self._seller_id = seller_id

    @property
    def campaign_ids(self):
        """Gets the campaign_ids of this CreateSellerBudgetMapiMessage.  # noqa: E501


        :return: The campaign_ids of this CreateSellerBudgetMapiMessage.  # noqa: E501
        :rtype: list[int]
        """
        return self._campaign_ids

    @campaign_ids.setter
    def campaign_ids(self, campaign_ids):
        """Sets the campaign_ids of this CreateSellerBudgetMapiMessage.


        :param campaign_ids: The campaign_ids of this CreateSellerBudgetMapiMessage.  # noqa: E501
        :type: list[int]
        """

        self._campaign_ids = campaign_ids

    @property
    def budget_type(self):
        """Gets the budget_type of this CreateSellerBudgetMapiMessage.  # noqa: E501


        :return: The budget_type of this CreateSellerBudgetMapiMessage.  # noqa: E501
        :rtype: str
        """
        return self._budget_type

    @budget_type.setter
    def budget_type(self, budget_type):
        """Sets the budget_type of this CreateSellerBudgetMapiMessage.


        :param budget_type: The budget_type of this CreateSellerBudgetMapiMessage.  # noqa: E501
        :type: str
        """

        self._budget_type = budget_type

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
        if not isinstance(other, CreateSellerBudgetMapiMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
