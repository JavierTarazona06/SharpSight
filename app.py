import json
from data import Results
import menu

def __init__():
    #menu.startMenu()
    impDLL = Results.generalResultsImplementation()
    products = impDLL.list_data
    result = []
    if products.isEmpty():
        return json.dumps(result)
    else:
        headRef = products.head
        while headRef.next is not None:
            result.append(headRef.key.json())
            headRef = headRef.next
        result.append(headRef.key.json())
        return json.dumps(result)

print(__init__())
