from marshmallow import Schema, fields
from sqlalchemy import Integer,Float,String,Column,Table,MetaData
# from assetserver.packages.base import base
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()
# from assetserver.packages.session import Base

# from sqlalchemy.ext.declarative import declarative_base

# meta=MetaData()

# Base = declarative_base()




class EmployeeDetailsTable:
    def __init__(self):
        self.meta = MetaData()
        self.employeed = Table(
            'employeedetails', self.meta,
            Column('empid', Integer, primary_key=True),
            Column('fullname', String),
            Column('salary', Float),
            Column('desid', Integer)
        )
        
class EmployeeDetailsSchema(Schema):
    empid = fields.Integer()
    fullname = fields.String()
    salary = fields.Float()
    designation = fields.String()
    desid = fields.Integer()
