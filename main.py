import uuid
from datetime import datetime
plans = {}

# Create plan function
def create_plan(plans):
    planTopic = input('Give this plan a topic: ')
    while planTopic == "":
        planTopic = input('It is required to name your topic: ')
    # [todo] add a while loop to create more plans
    while True:
            add_plan = input('What is your plan for this topic?: ')
            more_plan = input('Do you still want to add more plans? (y/n):  ')

            if more_plan == 'n':
                 break
            
    plan = {
        "planId" : str(uuid.uuid4()),
        "planTopic": planTopic,
        "plans": [
            {
                "id": str(uuid.uuid4()),
                "planName": "",
                "planDescription": ""
            }
        ],
        "createdOn": datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    }

    plans[plan["planId"]] = plan

create_plan(plans)
print(plans)