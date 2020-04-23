#!python
# coding: utf-8

"""
xkcd-wrapper Comic
"""

import datetime


class Comic:
    """
    Comic represents a single xkcd comic
    All properties can be None if the value can't be retrieved from the xkcd API

    Attributes
    ----------
    id : int or None
        xkcd comic id
    date : datetime.date or None
        date when comic was released
    title : str or None
        comic title
    description : str or None
        comic description
    transcript : str or None
        comic transcript
    image : str or None
        image url
    link : str or None
        comic url
    explanation : str or None
        url to explainxkcd wiki
    """

    def __init__(self, xkcd_dict):
        """
        Comic init

        Parameters
        ----------
        xkcd_dict : dict
            parsed json obtained from xkcd API
        """
        self._comic = dict()
        self._comic['id'] = xkcd_dict['id']
        self._comic['title'] = xkcd_dict['title']
        self._comic['description'] = xkcd_dict['description']
        self._comic['transcript'] = xkcd_dict['transcript']
        self._comic['image'] = xkcd_dict['image']
        self._comic['link'] = xkcd_dict['link']
        self._comic['explanation'] = xkcd_dict['explanation']
        if all([xkcd_dict['year'], xkcd_dict['month'], xkcd_dict['day']]):
            self._comic['date'] = datetime.date(xkcd_dict['year'], xkcd_dict['month'], xkcd_dict['day'])
        else:
            self._comic['date'] = None

    @property
    def id(self):
        """id property"""
        return self._comic['id']

    @property
    def date(self):
        """date property"""
        return self._comic['date']

    @property
    def title(self):
        """title property"""
        return self._comic['title']

    @property
    def description(self):
        """description property"""
        return self._comic['description']

    @property
    def transcript(self):
        """transcript property"""
        return self._comic['transcript']

    @property
    def image(self):
        """image property"""
        return self._comic['image']

    @property
    def link(self):
        """link property"""
        return self._comic['link']

    @property
    def explanation(self):
        """explanation property"""
        return self._comic['explanation']

    def __repr__(self):
        return 'xkcd_wrapper.Comic({})'.format(self.id)
