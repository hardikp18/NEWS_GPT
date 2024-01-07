from newsapi_helper import send_request

# params = {
#   "q": "microsoft"
# }


# send_request(data_dir, params)

# Example usage



data_dir = "../news"

search_parameters = {"q": "Microsoft", "pageSize": 30}  
send_request(data_dir,search_parameters)

