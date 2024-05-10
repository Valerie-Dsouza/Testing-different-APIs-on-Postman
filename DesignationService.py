from sqlalchemy import func
from assetproto import designation_pb2
from assetserver.models.DesignationDetailsSchema import DesignationDetailsSchema,DesignationDetailsTable
from assetserver.packages.base import base
import json

class DesignationService(base):
   
    def CreateDesignation(self, request):
      with self.session_obj as session:
         designation = self.desigd.desigd.insert().values(desid=request.desid, designation=request.designation)
         session.execute(designation)
         session.commit()
        #  self.redis_client.set(f"designation:{request.desid}", DesignationDetailsSchema().dumps(designation), 120)
         existingdata=self.redis_client.get("designation")
         if existingdata:
            existingdesignation = json.loads(existingdata)
         else:
            existingdesignation = []
         existingdesignation.append(DesignationDetailsSchema().dumps({
            'desid': request.desid,
            'designation': request.designation

        }))
         json_data = json.dumps(existingdesignation)
         self.redis_client.set("designation", json_data)
      return designation_pb2.CreateDesignationRequest(desid=request.desid, designation=request.designation)

    def GetDesignation(self, request):
        with self.session_obj as session:
            designation = session.query(self.desigd.desigd).filter(self.desigd.desigd.c.desid == request.desid).first()
            if designation:
                designation_data={
                    "desid":designation.desid,
                    "designation":designation.designation
                }
                self.redis_client.set(f"employee:{request.desid}", DesignationDetailsSchema().dumps(designation_data))
                return designation_pb2.CreateDesignationRequest(**designation_data)
            else:
                return designation_pb2.CreateDesignationRequest()
    