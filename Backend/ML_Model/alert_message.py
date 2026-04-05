def create_alert_message(alert):

    if "rain" in alert.lower():
        suggestion = "Carry umbrella and avoid flooded roads."

    elif "heatwave" in alert.lower():
        suggestion = "Drink water and avoid outdoor activities."

    elif "wind" in alert.lower():
        suggestion = "Stay indoors and secure loose objects."

    else:
        suggestion = "Stay updated with local weather reports."

    message = f"""
⚠ WEATHER ALERT

{alert}

Safety Suggestion:
{suggestion}

Stay safe!
Weather Monitoring System
"""

    return message