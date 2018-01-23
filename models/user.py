# -*- coding: utf-8 -*-
from bson import ObjectId


class User(Document):
    """schema and index definition for collection 'users'"""

    meta = {
        'collection': 'users',
        'index_background': True,
        'index_options': {
            'collation': {
                'locale': 'id'
            }
        },
        'indexes': [
            '#username',
            '$fullname',
            '#email',
            'isActive',
            'isDeleted',
            {
                'fields': ['-createdAt', '-updatedAt'],
                'unique': False
            },
            {
                'fields': ['#clientID'],
                'sparse': True
            },
            {
                'fields': ['#role'],
                'sparse': True
            }
        ]
    }

    __visible_role = [
        'client_admin',
        'client_user'
    ]

    posible_role = [
                       'admin'
                   ] + __visible_role

    clientID = ObjectIdField(required=True)
    username = StringField(max_length=64, required=True, unique=True)
    email = EmailField(max_length=200, required=True, unique=True)
    fullname = StringField(max_length=200, required=False, default='')
    role = StringField(max_length=200, required=True, choices=posible_role)
    passhash = StringField(max_length=200, required=True)
    last_login = LongField(required=False, default=0)
    createdAt = LongField(default=0)
    updatedAt = LongField(default=0)
    isActive = BooleanField(default=True)
    isDeleted = BooleanField(default=False)

    @classmethod
    def is_valid_role(cls, role):
        if role in cls.__visible_role:
            return True

        return False

    @classmethod
    def by_id(cls, uid):
        """get user by uid

        :param uid: user id
        :rtype: User|None
        """
        query = {
            '_id': ObjectId(uid),
            'isDeleted': False
        }

        u = cls.objects(__raw__=query).first()
        if u:
            return u

        return None

    def transform(self, with_email=False):
        """transform data to JSON friendly structure"""
        x = {
            'id': str(self.id),
            'role': self.role,
            'email': 'hidden',
            'fullname': self.fullname,
            'username': self.username,
            'isActive': self.isActive,
            'last_login': self.last_login,
            'client': self.clientID
        }

        if with_email:
            x.update({
                'email': self.email,
            })

        return x