from .audition import Audition

class Actor:
    
    
    all = []

    def __init__(self, name):
        self.name = name
        Actor.all.append(self)

    def actor_auditions(self):
        return [a for a in Audition.all if a.actor_i == self]
    
    def actor_roles(self):
        return [a.role_i for a in Audition.all if a.actor_i == self]
    
    def actor_characters(self):
        return [a.character_name for a in self.actor_roles()]
    
    def actor_paychecks(self):
        return [a.role_i.character_name for a in self.actor_auditions() if a.hired == True]
    

