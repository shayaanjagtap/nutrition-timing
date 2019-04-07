def detect_activity(data):
    """
    In: read a series of iwatch data
    Out: An "activity" string
    This function takes a series of iwatch data and based on whatever it says, run through a series of conditions to detect
    "an activity"
    """

    activity = ""

    if activity_1(data):
        activity = "1"

    elif activity_2(data):
        activity = "2"

    elif activity_3(data):
        activity = "3"

    return activity

def activity_1(data):

    # logic to evaluate if data qualifies as this activity
    # return True/False

    pass


def activity_2(data):

    # logic to evaluate if data qualifies as this activity
    # return True/False

    pass


def activity_3(data):

    # logic to evaluate if data qualifies as this activity
    # return True/False

    pass
