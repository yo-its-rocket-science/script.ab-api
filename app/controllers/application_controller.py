import flask
import six

from app.models.application import Application  # noqa: E501
from app.models.company import Company  # noqa: E501
from app import util


def application_post(body):  # noqa: E501
    """add appplication

     # noqa: E501

    :param body: Add application
    :type body: dict | bytes

    :rtype: None
    """
    if flask.request.is_json:
        body = Application.from_dict(flask.request.get_json())  # noqa: E501
    return 'do some magic!'


def deleteapplication(id):  # noqa: E501
    """Delete application

     # noqa: E501

    :param id: The application that needs to be deleted
    :type id: float

    :rtype: None
    """
    return 'do some magic!'


def getapplication_bycandidate_id(candidateid):  # noqa: E501
    """Get application by candidate id

     # noqa: E501

    :param candidateid: The candidate id that needs to be fetched.
    :type candidateid: float

    :rtype: Company
    """
    return 'do some magic!'
