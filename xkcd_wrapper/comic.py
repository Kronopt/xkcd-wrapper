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
    image : bytes or None
        raw comic image
    image_extension : str or None
        comic image extension (ex: .png, .jpeg)
    image_url : str or None
        comic image url
    comic_url : str or None
        comic url
    explanation_url : str or None
        url to explainxkcd wiki
    """

    def __init__(self, xkcd_dict, raw_image=None, comic_url=None, explanation_url=None):
        """
        Comic init

        Parameters
        ----------
        xkcd_dict : dict
            parsed json obtained from xkcd API (all fields are assumed to be the correct type)
        raw_image : bytes or None
            raw comic image
        comic_url : str or None
            comic url
        explanation_url : str or None
            url to explainxkcd wiki
        """
        self.id = xkcd_dict.get('num')
        self.title = xkcd_dict.get('safe_title')
        self.description = xkcd_dict.get('alt')
        self.transcript = xkcd_dict.get('transcript')
        self.image = raw_image
        self.image_url = xkcd_dict.get('img')
        self.comic_url = comic_url
        self.explanation_url = explanation_url

        day = xkcd_dict.get('day')
        month = xkcd_dict.get('month')
        year = xkcd_dict.get('year')
        self.date = datetime.date(year, month, day) if all([year, month, day]) else None

        self.image_extension = self.image_url.rsplit('.', maxsplit=1)[1] if self.image_url else None

    def __repr__(self):
        return 'xkcd_wrapper.Comic({})'.format(self.id)
