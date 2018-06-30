# adding the import commands for the kanren the logic library
from kanren import run, eq, membero, var, conde, Relation, facts

# specify the relation we wish to build (its parent in our case)
Parent=Relation()

# adding facts given in Question 1 - Modelling the knowledge
facts (Parent, ('Leia Organa', 'Kylo Ren'),
               ('Darth Vader', 'Leia Organa'),
               ('Darth Vader', 'Luke Skywalker'),
               ('Han Solo',  'Kylo Ren'))


# running queires in Question 2

# define parent variable
parent_l_s = var()
print "Who is the parent of Luke Skywalker :"
print(run(0, parent_l_s, Parent(parent_l_s, 'Luke Skywalker')))

# define child variable
children_d_v=var()
print "Who are the children of Darth Vader :"
print(run(0, children_d_v, Parent('Darth Vader', children_d_v)))

# grandparent Relation
def Grandparent(grand_parent, child):
    parent = var()
    return conde((Parent(grand_parent, parent), Parent(parent, child)))

# get answer to part 3
parent = var()
grand_parent = var()
child = var()
print "Who is the grandparent of of Kylo Ren :"
print(run(0, parent,Parent(parent,grand_parent), Parent(grand_parent, 'Kylo Ren')))
print "Who is the grandparent of of Kylo Ren ( 2nd way of doing it ) :"
print(run(1, grand_parent, Grandparent(grand_parent, 'Kylo Ren')))
