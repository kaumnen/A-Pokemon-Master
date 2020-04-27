class Pokemon:
  def __init__(self, name, level, typ, is_knocked_out):
    self.name = name
    self.level = level
    self.typ = typ
    self.is_knocked_out = is_knocked_out
    self.exp = 0
    self.max_health = level
    self.health = self.max_health
  
  def __repr__(self):
    return "Pokemon info. {}, current level: {}, typ: {}, maximum health: {}, current health: {}.\n".format(self.name, self.level, self.typ, self.max_health, self.health)
  
  def lose_health(self, dmg):
    self.health -= dmg
    if self.health <= 0:
      self.health = 0
      self.knock_out()
  
  def gain_health(self, heal):
    self.health += heal
    print("{} gained {} health".format(self.name, heal))
    print("{}'s health: {}".format(self.name, self.health))
  
  def knock_out(self):
    if self.is_knocked_out:
      print("{name} is already knocked out.".format(name = self.name))
    else:
      self.is_knocked_out = True
      print("{name} is knocked out!".format(name = self.name))
  
  def revive(self):
    if self.is_knocked_out:
      self.is_knocked_out = False
      self.health = 1
      print("{name} has been revived with {health} health!".format(name = self.name, health = self.health))
    else:
      print("{name} is not knocked out.".format(name = self.name))
  
  def attack(self, other, dmg):
    if self.is_knocked_out == True:
      print("You can not attack. {pokemon} is knocked out!".format(pokemon = self.name))
      return
    if self.typ == 'Water':
      if other.typ == 'Fire':
        dmg *= 2
      elif other.typ == 'Grass':
        dmg /= 2
    elif self.typ == 'Fire':
      if other.typ == 'Grass':
        dmg *= 2
      elif other.typ == 'Water':
        dmg /= 2
    elif self.typ == 'Grass':
      if other.typ == 'Water':
        dmg *= 2
      elif other.typ == 'Fire':
        dmg /= 2
    other.lose_health(dmg)
    print("{} attacked {}".format(self.name, other.name))
    print("{} dealt {} damage to {}. His health is {}.".format(self.name, dmg, other.name, other.health))
    self.gain_exp(1)
  
  def gain_exp(self, exp):
    self.exp += exp
    print("{} gained {} xp.\n".format(self.name, exp))
    if self.exp >= 3:
      self.level_up()
  
  def level_up(self):
    self.exp = 0
    self.level += 1
    self.max_health += 1
    self.health = self.max_health
    print("{} leveled up to {} level! Max health now is {}. Health fully regenerated.\n".format(self.name, self.level, self.max_health))
 

class Charmander(Pokemon):
  def __init__(self, name, level, typ, is_knocked_out):
    super().__init__(name, level, typ, is_knocked_out)
  
  def destroy(self, other):
    other.lose_health(other.health)
    print("{} totally destroyed {}!".format(self.name, other.name))


# Testing
pikachu = Pokemon("Pikachu", 3, "Fire", False)
bulbasaur = Pokemon("Bulbasaur", 3, "Grass", False)
squirtle = Pokemon("Squirtle", 3, "Water", False)
charmander = Charmander("Charmander", 3, "Fire", False)

print(pikachu)
print(bulbasaur)

pikachu.lose_health(1)
pikachu.gain_health(1)
pikachu.gain_exp(3)
