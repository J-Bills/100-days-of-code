# This is a sample Python script.
from turtle import Turtle, Screen

# turtle1 = Turtle()
# turtle1.shape('turtle')
# turtle1.color('pink')
# turtle1.forward(100)
#
#
# window = Screen()
# window.setup(width=600, height=600)
#
#
# window.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pickachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = 'l'

print(table)









