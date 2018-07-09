from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Category, Item

engine = create_engine('sqlite:///catalog_temp_data.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Some inital data for our database
# Create dummy user
User1 = User(username="Kiran Vadakkath", email="kiranvadakath@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')  # noqa
userpw = User1.hash_password('TestPass')
User1.hashed_password = userpw
session.add(User1)
session.commit()


# Create some categories
category = Category(name="TV, Appliances, Electronics", user_id=1)
session.add(category)
session.commit()

category = Category(name="Home, Kitchen, Pets", user_id=1)
session.add(category)
session.commit()

category = Category(name="Car, Motorbike, Industrial", user_id=1)
session.add(category)
session.commit()

category = Category(name="Books", user_id=1)
session.add(category)
session.commit()

category = Category(name="Movies, Music & Video Games", user_id=1)
session.add(category)
session.commit()

category = Category(name="Gift Cards & Mobile Recharges", user_id=1)
session.add(category)
session.commit()

category = Category(name="Sports, Fitness, Bags, Luggage", user_id=1)
session.add(category)
session.commit()

category = Category(name="Men's Fashion.", user_id=1)
session.add(category)
session.commit()

# Create some items
item = Item(title='Televisions',
            description='Televisions.',
            category_id=1,
            user_id=1)
session.add(item)
session.commit()

item = Item(title='Home Entertainment Systems',
            description='Home Entertainment Systems.',
            category_id=1,
            user_id=1)
session.add(item)
session.commit()

item = Item(title='Headphones',
            description='Headphones.',
            category_id=1,
            user_id=1)
session.add(item)
session.commit()

item = Item(title='Kitchen & Dining',
            description='Kitchen & Dining.',
            category_id=2,
            user_id=1)
session.add(item)
session.commit()

item = Item(title='Kitchen Storage & Containers',
            description='Kitchen Storage & Containers',
            category_id=2,
            user_id=1)
session.add(item)
session.commit()

item = Item(title='Motorbike Accessories & Parts',
            description='Motorbike Accessories ',
            category_id=3,
            user_id=1)
session.add(item)
session.commit()

item = Item(title='Car Accessories',
            description='Car Accessory items.',
            category_id=3,
            user_id=1)
session.add(item)
session.commit()

item = Item(title='Car Electronics',
            description='Car Electronics device',
            category_id=3,
            user_id=1)
session.add(item)
session.commit()

item = Item(title='Fiction Books',
            description='Fiction Book.',
            category_id=4,
            user_id=1)
session.add(item)
session.commit()

item = Item(title='School Textbooks',
            description='School Textbook.',
            category_id=4,
            user_id=1)
session.add(item)
session.commit()

item = Item(title='Blu-ray',
            description='Blu-ray disc.',
            category_id=5,
            user_id=1)
session.add(item)
session.commit()

item = Item(title='Popular Gift Cards',
            description='Gift card.',
            category_id=6,
            user_id=1)
session.add(item)
session.commit()

item = Item(title='Birthday Gift Cards',
            description='Birthday Gift Card.',
            category_id=6,
            user_id=1)
session.add(item)
session.commit()

item = Item(title='Football',
            description='Football gear.',
            category_id=7,
            user_id=1)
session.add(item)
session.commit()

item = Item(title='Cricket',
            description='Cricket equipment.',
            category_id=7,
            user_id=1)
session.add(item)
session.commit()

item = Item(title='Strength Training',
            description='Strength Training equipment',
            category_id=7,
            user_id=1)
session.add(item)
session.commit()


print ("All test data added")
