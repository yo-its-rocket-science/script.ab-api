from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app.models.skill import Skill  # noqa: F401,E501
from app import util


class Candidate(Model):
    def __init__(self, id: int = None, userid: int = None, skills: List[Skill] = None):  # noqa: E501
        """Candidate - a model defined in Swagger

        :param id: The id of this Candidate.  # noqa: E501
        :type id: int
        :param userid: The userid of this Candidate.  # noqa: E501
        :type userid: int
        :param skills: The skills of this Candidate.  # noqa: E501
        :type skills: List[Skill]
        """
        self.swagger_types = {
            'id': int,
            'userid': int,
            'skills': List[Skill]
        }

        self.attribute_map = {
            'id': 'id',
            'userid': 'userid',
            'skills': 'skills'
        }
        self._id = id
        self._userid = userid
        self._skills = skills

    @classmethod
    def from_dict(cls, dikt) -> 'Candidate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Candidate of this Candidate.  # noqa: E501
        :rtype: Candidate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Candidate.


        :return: The id of this Candidate.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Candidate.


        :param id: The id of this Candidate.
        :type id: int
        """

        self._id = id

    @property
    def userid(self) -> int:
        """Gets the userid of this Candidate.


        :return: The userid of this Candidate.
        :rtype: int
        """
        return self._userid

    @userid.setter
    def userid(self, userid: int):
        """Sets the userid of this Candidate.


        :param userid: The userid of this Candidate.
        :type userid: int
        """

        self._userid = userid

    @property
    def skills(self) -> List[Skill]:
        """Gets the skills of this Candidate.


        :return: The skills of this Candidate.
        :rtype: List[Skill]
        """
        return self._skills

    @skills.setter
    def skills(self, skills: List[Skill]):
        """Sets the skills of this Candidate.


        :param skills: The skills of this Candidate.
        :type skills: List[Skill]
        """

        self._skills = skills
