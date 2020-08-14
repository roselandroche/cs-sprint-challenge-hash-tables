#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    tickets_dict = {}
    route = []

    for ticket in tickets:
        tickets_dict[ticket.source] = ticket.destination
    
    route.append(tickets_dict["NONE"])

    last_dest = route[len(route) - 1]
    
    while last_dest is not "NONE":
        route.append(tickets_dict[last_dest])
        last_dest = route[len(route) - 1]

    return route


'''
U
Input
    list of Ticket instances

Output
    array of strings representing destinations

Task
    Order the tickets
    Start ticket has NONE as source
    Destination of ticket 1 is source of ticket 2
    Stop ticket has NONE as destination

P
Create dict
    key: source
    value: destination
Create result list
    result.append dict[NONE] to add first starting ticket
While loop
    while last item of result - when accessed in dict - does not have destination NONE:
        access dict at last item of result list
        append the value to result
return result
'''