# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants

def vars_for_all_templates(self):

    return {'total_q': 1,
            'total_rounds': Constants.num_rounds,
            'round_number': self.subsession.round_number,
            'role': self.player.role()}


class Welcome(Page):
    pass


class Question(Page):

    form_model = models.Player
    form_fields = [
        "gender", "age", "ethnicity", "education_level", "marital_status",
        "employment_status", "student_status", "enrolled_type", "auction_buy",
        "auctions_experience"]


class Gamble(Page):
    form_model = models.Player
    form_fields = ["gamble"]


page_sequence = [Welcome, Question, Gamble]
