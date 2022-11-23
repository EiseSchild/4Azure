import logging
import math

import azure.functions as func

def numInt(lower,upper):



    #amounts of subintervals
    NList = [10,100,1000,10000,100000,1000000]
    areas = []
    for N in NList:
        area = 0
        step = (upper - lower)/N
        start = lower + 0.5*step
        for subinterval in range(N):
            current = start + step*subinterval
            subarea = abs(math.sin(current))*step
            area += subarea
        areas.append(area)
    return areas

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    lower = float(req.params.get('lower'))
    upper = float(req.params.get('upper'))
    if not lower:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            lower = req_body.get('lower')

    if lower:
        return func.HttpResponse(f"Look at that:  {numInt(lower,upper)}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
