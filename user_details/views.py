from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import HttpResponse,JsonResponse
import json
from user_details.models import Registermodel
from django.db.models import Q

@csrf_exempt
@api_view(['POST', 'GET'])
def Register(request):
    if request.method == "POST":
        b = json.loads(request.body)
        if "id" not in b:
            obj = Registermodel.objects.create(firstname=b['firstname'],lastname=b['lastname'],
                                               userid=b['userid'],password=b['password'],mblenum=b['mblenum'],
                                               email=b['email'])
            a = [{'Message': 'Data Created'}]
            return HttpResponse(json.dumps(a))
        else:
            obj = Registermodel.objects.filter(id=b["id"]).update(firstname=b['firstname'], lastname=b['lastname'],
                                               userid=b['userid'], password=b['password'], mblenum=b['mblenum'],
                                               email=b['email'])
            a = [{'Message': 'Data Created'}]
            return HttpResponse(json.dumps(a))


from user_details.models import AddressTable

@csrf_exempt
@api_view(['POST', 'GET'])
def Address(request):
    if request.method == "POST":
        b = json.loads(request.body)
        obj = AddressTable.objects.create(line1=b['line1'],line2=b['line2'],
                                         pin=b['pin'],state=b['state'],district=b['district'],
                                         city=b['city'],status=b['status'],created_by=b['created_by'])
        a = [{'Message': 'Data Created'}]
        return HttpResponse(json.dumps(a))




from user_details.models import Contact_details

@csrf_exempt
@api_view(['POST', 'GET'])
def Contact(request):
    if request.method == "POST":
        b = json.loads(request.body)
        obj = Contact_details.objects.create(mob=b['mob'],email=b['email'],
                                           account=b['account'],status=b['status'],created_by=b['created_by'])
        a = [{'Message': 'Data Created'}]
        return HttpResponse(json.dumps(a))


from user_details.models import VendorTable

@csrf_exempt
@api_view(['POST', 'GET'])
def Vendor(request):
    if request.method == "POST":
        b = json.loads(request.body)
        obj = VendorTable.objects.create(name=b['name'],code=b['code'],
                                        gst=b['gst'],pan=b['pan'],branch=b['branch'],address_id=b['address'],
                                        contact_id=b['contact'],status=b['status'],created_by=b['created_by'])

        a = [{'Message': 'Data Created'}]
        return HttpResponse(json.dumps(a))


@csrf_exempt
@api_view(['POST', 'GET'])
def Get_Register(request):
    obj = Registermodel.objects.all()
    a = []
    for i in obj:
        b={"firstname":i.firstname,"lastname":i.lastname}
        a.append(b)
    return HttpResponse(a)


@csrf_exempt
@api_view(['POST', 'GET'])
def Get_Address(request):
    obj = AddressTable.objects.all()
    a = []
    for i in obj:
        b={"state":i.state,"district":i.district}
        a.append(b)
    return HttpResponse(a)


@csrf_exempt
@api_view(['POST', 'GET'])
def Get_Contact(request):
    obj = Contact_details.objects.all()
    a = []
    for i in obj:
        b={"mob":i.mob,"email":i.email}
        a.append(b)
    return HttpResponse(a)


@csrf_exempt
@api_view(['POST', 'GET'])
def Get_Vendor(request):
    obj = VendorTable.objects.all()
    a = []
    for i in obj:
        b={
            "name":i.name,
            "address_id": {"field1":i.address.line1,"field2":i.address.line2},
            "contact_id":i.contact.mob
        }
        a.append(b)
    return HttpResponse(a)

@csrf_exempt
@api_view(['POST', 'GET'])
def Get_ind_val(request,pk):
    obj = Registermodel.objects.get(id=pk)
    a = []
    b = {"firstname": obj.firstname, "lastname": obj.lastname}
    a.append(b)
    return HttpResponse(a)

@csrf_exempt
@api_view(['POST', 'GET'])
def Get_Address_ind(request,pk):
    obj = AddressTable.objects.get(id=pk)
    a = []
    b={"state":obj.state,"district":obj.district}
    a.append(b)
    return HttpResponse(a)

@csrf_exempt
@api_view(['POST', 'GET'])
def Get_Contact_ind(request,pk):
    obj = Contact_details.objects.get(id=pk)
    a = []
    b={"mob":obj.mob,"email":obj.email}
    a.append(b)
    return HttpResponse(a)


@csrf_exempt
@api_view(['POST', 'GET'])
def Get_Vendor_ind(request,pk):
    obj = VendorTable.objects.get(id=pk)
    a = []
    b={
            "name":obj.name,
            "address_id": {"field1":obj.address.line1,"field2":obj.address.line2},
            "contact_id":obj.contact.mob
        }
    a.append(b)
    return HttpResponse(a)


@csrf_exempt
@api_view(['POST', 'GET'])
def Index(request):
    if request.method == "POST":
        pass
    return render(request,'index.html')


@csrf_exempt
@api_view(['POST', 'GET'])
def Get_Register_m1(request):
    if request.method == "GET":
        r1 = request.GET.get("firstname")
        obj = Registermodel.objects.filter(firstname__contains=r1)
        a = []
        for i in obj:
            b={"firstname":i.firstname,"lastname":i.lastname}
            a.append(b)
        return HttpResponse(a)

@csrf_exempt
@api_view(['POST', 'GET'])
def Get_Address_m1(request):
    if request.method == "GET":
        a1 = request.GET.get("line2")
        obj = AddressTable.objects.filter(line2__contains=a1)
        a = []
        for i in obj:
            b={"state":i.state,"district":i.district}
            a.append(b)
        return HttpResponse(a)

@csrf_exempt
@api_view(['POST', 'GET'])
def Get_Contact_m1(request):
    if request.method == "GET":
        c1 = request.GET.get("email")
        c2 = request.GET.get("id")
        query = Q()
        if c1:
            query |= Q(email__contains=c1)
        if c2:
            query |= Q(id__contains=c2)
        obj = Contact_details.objects.filter(query)
        a = []
        for i in obj:
            b={"id":i.id,"email":i.email}
            a.append(b)
        return HttpResponse(a)

@csrf_exempt
@api_view(['POST', 'GET'])
def Get_Vendor_m1(request):
    if request.method == "GET":
        v1 = request.GET.get("name")
        v2 = request.GET.get("address_id")
        v3 = request.GET.get("contact_id")
        query = Q()
        if v1:
            query |= Q(name__contains=v1)
        if v2:
            query |= Q(address_id=v2)
        if v3:
            query |= Q(contact_id=v3)

        obj = VendorTable.objects.filter(query)
        a = []
        for i in obj:
            b={
                "name":i.name,
                "address_id": {"field1":i.address.line1,"field2":i.address.line2},
                "contact_id":i.contact.mob
            }
            a.append(b)
        return HttpResponse(a)

@csrf_exempt
@api_view(['DELETE'])
def Del_Register(request,pk):
    obj = Registermodel.objects.filter(id=pk).delete()
    a = []
    b = {"Message: Successfully Deleted"}
    a.append(b)
    return HttpResponse(a)

@csrf_exempt
@api_view(['DELETE'])
def Del_Address(request,pk):
    obj = AddressTable.objects.get(id=pk)
    a = []
    b = {"Message: Successfully Deleted"}
    a.append(b)
    return HttpResponse(a)

@csrf_exempt
@api_view(['DELETE'])
def Del_Contact(request,pk):
    obj = Contact_details.objects.get(id=pk)
    a = []
    b = {"Message: Successfully Deleted"}
    a.append(b)
    return HttpResponse(a)

@csrf_exempt
@api_view(['DELETE'])
def Del_Vendor(request,pk):
    obj = VendorTable.objects.get(id=pk)
    a = []
    b = {"Message: Successfully Deleted"}
    a.append(b)
    return HttpResponse(a)

@csrf_exempt
@api_view(['POST'])
def RegLogin(request):
    b = json.loads(request.body)
    obj = VendorTable.objects.filter(userName=b["userName"],Password=b["Password"])
    a = []
    if len(obj) == 0:
        a= [{"Message":"Failed"}]
    else:
        a = [{"Message":"Success"}]
    return HttpResponse(a)


