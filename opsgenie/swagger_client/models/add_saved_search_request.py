# coding: utf-8

"""
    OpsGenie REST API

    OpsGenie API Description

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat

from six import iteritems


class AddSavedSearchRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    def __init__(self, name=None, description=None, query=None, owner=None, teams=None):
        """
        AddSavedSearchRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'query': 'str',
            'owner': 'UserRecipient',
            'teams': 'list[TeamRecipient]'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'query': 'query',
            'owner': 'owner',
            'teams': 'teams'
        }

        self._name = name
        self._description = description
        self._query = query
        self._owner = owner
        self._teams = teams

    @property
    def name(self):
        """
        Gets the name of this AddSavedSearchRequest.

        :return: The name of this AddSavedSearchRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AddSavedSearchRequest.

        :param name: The name of this AddSavedSearchRequest.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this AddSavedSearchRequest.

        :return: The description of this AddSavedSearchRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AddSavedSearchRequest.

        :param description: The description of this AddSavedSearchRequest.
        :type: str
        """
        if description is not None and len(description) > 15000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `15000`")

        self._description = description

    @property
    def query(self):
        """
        Gets the query of this AddSavedSearchRequest.

        :return: The query of this AddSavedSearchRequest.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this AddSavedSearchRequest.

        :param query: The query of this AddSavedSearchRequest.
        :type: str
        """
        if query is None:
            raise ValueError("Invalid value for `query`, must not be `None`")
        if query is not None and len(query) > 1000:
            raise ValueError("Invalid value for `query`, length must be less than or equal to `1000`")

        self._query = query

    @property
    def owner(self):
        """
        Gets the owner of this AddSavedSearchRequest.

        :return: The owner of this AddSavedSearchRequest.
        :rtype: UserRecipient
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this AddSavedSearchRequest.

        :param owner: The owner of this AddSavedSearchRequest.
        :type: UserRecipient
        """
        if owner is None:
            raise ValueError("Invalid value for `owner`, must not be `None`")

        self._owner = owner

    @property
    def teams(self):
        """
        Gets the teams of this AddSavedSearchRequest.
        Teams that the alert will be routed to send notifications

        :return: The teams of this AddSavedSearchRequest.
        :rtype: list[TeamRecipient]
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """
        Sets the teams of this AddSavedSearchRequest.
        Teams that the alert will be routed to send notifications

        :param teams: The teams of this AddSavedSearchRequest.
        :type: list[TeamRecipient]
        """

        self._teams = teams

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, AddSavedSearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other