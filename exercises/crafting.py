#!/usr/bin/python
commands = {
              "i"            : "see inventory",
              "c"            : "see crafting options",
              "craft [item]" : "craft something from inventory items"
           }
# inventory of items
items = {
            "flint"   : 50,
            
            "grass"   : 100,
            "hay"     : 0,

            "tree"    : 100,
            "log"     : 0,

            "sapling" : 100,
            "twig"    : 0,

            "boulder" : 30,
            "rock"    : 0,

            "pickaxe" : 0,
            "axe"     : 0,

            "firepit" : 0,
            "tent"    : 0,

            "torch"   : 0
        }

# Rules to make new objects
crafts = {
            "hay"     : {"grass"   : 1},
            "twig"    : {"sapling" : 1},
            "log"     : {"axe"     : 1,  "true"  : 1},
            "axe"     : {"twig"    : 1,  "flint" : 1},
            "tent"    : {"twig"    : 10, "hay"   : 15},
            "firepit" : {"boulder" : 5,  "log"   : 3,  "twig" : 1,  "torch" : 1},
            "torch"   : {"flint"   : 1,  "grass" : 1,  "twig" : 1},
            "pickaxe" : {"flint"   : 2,  "twig"  : 1}
         }

def displayCommands():
  for command in commands:
    print command + " : " + commands[command]

def displayInventory():
  for item in items:
    print item + " : " + str(items[item])

def displayCraftOptions():
  for craft in crafts:
    print craft + " can be made with: "
    for item in crafts[craft]:
      print str(crafts[craft][item]) + " " + item
    print

def makeCraft(item):
  print "making " + item + ":"
  item_made = True

  for i in crafts[item]:
    if items[i] < crafts[item][i]:
      item_made = False

  for i in crafts[item]:
    print "   you need: " + str(crafts[item][i]) + " " + i + " and you have " + str(items[i])

  if item_made:
    for i in crafts[item]:
      items[i] -= crafts[item][i]
    print "item crafted"
  else:
    print "item cannot be crafted"

def parseCommands(verb, item):
  if verb == "?" or verb == "help":
    displayCommands()
  elif verb == "i":
    displayInventory()
  elif verb == "c":
    displayCraftOptions()
  elif verb == "craft" and item != "":
    makeCraft(item)

def main():
  verb = ""
  item = ""
  while True:
    command = raw_input("> ").split()

    if len(command) == 0:
      continue
    if len(command) > 0:
      verb = command[0].lower()
    if len(command) > 1:
      item = command[1].lower()
    if verb == "exit":
      break
    parseCommands(verb, item)

if __name__ == "__main__":
  main()
