""" Control Panel Interfaces

   >>> portal = layer['portal']
   >>> sandbox = portal['sandbox']

"""
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from zope.interface import Interface
from zope import schema
from plone.autoform import directives as aform
from eea.similarity.config import EEAMessageFactory as _
from decimal import Decimal


class IEEASimilaritySettings(Interface):
    """ Settings

        >>> from eea.similarity.interfaces import IEEASimilaritySettings
        >>> IEEASimilaritySettings(portal).portalTypes
        [u'Document']

    """
    aform.widget('portalTypes', CheckBoxFieldWidget)
    portalTypes = schema.List(
        title=_(u"Enable similarity suggestions"),
        description=_(u"Suggestions for similar items are enabled for the "
                      u"following content-types"),
        required=False,
        default=[u"Document"],
        value_type=schema.Choice(
            vocabulary=u"plone.app.vocabularies.ReallyUserFriendlyTypes")
    )

    equivalent_content_types = schema.List(
        title=_(u"Equivalent content types"),
        description=_(
            u"Please enter sets of equivalent content types, separated by"
            u" commas (each line a different set)"
        ),
        value_type=schema.TextLine(),
        required=True,
    )

    number_of_suggestions = schema.Int(
        title=_(u"Max. number of suggestions"),
        description=_(
            u"Specify the maximum number of suggestions"
        ),
        required=True,
    )

    max_difference = schema.TextLine(
        title=_(u"Max. score difference between suggestions"),
        description=_(
            u"Specify the maximum similarity score difference between "
            u"displayed suggestions (set to 1 to disable):"
        ),
        required=True,
    )

    remove_stopwords = schema.Bool(
        title=_(u"Remove stopwords"),
        description=_(
            u"Should stopwords be removed from the titles before search?"
            u" (a change here will only have effects after an index rebuild)"
        ),
    )

    refresh_frequency = schema.Int(
        title=_(u"TF-IDF index refresh frequency"),
        description=_(
            u"Specify the interval (in hours) at which the TF-IDF index should "
            u"be rebuilt."
        ),
        default=24,
        required=True,
    )

    dialog_title = schema.TextLine(
        title=_(u"Dialog title"),
        description=_(
            u"Customise the title of the dialog window"
        ),
        required=False,
    )

    dialog_text = schema.Text(
        title=_(u"Dialog text"),
        description=_(
            u"Customise the text of the dialog window"
        ),
        required=False,
    )

    threshold1 = schema.TextLine(
        title=_(u"Similarity threshold for 3-4 words titles"),
        description=_(
            u"Define the similarity score threshold for 3-4 words titles."
        ),
        required=True,
    )

    threshold2 = schema.TextLine(
        title=_(u"Similarity threshold for titles with more than 4 words"),
        description=_(
            u"Define the similarity score threshold for titles with "
            u"more than 4 words."
        ),
        required=True,
    )
