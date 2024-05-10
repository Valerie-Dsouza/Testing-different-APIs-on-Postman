from marshmallow import Schema, fields
from sqlalchemy import Integer,String,Column,Table,MetaData,ForeignKey
from assetserver.models.EmployeeDetailsSchema import EmployeeDetailsTable


class DesignationDetailsTable:
    def __init__(self):
        self.meta = MetaData()
        self.employeed= EmployeeDetailsTable()

        self.desigd = Table(
            'designationdetails', self.meta,
            Column('desid', Integer,ForeignKey(self.employeed.employeed.c.desid), primary_key=True),
            Column('designation', String),
        )

class DesignationDetailsSchema(Schema):
    desid = fields.Integer()
    designation = fields.String()