from flask import Flask
import ghhops_server as hs
from area_comparison import boundrec_list, points

# register hops app as middleware
app = Flask(__name__)
hops = hs.Hops(app)

@hops.component(
    "/bound_rec",
    name="Bound_rec",
    description="Get bound rec",
    inputs= hs.HopsBoolean["Run", "Run", "Run function"
    ],
    outputs=[
        hs.HopsPoint("P", "P", "Point")
    ]
)
def hopswrap(run):
    if run:
        return boundrec_list(points)

if __name__ == "__main__":
    app.run()