
from django.shortcuts import render

def register(request):
    errors = []

    if request.method == "POST":
        student_name = request.POST.get("student_name", "").strip()
        student_id = request.POST.get("student_id", "").strip()

        if not student_name:
            errors.append("Student Name cannot be blank.")

        if not student_id:
            errors.append("Student ID cannot be blank.")

        if not errors:
            return render(request, "results.html", {
                "student_name": student_name,
                "student_id": student_id,
                "major": request.POST.get("major"),
                "standing": request.POST.get("standing"),
                "languages": request.POST.getlist("languages"),
                "graduation": request.POST.get("graduation"),
            })

    return render(request, "form.html", {"errors": errors})
