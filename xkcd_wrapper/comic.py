#!python
# coding: utf-8

"""
xkcd-wrapper Comic
"""

import datetime
import imghdr


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
        self.date = self._determine_date(xkcd_dict)
        self.title = xkcd_dict.get('safe_title')
        self.description = xkcd_dict.get('alt')
        self.transcript = xkcd_dict.get('transcript')
        self.image = raw_image
        self.image_extension = self._determine_image_extension()
        self.image_url = xkcd_dict.get('img')
        self.comic_url = comic_url
        self.explanation_url = explanation_url

    def update_raw_image(self, raw_image):
        """
        Updates raw_image and image_extension

        Parameters
        ----------
        raw_image : bytes or None
            raw comic image
        """
        self.image = raw_image
        self.image_extension = self._determine_image_extension()

    @staticmethod
    def _determine_date(xkcd_dict):
        """
        Determine date of xkcd comic

        Parameters
        ----------
        xkcd_dict : dict
            parsed json obtained from xkcd API (all fields are assumed to be the correct type)

        Returns
        -------
        datetime.date or None
            date when comic was released
        """
        day = xkcd_dict.get('day')
        month = xkcd_dict.get('month')
        year = xkcd_dict.get('year')
        return datetime.date(year, month, day) if all([year, month, day]) else None

    def _determine_image_extension(self):
        """
        Determine the extension of the xkcd comic image (ex: .png, .jpeg)

        Returns
        -------
        str or None
            image extension
        """
        return imghdr.what(None, self.image) if self.image else None

    def __repr__(self):
        return 'xkcd_wrapper.Comic({})'.format(self.id)
