# -*- coding: UTF-8 -*-
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from plone.dexterity.browser.view import DefaultView
from plone.app.event.dx.behaviors import IEventBasic


class DemoView(BrowserView):
    """ This does nothing so far
    """


class TalkView(DefaultView):
    """ The default view for talks
    """

    def talk_date(self):
        wrapped = IEventBasic(self.context)
        return ''


class TalkListView(BrowserView):
    """ A list of talks
    """

    def talks(self):
        results = []
        portal_catalog = getToolByName(self.context, 'portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())

        brains = portal_catalog(portal_type="talk",
                                path=current_path)
        for brain in brains:
            results.append({
                'title': brain.Title,
                'description': brain.Description,
                'url': brain.getURL(),
                'audience': ', '.join(brain.audience),
                'type_of_talk': brain.type_of_talk,
                'speaker': brain.speaker,
                'uuid': brain.UID,
                })
        return results
