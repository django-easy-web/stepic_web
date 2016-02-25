from cgi import parse_qs, escape

def wsgi_application(environ, start_response):
	d = parse_qs(environ['QUERY_STRING'], keep_blank_values=True)
	response_body = []
	for key in d:
		for value in d[key]:
			response_body.append(bytes("%s=%s\n" % (key, value), "UTF-8"))
	status = '200 OK'
	response_header = [('Content-type','text/plain')]
	start_response(status, response_header)
	return response_body