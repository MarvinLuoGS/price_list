from otree.api import *


doc = """
A price list using otree. It can be used to elicit risk preference, time preference
"""


class C(BaseConstants):
    NAME_IN_URL = 'list'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # Parameters for time list
    TIME_ROW_NUM = 10 # num of rows
    TIME_AMOUNT = 10 # pay in short term e.g today 
    TIME_ACC = 1 # pay in the furture is incremented by 1
    TIME_STAMP1 = 'Today' # when to get the payment in short term
    TIME_STAMP2 = 'in Two Weeks' # when to get the payment in the furture
    # Parameters for risk list
    RISK_ROW_NUM = 10 # num of rows
    RISK_SURE_PAY = 0 # safe pay start from 0
    RISK_SURE_ACC = 2 # safe pay is incremented by 2
    RISK_HIGH_PAY = 30 # win lottery get 30
    RISK_LOW_PAY = 0 # lose lottery get 0
    RISK_PROB = 'Half the chance' # probability to win the lottery

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    time_switching_point = models.IntegerField() # switching point's value 
    time_consistency = models.BooleanField() # 1=only switch once,0=otherwise
    time_left_sum = models.IntegerField() # number or left options(option A)
    time_right_sum = models.IntegerField() # number of right options(option B)
    time_choice_list = models.StringField() # complete list of participants' choices, stored as a string
    #time_pay_order = models.IntegerField(initial=0) # the ith row is chose to calculate the payoff
    #time_pay_which = models.BooleanField(initial=False) # 0=left option chose, 1=right option chose in the ith row
    
    risk_switching_point = models.IntegerField() # switching point's value
    risk_consistency = models.BooleanField() # 1=only switch once,0=otherwise
    risk_left_sum = models.IntegerField() # number or left options(option A)
    risk_right_sum = models.IntegerField() # number of right options(option B)
    risk_choice_list = models.StringField() # complete list of participants' choices, stored as a string
    #risk_pay_order = models.IntegerField(initial=0) # the ith row is chose to calculate the payoff
    #risk_pay_which = models.BooleanField(initial=False) # 0=left option chose, 1=right option chose in the ith row
    #risk_pay_win = models.BooleanField(initial=False) # whether participants win the lottery
    
    # the choice_list field is easier to handle after changing it to a list
    # for example, list = [int(n) for n in choice_list.split(',')]
    # after changint it to a real list, it is more convenient to use it in calculating the payment and other situations
    # for example, use random to determine the row to be used as payoff: list[random.randint(0,C.TIME_ROW_NUM)]

# PAGES
class Time_list(Page):
    form_model = 'player'
    form_fields = ['time_switching_point','time_consistency','time_left_sum','time_right_sum','time_choice_list']

    @staticmethod
    def vars_for_template(player: Player):
        right_side_amounts = list(range(C.TIME_AMOUNT, C.TIME_AMOUNT+C.TIME_ROW_NUM*C.TIME_ACC+1, C.TIME_ACC))
        return dict(right_side_amounts=right_side_amounts)


class Risk_list(Page):
    form_model = 'player'
    form_fields = ['risk_switching_point','risk_consistency','risk_left_sum','risk_right_sum','risk_choice_list']

    @staticmethod
    def vars_for_template(player: Player):
        safe_side_amounts = list(range(C.RISK_SURE_PAY, C.RISK_SURE_PAY+C.RISK_ROW_NUM*C.RISK_SURE_ACC+1, C.RISK_SURE_ACC))
        return dict(safe_side_amounts=safe_side_amounts)


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Time_list,Risk_list]
