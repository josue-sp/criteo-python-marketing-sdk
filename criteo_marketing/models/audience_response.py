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


class AudienceResponse(object):
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
        'id': 'int',
        'advertiser_id': 'int',
        'name': 'str',
        'description': 'str',
        'created': 'int',
        'updated': 'int',
        'nb_lines': 'int',
        'nb_lines_email': 'int',
        'nb_matches_email': 'int'
    }

    attribute_map = {
        'id': 'id',
        'advertiser_id': 'advertiserId',
        'name': 'name',
        'description': 'description',
        'created': 'created',
        'updated': 'updated',
        'nb_lines': 'nbLines',
        'nb_lines_email': 'nbLinesEmail',
        'nb_matches_email': 'nbMatchesEmail'
    }

    def __init__(self, id=None, advertiser_id=None, name=None, description=None, created=None, updated=None, nb_lines=None, nb_lines_email=None, nb_matches_email=None):  # noqa: E501
        """AudienceResponse - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._advertiser_id = None
        self._name = None
        self._description = None
        self._created = None
        self._updated = None
        self._nb_lines = None
        self._nb_lines_email = None
        self._nb_matches_email = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if advertiser_id is not None:
            self.advertiser_id = advertiser_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if nb_lines is not None:
            self.nb_lines = nb_lines
        if nb_lines_email is not None:
            self.nb_lines_email = nb_lines_email
        if nb_matches_email is not None:
            self.nb_matches_email = nb_matches_email

    @property
    def id(self):
        """Gets the id of this AudienceResponse.  # noqa: E501


        :return: The id of this AudienceResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AudienceResponse.


        :param id: The id of this AudienceResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def advertiser_id(self):
        """Gets the advertiser_id of this AudienceResponse.  # noqa: E501


        :return: The advertiser_id of this AudienceResponse.  # noqa: E501
        :rtype: int
        """
        return self._advertiser_id

    @advertiser_id.setter
    def advertiser_id(self, advertiser_id):
        """Sets the advertiser_id of this AudienceResponse.


        :param advertiser_id: The advertiser_id of this AudienceResponse.  # noqa: E501
        :type: int
        """

        self._advertiser_id = advertiser_id

    @property
    def name(self):
        """Gets the name of this AudienceResponse.  # noqa: E501


        :return: The name of this AudienceResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AudienceResponse.


        :param name: The name of this AudienceResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this AudienceResponse.  # noqa: E501


        :return: The description of this AudienceResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AudienceResponse.


        :param description: The description of this AudienceResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def created(self):
        """Gets the created of this AudienceResponse.  # noqa: E501

        Unix timestamp in seconds of audience creation  # noqa: E501

        :return: The created of this AudienceResponse.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this AudienceResponse.

        Unix timestamp in seconds of audience creation  # noqa: E501

        :param created: The created of this AudienceResponse.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this AudienceResponse.  # noqa: E501

        Unix timestamp in seconds of audience last update  # noqa: E501

        :return: The updated of this AudienceResponse.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this AudienceResponse.

        Unix timestamp in seconds of audience last update  # noqa: E501

        :param updated: The updated of this AudienceResponse.  # noqa: E501
        :type: int
        """

        self._updated = updated

    @property
    def nb_lines(self):
        """Gets the nb_lines of this AudienceResponse.  # noqa: E501

        The total number of line in the audience  # noqa: E501

        :return: The nb_lines of this AudienceResponse.  # noqa: E501
        :rtype: int
        """
        return self._nb_lines

    @nb_lines.setter
    def nb_lines(self, nb_lines):
        """Sets the nb_lines of this AudienceResponse.

        The total number of line in the audience  # noqa: E501

        :param nb_lines: The nb_lines of this AudienceResponse.  # noqa: E501
        :type: int
        """

        self._nb_lines = nb_lines

    @property
    def nb_lines_email(self):
        """Gets the nb_lines_email of this AudienceResponse.  # noqa: E501

        The number of email line in the audience  # noqa: E501

        :return: The nb_lines_email of this AudienceResponse.  # noqa: E501
        :rtype: int
        """
        return self._nb_lines_email

    @nb_lines_email.setter
    def nb_lines_email(self, nb_lines_email):
        """Sets the nb_lines_email of this AudienceResponse.

        The number of email line in the audience  # noqa: E501

        :param nb_lines_email: The nb_lines_email of this AudienceResponse.  # noqa: E501
        :type: int
        """

        self._nb_lines_email = nb_lines_email

    @property
    def nb_matches_email(self):
        """Gets the nb_matches_email of this AudienceResponse.  # noqa: E501

        The number of email matches in the audience  # noqa: E501

        :return: The nb_matches_email of this AudienceResponse.  # noqa: E501
        :rtype: int
        """
        return self._nb_matches_email

    @nb_matches_email.setter
    def nb_matches_email(self, nb_matches_email):
        """Sets the nb_matches_email of this AudienceResponse.

        The number of email matches in the audience  # noqa: E501

        :param nb_matches_email: The nb_matches_email of this AudienceResponse.  # noqa: E501
        :type: int
        """

        self._nb_matches_email = nb_matches_email

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
        if not isinstance(other, AudienceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
