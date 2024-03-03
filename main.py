import server


def start():
    server.app.run(debug=True)


if __name__ == '__main__':
    start()
