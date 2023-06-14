from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
from .serializer import TaskSerializer



# Create your views here.

@api_view(['GET'])
def get_Routes(request):
    context = {
        'home': '/api',
        'allTask': '/api/tasks',
        'createTask': '/api/tasks/create',
        'singleTask': '/api/tasks/{pk}',
        'updateTask': '/api/tasks/{pk}',
        'deleteTask': '/api/tasks/{pk}',

    }
    return Response(context)

@api_view(['GET'])
def all_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)



@api_view(['GET', 'POST'])
def create_task(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'Data saved successfully'
            })

        else:
            return Response({
                'status': False,
                'message': 'Field Mismatch'
            })
    return Response({
        'status': 'Provide Some data'
    })


@api_view(['GET', 'PUT', 'DELETE'])
def single_task(request, pk):
    if request.method == 'GET':
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(instance=task, data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'Data Updated Successfully'
            })
        else:
            return Response({
                'status': 'False',
                'message': 'Ooops!, something went wrong'
            })


    elif request.method == 'DELETE':
        task = Task.objects.get(id=pk)
        task.delete()
        return Response({
            'status': True,
            'message': 'Data Deleted Successfully'
        })