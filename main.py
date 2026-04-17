import uuid
from datetime import datetime
plans = {}

# Create plan function
def create_plan(plans):
    planTopic = input('Give this plan a name: ')
    while planTopic == "":
        planTopic = input('It is required to name your plan: ')
    # [todo] add a while loop to create more plans
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