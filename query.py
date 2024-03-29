"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?
# <flask_sqlalchemy.BaseQuery at 0x7f1716bb4510>
# This is an flask sqlalchemy query object telling us the location in memory of this object.


# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?


#Association table is a middle table that has no meaningful fields and is the 
#glue between the two tables 

# One to one relationship does not have an association table middle table 
# because it is a direct relationship no constraints primary key and foreign key 
#are unique. They are pointing to each other.  

#Many to many need a middle table because you need it to connect and point to the 
#two different tables. It is a buffer. 

#Many to one the forign key is on the side of the many table it points back to primary
#key of the one table so no middle table is not needed. For example many cities to one state.

#Example State 
            #id.(PK) #name.       #Abrev
            #1.      California.  CA
            #2.      Missouri     MO 



        #City
           #id.      #Name     #State id (FK)
           #6.        SF.       1
           #7.        Sac.      1
           #8.        Stockton. 1
           #9         KC.       2   



# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# # Get the brand with the ``id`` of "ram."
# q1 = "your query here"
q1=Brand.query.filter(Brand.brand_id == 'ram').one()


# # Get all models with the name "Corvette" and the brand_id "che."
# q2 = "your query here"
q2=Model.query.filter(Model.name == 'Corvette', Model.brand_id == 'che').all() 


# # Get all models that are older than 1960.
# q3 = "your query here"
q3=Model.query.filter(Model.year > 1960).all()

# # Get all brands that were founded after 1920.
# q4 = "your query here"
q4 = Brand.query.filter(Brand.founded > 1920).all()

# # Get all models with names that begin with "Cor."
# q5 = "your query here"
q5 = Model.query.filter(Model.name.like('%Cor%')).all()

# # Get all brands that were founded in 1903 and that are not yet discontinued.
# q6 = "your query here"
q6 = Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# # Get all brands that are either 1) discontinued (at any time) or 2) founded
# # before 1950.
# q7 = "your query here " 
q7 = Brand.query.filter((Brand.discontinued.isnot(None)) |( Brand.founded < 1950)).all()

# # Get any model whose brand_id is not "for."
# q8 = "your query here"
q8 = Model.query.filter(Model.brand_id != 'for').all()



# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""
    models = Model.query.filter(Model.year == year).all()

    for model in models:
        print model.name, model.brand.name, model.brand.headquarters


get_model_info(1963)

def get_brands_summary():
    """Prints out each brand name and each model name with year for that brand
    using only ONE database query."""
    brands = Brand.query.all()

    for brand in brands:
        print brand.name
        for model in brand.models:
            print "\t", model.name, model.year

# get_brands_summary()

def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    return Brand.query.filter(Brand.name.like("%" + mystr + "%")).all()

# print search_brands_by_name("hrys")

def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    return Model.query.filter(Model.year>=start_year, Model.year<end_year).all()


# print get_models_between(1958, 1960))
