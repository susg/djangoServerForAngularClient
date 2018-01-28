from django.http import JsonResponse
from django.shortcuts import render


# The aim of making this decorator is that the server will
# always return a proper JSON for the API called and morever
# we don't need to write whole try except block in every def

def controller_api(function):
	def wrap(request, *args, **kwargs):
		response = {}
		try:
			return function(request, *args, **kwargs)
		except Exception as e:
			print (e)
			response['success'] = False
			response['message'] = str(e)
			response['response_code'] = RESPONSE_CODE["internal_server_error"]
			return JsonResponse(response)
	wrap.__doc__ = function.__doc__
	wrap.__name__ = function.__name__
	return wrap