from assetserver.packages.session import sessions
from assetserver.models.EmployeeDetailsSchema import EmployeeDetailsTable
from assetserver.models.DesignationDetailsSchema import DesignationDetailsTable
from assetserver.models.WebDetailsSchema import WebDetailsTable


class base(sessions):
    def __init__(self):
        super().__init__()
        self.session_obj = self.get_session()
        self.employeed= EmployeeDetailsTable()
        self.desigd=DesignationDetailsTable()
        self.webd=WebDetailsTable()
        self.redis_client=self.start_redis()
        self.hub_connection=self.start_hub_connection()
        