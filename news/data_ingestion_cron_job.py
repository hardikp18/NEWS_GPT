from newsapi_helper import send_request

# params = {
#   "q": "microsoft"
# }


# send_request(data_dir, params)

# Example usage



data_dir = "../news"

parameter= os.get.environ("PARAMETER","")

search_parameters = {"q": parameter, "pageSize": 30}  
send_request(data_dir,search_parameters)

