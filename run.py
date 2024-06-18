from ecs import create_app,configure_logging
app = create_app('dev')
if __name__ == "__main__":
    app.run(debug=True,host = "0.0.0.0")
