# from django.http import HttpResponse
# from django.utils.deprecation import MiddlewareMixin
#
#
# class Middleware1(MiddlewareMixin):
#     def process_request(self,request):
#         print('middleware')
#         # ip = request.Meta.get('REMOTE_ADDR')
#         # print(ip)
#         # return HttpResponse('return')
#
#     def process_view(self,request,view_func,view_args,view_kwargs):
#         print(view_func,view_args,view_kwargs)
#         print('middleware1:process_view')
#
#     def process_response(self,request,response):
#         print('middleware1:process_response')
#         return  response
#
#     def process_tempalte_response(self,request,response):
#         print('middleware1:process_template_response')
#         return response
#
