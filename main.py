def classify_request(request):
    request = request.lower()

    if "schedule" in request or "appointment" in request or "meeting" in request:
        return "Scheduling"
    elif "price" in request or "cost" in request or "quote" in request:
        return "Sales"
    elif "problem" in request or "issue" in request or "help" in request:
        return "Support"
    else:
        return "General"


def main():
    print("=== FlowPilot Core V0.1 ===")

    name = input("Client name:")
    email = input("Client email:")
    request = input("Client request:")
    urgency = input("Client urgency (low, medium, high):")

    category = classify_request(request)

    print()
    print("=== Request Summary ===")
    print("Client:", name)
    print("Email:", email)
    print("Request:", request)
    print("Category:", category)
    print("Urgency:", urgency)


if __name__ == "__main__":
    main()

