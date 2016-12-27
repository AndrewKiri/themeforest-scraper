import json

themeforest_name = 'cmsmasters'
file_name = themeforest_name + '_portfolio_page_'
files_number = 3

counter = 1

obj = {
    "number of templates": 0,
    "total sales": 0,
    "total revenue": 0,
    "number of months": 7*12
}

while counter <= files_number:
    with open(file_name+str(counter)+'.json') as json_file:
        data = json.load(json_file)
        records_c = 1
        records_c_max = len(data)
        while records_c <= records_c_max:
            current_n_temp = obj["number of templates"]
            current_sales = obj["total sales"]
            current_revenue = obj["total revenue"]
            obj["number of templates"] = current_n_temp + 1
            obj["total sales"] = current_sales + int(data[str(records_c)]["sales"])
            obj["total revenue"] = current_revenue + 0.65 * int(data[str(records_c)]["sales"]) * int(data[str(records_c)]["price"])
            records_c += 1
    counter += 1

print(obj)