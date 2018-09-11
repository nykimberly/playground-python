def greeting(name, haircolor, adjective='cool'):
    """This function greets user by their supplied name"""
    print("Hello %s! You are %s. I love your %s haircolor." \
        % (name.title(), adjective, haircolor))
