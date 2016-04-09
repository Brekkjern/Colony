class Entity(object):
    def __init__(self, entity_id):
        self.entity_id = entity_id
        self.alive = True

    def update(self):
        pass

    def tick(self):
        pass