import cherrypy
import functions

class Predictor(object):
	@cherrypy.expose
	def index(self):
		return file('index.html')

class PredictorWebService(object):
	exposed = True

	
	def GET(self, train, hours, wl, quota, cl):
		print hours
		return functions.getPrediction([{'train': train},{'class': cl},{'quota': quota}], int(hours), int(wl))

if __name__ == '__main__':
	conf = {
		'/': {
			'tools.sessions.on': True
		},
		'/predict': {
			'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
			'tools.response_headers.on': True,
			'tools.response_headers.headers': [('Content-type', 'text/json')]
		}
	}
	predictor = Predictor()
	predictor.predict = PredictorWebService()
	cherrypy.quickstart(predictor,'/', conf)