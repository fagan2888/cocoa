from cocoa.systems.rulebased_system import RulebasedSystem as BaseRulebasedSystem
from sessions.rulebased_session import RulebasedSession

class RulebasedSystem(BaseRulebasedSystem):

    def __init__(self, lexicon, templates, timed_session=False):
        super(RulebasedSystem, self).__init__(timed_session)
        self.lexicon = lexicon
        self.templates = templates

    def _new_session(self, agent, kb, config=None):
        return RulebasedSession(agent, kb, self.lexicon, config, self.templates)