import datetime
import json
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from ...models import Student, Submission

@require_POST
@csrf_exempt
def submission(request):
    sub = json.loads(request.body.decode("utf-8"))
    print(sub)

    try:
        student = Student.objects.get(id=sub['studentId'])
    except Student.DoesNotExist:
        student = Student()
        student.first_name = sub['first_name']
        student.last_name = sub['last_name']
        student.save()
        print(student)

    try:
        already_recorded = Submission.objects.get(student=student, id=sub['exerciseId'])
    except Submission.DoesNotExist:
        print("Submission does not exists. Creating...")
        submission = Submission()
        submission.time_submitted = datetime.datetime.fromtimestamp(sub['timestamp']/1000.0)
        submission.exercise_id = sub['exerciseId']
        submission.student = student
        submission.save()
        print(submission)

    return HttpResponse('Thank you')