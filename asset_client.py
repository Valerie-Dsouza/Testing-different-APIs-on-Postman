import grpc
import json
from assetproto import employee_pb2
from assetproto import employee_pb2_grpc
from assetproto import designation_pb2
from assetproto import designation_pb2_grpc
from assetproto import web_pb2
from assetproto import web_pb2_grpc
from flask import Flask, jsonify, request

app = Flask(__name__)

channel = grpc.insecure_channel('localhost:50051')
stube = employee_pb2_grpc.EmployeeServiceStub(channel)
stubd = designation_pb2_grpc.DesignationServiceStub(channel)
stubw = web_pb2_grpc.WebServiceStub(channel)


@app.route('/create',methods=['POST'])
def CreateEmployeedata():
    
    req_data = request.get_json()
    fullname = req_data['fullname']
    salary = req_data['salary']
    desid = req_data['desid']

    create_request = employee_pb2.CreateUpdateEmployeeRequest(fullname=fullname, salary=salary, desid=desid)
    response = stube.CreateEmployee(create_request)
    if response:
      return jsonify({'message': 'Employee details created successfully'}), 200
    else:
            return jsonify({'error': 'Failed to fetch designation for desid: {}'.format(str(response))}), 500
    
@app.route('/createdesignation',methods=['POST'])
def CreateDesignation():
    
    req_data = request.get_json()
    desid = req_data['desid']
    designation = req_data['designation']
    request_message = designation_pb2.CreateDesignationRequest(desid=desid, designation=designation)
    response = stubd.CreateDesignation(request_message)
    if response:
        return jsonify({'message': 'Designation details created successfully'}), 200

    else:
        return jsonify({'Failed to create Designation details. Error: {}'.format(str(response))}), 500

@app.route('/get', methods=['GET'])
def GetEmployeedata():
    req_data = request.get_json()
    empid = req_data.get('empid')
    request_message_emp = employee_pb2.GetDeleteEmployeeRequest(empid=empid)
    response_emp = stube.GetEmployee(request_message_emp)
    employee_details = {
        'empid': response_emp.empid,
        'fullname': response_emp.fullname,
        'salary': response_emp.salary,
        'designation': response_emp.designation ,
        'desid': response_emp.desid
    }
    
    return jsonify({'employee_details': employee_details}), 200


@app.route('/getdesignation',methods=['GET'])
def GetDesignationdata():
    req_data=request.get_json()
    desid=req_data['desid']
    request_message = designation_pb2.GetDesignationRequest(desid=desid)
    response = stubd.GetDesignation(request_message)
    if response:
        response_dict = {

             'desid':response.desid,
             'designation': response.designation
}
        print({'designation details': response_dict})
        return jsonify({'designation': response_dict}), 200
    else:
        return jsonify({'error': 'Failed to get designation details. Error: {}'.format(str(response))}), 500

@app.route('/update',methods=['PUT'])
def UpdateEmployeedata():
    req_data = request.get_json()
    empid = req_data['empid']
    fullname = req_data['fullname']
    salary = req_data['salary']
    desid=req_data['desid']
    request_message = employee_pb2.CreateUpdateEmployeeRequest(empid=empid, fullname=fullname, salary=salary,desid=desid)
    response = stube.UpdateEmployee(request_message)
    if response:
        response_dict = {
             'empid': response.empid,
             'fullname': response.fullname,
             'salary': response.salary,
             'designation':response.designation,
             'desid':response.desid

}
        json_response=json.dumps(response_dict)
        return jsonify({'employee details': (json_response)}), 200
    else:
        return jsonify({'error': 'Failed to update employee details. Error: {}'.format(str(response))}), 500


@app.route('/delete',methods=['DELETE'])
def DeleteEmployeedata():
    req_data=request.get_json()
    empid=req_data['empid']
    request_message = employee_pb2.GetDeleteEmployeeRequest(empid=empid)
    response = stube.DeleteEmployee(request_message)
    if response:
        response_dict = {
             'empid': empid,
        }
        json_response=json.dumps(response_dict)
        return jsonify({'employee details deleted successfully': (json_response)}), 200
    else:
        return jsonify({'error': 'Failed to update employee details. Error: {}'.format(str(response))}), 500


@app.route('/selectallemployee',methods=['GET'])
def SelectAllEmployeedata():
    # req_data = request.get_json()
    request_message = employee_pb2.SelectColumnsRequest(columns=['empid','fullname','salary','designation','desid'])
    response = stube.SelectAllEmployee(request_message)
    if response:
      employeelist = [
        {
            'EmpID': employee.empid,
            'Fullname': employee.fullname,
            'Salary': employee.salary,
            'Designation': employee.designation,
            'DesID': employee.desid
        }
        for employee in response.employees
        ]
      return jsonify({'employee_details': employeelist}), 200
    else:
      return jsonify({'message': 'No employees found'}), 404

@app.route('/selectspecificcolumn', methods=['POST'])
def SelectSpecificColumn():
    req_data = request.get_json()
    columns = req_data.get('columns')
    allcolumns = ['empid', 'fullname', 'salary', 'designation','desid']
    if not all(column in allcolumns for column in columns):
        return jsonify({'error': 'Invalid column name'}), 400
    elif not columns:
        columns= allcolumns

    request_message = employee_pb2.SelectColumnsRequest(columns=columns)
    response = stube.SelectAllEmployee(request_message)

    employee_list = []
    if response.employees:
        for employee in response.employees:
            employee_data = {}
            for column in columns:
                employee_data[column]=switch_column(column,employee)
            employee_list.append(employee_data)
            
        return jsonify({'column_values': employee_list}), 200
        
    else:
           return jsonify({'error': 'Failed to retrieve column values'}), 500
    
def switch_column(column,employee):
    switcher={
    'empid':employee.empid,
    'fullname':employee.fullname,
    'salary':employee.salary,
    'designation':employee.designation,
    'desid':employee.desid
    }
    return switcher.get(column, "Invalid column name")


@app.route('/selectsalarybyrange',methods=['POST'])
def SelectSalaryByRange():
    req_data = request.get_json()
    max = req_data['max']
    min = req_data['min']
    request_message = employee_pb2.SelectSalaryByRangeRequest(min=min, max=max)
    response = stube.SelectSalaryByRange(request_message)
    print(response)

    employee_list = []
    if response.employees:
     for employee in response.employees:
         employee_data = {
            'empid': employee.empid,
            'fullname': employee.fullname,
            'salary': employee.salary,
            'designation': employee.designation,
            'desid':employee.desid
        }
         employee_list.append(employee_data)

     return jsonify({'employees within range': employee_list}), 200
    else:
     return jsonify({'message': 'No employees records found within the salary range'}), 500

@app.route('/getredis',methods=['POST'])
def GetRedisdata():
    req_data=request.get_json()
    key=req_data['key']
    request_message = employee_pb2.GetRedisRequest(key=key)
    response = stube.GetRedisData(request_message)
    if response:
     return jsonify({'data': response.data}), 200
    else:
     return jsonify({'message': 'No data found'}), 500

@app.route('/postform',methods=['POST'])
def GetFormdata():
    content=request.get_data(as_text=True) 
    contentbyte=content.encode('UTF-8')
    request_2 = employee_pb2.GetFormRequest(content=contentbyte)
    response=stube.GetForm(request_2)
    employee_list = []
    print(response.employees)
    if response.employees:
      employee_list = [{'empid': employee.empid, 'fullname': employee.fullname, 'salary': employee.salary, 'desid': employee.desid} for employee in response.employees]
      return jsonify({'employees inserted': employee_list}), 200
    else:
      return jsonify({'message': 'No employees found'}), 404

@app.route('/getwebapp',methods=['POST'])
def GetWebApp():
    req_data=request.get_json()
    user=req_data['user']
    message=req_data['message']
    request_app = web_pb2.WebAppRequest(user=user,message=message)
    response = stubw.WebApp(request_app)
    if response:
     confirmation=[{'user':user, 'message':message}]
     return jsonify(confirmation), 200
    else:
     return jsonify({'message': 'No data found'}), 500


if __name__ == '__main__':
    app.run(debug=True)
