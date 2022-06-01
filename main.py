import drums
import server

if __name__ == '__main__':
    server.serverStart()
    drums.drumRun()
    # app.run(debug=True)
    server.serverStop()
