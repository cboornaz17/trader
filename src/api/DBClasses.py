from mongoengine import *

STATUSES = ('created', 'certified', 'authenticated', 'expired')
ROLES = ('creator', 'certifier', 'end_user', 'admin')

class WatchedSymbol(Document):
    symbol = StringField(required=True)
    # trades = ListField(ReferenceField(Trade))
    # trades get created with symbols and then are automatically

    meta = {"db_alias": "trader", 'collection': 'symbols'}

class Candle(Document):
    open = DecimalField(min_value=0, precision=2)
    close = DecimalField(min_value=0, precision=2)
    high = DecimalField(min_value=0, precision=2)
    low = DecimalField(min_value=0, precision=2)
    volume = IntField()
    symbol = ReferenceField(WatchedSymbol)

    meta = {"db_alias": "trader", 'collection': 'candles'}

# class Trade(Document):
    # move_id = StringField(required=True, max_length=6, min_length=6)
    # buy = BooleanField(required=True)
    # open = BooleanField(required=True)
    # ul_candle = ReferenceField(Candle)

    # meta = {"db_alias": "trader", 'collection': 'trades'}


class Role(Document):
    name = StringField(required=True, choices=ROLES)
    can_create = BooleanField(required=True)
    can_print = BooleanField(required=True)
    can_certify = BooleanField(required=True)

    meta = {"db_alias": "default", 'collection': 'roles'}

class Company(Document):
    company_id = StringField(required=True, max_length=6, min_length=6)
    name = StringField(required=True)

    meta = {"db_alias": "default", 'collection': 'companies'}

class User(Document):
    user_id = StringField(required=True, max_length=7, min_length=7)
    name = StringField()
    email = EmailField()
    role = ReferenceField(Role, required=True)
    company = ReferenceField(Company)

    meta = {"db_alias": "default", 'collection': 'users'}

class Authentication(EmbeddedDocument):
    status = StringField(required=True, choices=STATUSES)
    creator = ReferenceField(User, required=True)
    printer = ReferenceField(User)
    certifier = ReferenceField(User)
    authenticator = ReferenceField(User)
    created_dt = DateTimeField(required=True)
    printed_dt = DateTimeField()
    certified_dt = DateTimeField()
    authenticated_dt = DateTimeField()

class Product(Document):
    product_id = StringField(required=True, max_length=6, min_length=6)
    name = StringField(required=True)
    company = ReferenceField(Company)

    meta = {"db_alias": "default", 'collection': 'products'}

class Unit(Document):
    code = StringField(required=True, max_length=8, min_length=8)
    authentication = EmbeddedDocumentField(Authentication)
    product = ReferenceField(Product)

    meta = {'allow_inheritance': True, "db_alias": "default", 'collection': 'units'}

class DynamicUnit(Unit):
    metadata = DictField()
