from marshmallow import Schema, fields
from sqlalchemy import String,Column,Table,MetaData



meta=MetaData()

class WebDetailsTable:
    def __init__(self):
        self.meta = MetaData()
        self.webd = Table(
            'webdetails', self.meta,
            Column('user', String, primary_key=True),
            Column('message', String)
        )
        
class WebDetailsSchema(Schema):
    user = fields.String()
    message = fields.String()
    