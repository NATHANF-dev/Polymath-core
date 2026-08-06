#video metrics configuration
video_duration = 45  # in seconds 
has_compelling_hook =  True  # boolean state


# Automated quality gate logic 
if video_duration < 60 and has_compelling_hook  == True:
    print("Approved for High-RPM Youtube Shorts!")
else:
    print("Rejected. Rewrite the opening hook.")