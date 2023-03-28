
class Audition:
    
    all = []

    def __init__( self, location, hired, role_i, actor_i ):
        self.location = location
        self.hired = hired
        self.role_i = role_i
        self.actor_i = actor_i
        Audition.all.append(self)

    def audition_role(self):
        return [self.role_i]

    def audition_actor(self):
        return [self.actor_i]
    
    def audition_call_back(self):
        if self.hired is False:
            self.hired = True
        elif self.hired is True:
            print("You have already called and hired this actor.")