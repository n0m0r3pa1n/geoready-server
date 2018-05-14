import numpy as np

from flask import Flask
app = Flask(__name__)

def GeoReadyFun():
    def heating(t, on_off):
        heating_power = 5
        start_period = 0.5
        if on_off == 1:
            if t < start_period:
                return t * heating_power / samples_per_hour / start_period
            else:
                return heating_power / samples_per_hour
        else:
            return 0

    samples_per_hour = 30
    h_c = -0.077 / samples_per_hour
    T_0 = 18
    T_E = 15
    target = 20
    time_to_simulate = 4

    time = np.linspace(0, time_to_simulate, time_to_simulate * samples_per_hour)
    coef = 1.2
    T = T_0
    for point in time:
        if T < target:
            T = T + h_c * (T - T_E) + heating(point, 1) * coef
        else:
            break
    time_needed = point * 60

    return str(time_needed)

@app.route("/")
def hello():
    return GeoReadyFun()

