from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

db = SQLAlchemy()


class Lease( db.Model, SerializerMixin ):
    __tablename__ = 'lease_table'
    id = db.Column( db.Integer, primary_key = True )
    rent = db.Column( db.Float )
    apartment_id = db.Column( db.Integer, db.ForeignKey( 'apartments.id' ) )
    apartment_relationship = db.relationship( 'Apartment', back_populates = 'lease_a_relationship' )


    tenant_id = db.Column( db.Integer, db.ForeignKey( 'tenants.id' ) )
    tenant_relationship = db.relationship( 'Tenant', back_populates = 'lease_t_relationship' )



class Apartment( db.Model, SerializerMixin ):
    __tablename__ = 'apartment_table' 
    id = db.Column( db.Integer, primary_key = True )
    number = db.Column( db.String )

    lease_a_relationship = db.relationship( 'Lease', back_populates = 'apartment_relationship' )




class Tenant( db.Model, SerializerMixin ):
    __tablename__ = 'tenant_table'

    serialize_rules = ( '-leases.tenant', '-leases.apartment' )

    id = db.Column( db.Integer, primary_key = True )
    name = db.Column( db.String, nullable = False )
    age = db.Column( db.Integer, nullable = False  )
    lease_t_relationship = db.relationship( 'Lease', back_populates = 'tenant_relationship' )
