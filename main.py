import in_coming_requests as icreq
import FindAndSendFlightWithProblem as fas

if __name__ == '__main__':

    icreq.app.run(host='0.0.0.0', port=3162, debug=True)
