import uuid
plans = {}

# Create plan function
def create_plan(plans):
    planTopic = input('Give this plan a name: ')
    while planTopic == "":
        planTopic = input('It is required to name your plan: ')
    plan = {
        "planId" : str(uuid.uuid4()),
        "planTopic": planTopic
    }

    plans[plan["planId"]] = plan

create_plan(plans)
print(plans)