from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from dapp.models import Project, Issue
from dapp.serializers import ProjectSerializer, IssueSerializer, AssignSerializer


@api_view(['GET', 'POST', 'DELETE'])
def project_list(request):
    print("project_list")
    if request.method == 'GET':
        projects = Project.objects.all()
        title = request.GET.get('title', None)
        if title is not None:
            projects = projects.filter(title__icontains=title)

        projects_serializer = ProjectSerializer(projects, many=True)
        return JsonResponse(projects_serializer.data, safe=False)
    elif request.method == 'POST':
        project_data = JSONParser().parse(request)
        projects_serializer = ProjectSerializer(data=project_data)
        if projects_serializer.is_valid():
            projects_serializer.save()
            return JsonResponse(projects_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(projects_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def project_detail(request, pk):
    print("hey")
    id = pk
    try:
        project = Project.objects.get(id=id)
    except Project.DoesNotExist:
        return JsonResponse({'message': 'The project does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        print("dcdcd")
        project_serializer = ProjectSerializer(project)
        return JsonResponse(project_serializer.data)
    elif request.method == 'PUT':
        project_data = JSONParser().parse(request)
        project_serializer = ProjectSerializer(project, data=project_data)
        if project_serializer.is_valid():
            project_serializer.save()
            return JsonResponse(project_serializer.data)
        return JsonResponse(project_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        project.delete()
        return JsonResponse({'message': 'project was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'DELETE':
        count = project.objects.all().delete()
        return JsonResponse({'message': '{} projects were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def issue_list(request):
    if request.method == 'GET':
        issue = Issue.objects.all()
        title = request.GET.get('title', None)
        if title is not None:
            issue = issue.filter(title__icontains=title)

        issue_serializer = IssueSerializer(issue, many=True)
        return JsonResponse(issue_serializer.data, safe=False)
    elif request.method == 'POST':
        issue_data = JSONParser().parse(request)
        issue_serializer = IssueSerializer(data=issue_data)
        if issue_serializer.is_valid():
            issue_serializer.save()
            return JsonResponse(issue_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(issue_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def issue_detail(request, pk):
    id = pk
    try:
        issue = Issue.objects.get(id=id)
    except Issue.DoesNotExist:
        return JsonResponse({'message': 'The issue does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        issue_serializer = issueSerializer(issue)
        return JsonResponse(issue_serializer.data)
    elif request.method == 'PUT':
        issue_data = JSONParser().parse(request)
        issue_serializer = IssueSerializer(issue, data=issue_data)
        if issue_serializer.is_valid():
            issue_serializer.save()
            return JsonResponse(issue_serializer.data)
        return JsonResponse(issue_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        issue.delete()
        return JsonResponse({'message': 'issue was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'DELETE':
        count = issue.objects.all().delete()
        return JsonResponse({'message': '{} issue were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def assign(request):
    if request.method == 'POST':
        assign_data = JSONParser().parse(request)
        assign_serializer = AssignSerializer(data=assign_data)
        if assign_serializer.is_valid():
            assign_serializer.save()
            return JsonResponse(assign_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(assign_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
