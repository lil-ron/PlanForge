import uuid
from datetime import datetime
plans = {}

# Create plan function
def create_plan(plans):
    planTopic = input('What is this plan about: ')
    while planTopic == "":
        planTopic = input('It is required to name your plan: ')
    # [todo] add a while loop to create more plans

    itineraries = []
    while True:
            add_itinerary = input('What is your itinerary for this topic?: ')
            add_itinerary_description = input('What is the description for this itinerary?: ')
            itineraries.append({
                 "id": str(uuid.uuid4()),
                "itineraryName": add_itinerary,
                "itineraryDescription": add_itinerary_description
            })

            more_itineraries = input('Do you still want to add more itinerary? (y/n):  ')
            if more_itineraries == 'n':
                 break
    plan = {
        "planId": str(uuid.uuid4()),
        "planTopic": planTopic,
        "itineraries": itineraries,
        "createdOn": datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
        }
    
    plans[plan["planId"]] = plan

    
create_plan(plans)
print(plans)