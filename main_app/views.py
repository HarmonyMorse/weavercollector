from django.shortcuts import render

weavers = [
    {
        "alias": "Spider-Man",
        "name": "Peter Parker",
        "universe": "Earth-616",
        "enemies": ["Green Goblin", "Venom"],
    },
    {
        "alias": "Spider-Woman",
        "name": "Gwen Stacy",
        "universe": "Earth-65",
        "enemies": ["Daredevil", "Vulture"],
    },
    {
        "alias": "Spider-Man",
        "name": "Miles Morales",
        "universe": "Earth-1610",
        "enemies": ["Prowler", "Doctor Octopus"],
    },
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')