from sqlalchemy import func
from assetproto import employee_pb2
from assetserver.models.EmployeeDetailsSchema import EmployeeDetailsSchema,EmployeeDetailsTable
from assetserver.packages.base import base
import json
import csv


class EmployeeService(base):
    # def __init__(self):
    #    self.employeed = EmployeeDetailsTable()

    def CreateEmployee(self, request):
     with self.session_obj as session:
        self.get_id()
        empid = self.empcount
        employee = self.employeed.employeed.insert().values(empid=empid, fullname=request.fullname, salary=request.salary,desid=request.desid)
        session.execute(employee)
        session.commit()
        existingdata = self.redis_client.get("employee")
        if existingdata:
            existingemployees = json.loads(existingdata)
        else:
            existingemployees = []
        existingemployees.append({
            'empid': empid,
            'fullname': request.fullname,
            'salary': request.salary,
            'designation': request.designation,
            'desid': request.desid
        })
        json_data = json.dumps(existingemployees)
        self.redis_client.set("employee", json_data)
        return employee_pb2.CreateUpdateEmployeeRequest(empid=empid, fullname=request.fullname, salary=request.salary, designation=request.designation,desid=request.desid)
        
       
    def get_id(self):
        with self.session_obj as session:
            max_empid=session.query(func.max(self.employeed.employeed.c.empid)).scalar()
            print(max_empid)
            if max_empid is None:
                self.empcount = 1
            else:
                self.empcount=max_empid +1    
        return self.empcount

    def GetEmployee(self, request):
       with self.session_obj as session:
            employeejoin = session.query(self.employeed.employeed,self.desigd.desigd.c.designation).join(self.desigd.desigd,self.desigd.desigd.c.desid == self.employeed.employeed.c.desid).filter(self.employeed.employeed.c.empid == request.empid).first()
            if employeejoin:
              employee_columns = [column.key for column in self.employeed.employeed.c]
              designation_columns = ['designation']
              columns = employee_columns + designation_columns
              as_dict = dict(zip(columns, employeejoin))
              employee_data_json = EmployeeDetailsSchema().dumps(as_dict)
              employee_data_dict = json.loads(employee_data_json) 
              
              return employee_pb2.CreateUpdateEmployeeRequest(**employee_data_dict)
            else:
              return employee_pb2.CreateUpdateEmployeeRequest
             
    def UpdateEmployee(self, request):

        with self.session_obj as session:
            employee=session.query(self.employeed.employeed,self.desigd.desigd.c.designation).join(self.desigd.desigd,self.desigd.desigd.c.desid == self.employeed.employeed.c.desid).filter(self.employeed.employeed.c.empid==request.empid).first()
            if employee:
                session.execute(self.employeed.employeed.update().where(self.employeed.employeed.c.empid==request.empid).values(fullname=request.fullname,salary=request.salary,desid=request.desid))
                session.commit()
                existingdata = self.redis_client.get("employee")
                if existingdata:
                  existingemployees = json.loads(existingdata)
                  for e in existingemployees:
                      if e['empid']==request.empid:
                          e['fullname']=request.fullname
                          e['salary']=request.salary
                          e['designation']=employee.designation
                          e['desid']=request.desid
                          break
                  else:
                    existingemployees.append({
                        'empid': request.empid,
                        'fullname': request.fullname,
                        'salary': request.salary,
                        'designation': employee.designation,
                        'desid': request.desid
                    })
                self.redis_client.set("employee",json.dumps(existingemployees))
                return employee_pb2.CreateUpdateEmployeeRequest(empid=request.empid, fullname=request.fullname, salary=request.salary,designation=employee.designation,desid=request.desid)
    
            else:
                return employee_pb2.CreateUpdateEmployeeRequest()


    def DeleteEmployee(self,request):
         with self.session_obj as session:
            employee = session.query(self.employeed.employeed).filter(self.employeed.employeed.c.empid == request.empid).first()
            if employee:
                session.execute(self.employeed.employeed.delete().where(self.employeed.employeed.c.empid == request.empid))
                session.commit()
                self.redis_client.delete(f"employee:{request.empid}")
                return employee_pb2.DeleteEmployeeResponse(success=True)
            else:
                return employee_pb2.DeleteEmployeeResponse(success=False)

    def SelectAllEmployee(self, request):
        with self.session_obj as session:
            employees =session.query(self.employeed.employeed,self.desigd.desigd.c.designation).join(self.desigd.desigd,self.desigd.desigd.c.desid == self.employeed.employeed.c.desid).all()

            employee_list = []
            for employee in employees:
                
                employee_dict={
                    'empid':employee.empid,
                    'fullname':employee.fullname,
                    'salary':employee.salary,
                    'designation':employee.designation,
                    'desid':employee.desid
                }
                employee_list.append(employee_dict)
            return employee_pb2.SelectAllEmployeeResponse(employees=employee_list)

    def SelectSalaryByRange(self, request):
        with self.session_obj as session:
            
            employees = session.query(self.employeed.employeed, self.desigd.desigd.c.designation).join(self.desigd.desigd, self.desigd.desigd.c.desid == self.employeed.employeed.c.desid).filter(self.employeed.employeed.c.salary.between(request.min, request.max)).all()
            if employees:
                employee_columns = [column.key for column in self.employeed.employeed.c]
                designation_columns = ['designation']
                columns = employee_columns + designation_columns
                print(columns)
                employeelist = []
                for employee in employees:
                  as_dict = dict(zip(columns, employee))
                  print(as_dict)
                  employeelist.append(as_dict)
                return employee_pb2.SelectAllEmployeeResponse(employees=employeelist)
            else:
                return employee_pb2.CreateUpdateEmployeeRequest()


    def GetRedis(self,request):
          data = self.redis_client.get(request.key)
          print(type(data))
          if data:
              return employee_pb2.GetRedisResponse(data=data)
          else:
              return employee_pb2.GetRedisResponse(data="Unable to find key!!")
          
    def GetForm(self,request):
        content=request.content
        csvdata=[]
        contentstr=content.decode('UTF-8')
        csvreader=csv.reader(contentstr.splitlines())
        for c in csvreader:
            csvdata.append(c)
        columns=csvdata[4]
        empid = self.get_id()
        filteredlist = csvdata[5:-2]

        existingemployees = []
        for row in filteredlist:
                data = dict(zip(columns, row))
             
                data['empid'] = empid
                empid += 1
                existingemployees.append({
                        'empid': empid,
                        'fullname': data['fullname'],
                        'salary': float(data['salary']),
                        'desid': int(data['desid'])
                        })
                
        with self.session_obj as session:
            employee = self.employeed.employeed.insert().values(existingemployees)
            session.execute(employee)
            session.commit()
        existingdata = self.redis_client.get("employee")
        if existingdata:
            existing = json.loads(existingdata)
        else:
            existing = []
        existing.extend(existingemployees)
        json_data = json.dumps(existing)
        self.redis_client.set("employee", json_data)
        return employee_pb2.SelectAllEmployeeResponse(employees=existingemployees)        
       
    # def GetWebApp(self,request):
    #     user=request.user
    #     message=request.message 
    #     self.StartConnection(user,message)
    #     return employee_pb2.WebAppRequest(user=user,message=message)

    # def StartConnection(self,user,message):
    #     self.hub_connection.send("SendMessage", [user, message])
      