from Entities.entity import Entity


class Structure(Entity):
    """Object model for structures."""

    def __init__(self, entity_id, powered = None, health = 100, task = None):
        super(Structure, self).__init__(entity_id)
        self.destroyed = False
        self.health = health
        self.powered = powered
        self.task = task

    def update(self):
        super(Structure, self).update()
        if self.health > 0:
            self.alive = False

        self.work()
        self.check_progress()

    def tick(self):
        super(Structure, self).tick()

    def damage(self, dmg):
        self.health -= dmg
        if self.health <= 0:
            self.destroyed = True

    def repair(self, dmg):
        self.health += dmg
        if self.health >= 100:
            self.health = 100

    def work(self, work):
        self.task.perform_task(work)

    def check_progress(self):
        if self.task.check_progress():
            output = self.task.return_output()
            self.task = None
            return output
        else:
            return None

    def needs_power(self):
        if self.powered is None:
            return False
        else:
            return True