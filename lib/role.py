from .audition import Audition

class Role:

    all = []

    def __init__(self, character_name):
        self.character_name = character_name
        Role.all.append(self)

    def role_auditions(self):
        return [a for a in Audition.all if a.role_i == self]
    
    def role_actors(self):
        return [a.actor_i.name for a in Audition.all if a.role_i == self]
    
    def role_locations(self):
        return [a.location for a in self.role_auditions()]
    
    def role_silver_screen(self):
        return [a.role_i.character_name for a in Audition.all if a.hired == True]
    
    ## unsure if it works but I need to be sure how how DB is structured first before I can debug
