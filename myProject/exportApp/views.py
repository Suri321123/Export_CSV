from django.shortcuts import render
from django.http import HttpResponse
from .resources import UserResource,MemberResource
from .myFunctions import ExportData

def index(request):
	if(request.GET.get('User_CSV')):
	    user_resource = UserResource()
	    dataset = user_resource.export()
	    response = HttpResponse(dataset.csv, content_type='text/csv')
	    response['Content-Disposition'] = 'attachment; filename="UserTable.csv"'
	    return response

	elif(request.GET.get('Member_CSV')):
	    member_resource = MemberResource()
	    dataset = member_resource.export()
	    response = HttpResponse(dataset.csv, content_type='text/csv')
	    response['Content-Disposition'] = 'attachment; filename="MemberTable.csv"'
	    return response

	else:
		context={"datasetOfUser":"datasetOfUser"}
		return render(request, 'index.html', context=context)


