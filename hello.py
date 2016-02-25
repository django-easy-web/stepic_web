def wsgi_application(environ, start_response):
	response_body = []
	for key, value in environ.items():
		response_body.append(bytes("%s: %s" % (key, value), "UTF-8"))
	status = '200 OK'
	response_header = [('Content-type','text/plain')]
	start_response(status, response_header)
	return [response_body]