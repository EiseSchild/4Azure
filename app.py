import math
from flask import Flask, request




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

app = Flask(__name__)

@app.route("/numint", methods=['GET', 'POST'])
def hello_world():
    lower = request.args.get('lower')
    upper = request.args.get('upper')
    areas = numInt(float(lower), float(upper))
    areasstring = ""
    for area in areas:
        areasstring += str(area) + ", "
    return "<p>"+ areasstring + "</p>"
