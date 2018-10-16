import json

class God_attributes(object):

  def __init__ (self, name, siege = 0, initiation = 0, crowd_control = 0, wave_clear = 0, objective_damage = 0):
    self.name = name
    self.siege = siege
    self.initiation = initiation
    self.crowd_control = crowd_control
    self.wave_clear = wave_clear
    self.objective_damage = objective_damage

    self.attributes = {
     "name" : name,
     "siege" : siege,
     "initiation" : initiation,
     "crowd_control" : crowd_control,
     "wave_clear" : wave_clear,
     "objective_damage" : objective_damage}

  def __repr__(self):
    return str(self.attributes)

  def toJSON(self):
      return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

  def get_name(self):
      return self.name

  def get_siege(self):
      return self.siege

  def get_initiation(self):
      return self.initiation

  def get_crowd_control(self):
      return self.crowd_control

  def get_wave_clear(self):
      return self.wave_clear

  def get_objective_damage(self):
      return self.objective_damage





# 0-5 scale
# siege: 0: doesnt contribute anything
#       +1: has 1 ability that contributes to siege
#       +1: self heal ability
#       +2: team heal ability
#       +2: character can frontline
#       +2: long range ability
#       +2: high damage ranged auto attacks
#       +1: high damage melee auto attacks
# initiation 0: does not have any ability that can initiate
#       +2: has an ability that is useful for initiating (hard cc)
#       +1: has blink
#       +1: has a movement ability that can help close the game and initiate
# crowd control 0: does not have a slow, stun, etc
#       +2: has a single target ability that can hard cc
#       +3: has a multi target hard cc
#       +1: has a soft cc single target
#       +1: has a soft cc multi target
# wave clear 0: cannot clear
#       +1: physical auto attacks
#       +1: has an ability that helps clear a little
#       +2: has an ability that clears a lot
# objective damage:
#       +2: physical auto attacks
#       +1: high damage ability
#       +2: damaging secure ability
#       +1: high damage kit
