from flask import Flask
from route.trains_setup_route import trainsSetupBP
from route.trains_route import trainsBP

app=Flask(__name__)
app.register_blueprint(trainsSetupBP)
app.register_blueprint(trainsBP)


if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)


