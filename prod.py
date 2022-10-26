from flask import Flask,json, render_template, request

@app.route("/year/<year>",methods=['GET','POST'])
def add_year(year):
    json_url = os.path.join("data","data.json")
    if request.method == 'GET':
        data_json = json.load(open(json_url))
        data = data_json['events']
        year = request.view_args['year']
        output_data = [x for x in data if x['year']==year]
        
        #render template is always looking in tempate folder
        return render_template('events.html',html_page_text=output_data)
    elif request.method == 'POST':
        year = request.form['year']

        #case sensitive, so be careful!
        id = request.form['ID']
        category = request.form['category']
        product = request.form['product']
        product_yr= { "year":year,
                    "id":id,
                    "product_category":category,
                    "product":product
                    }

        with open(json_url,"r+") as file:
            data_json = json.load(file)
            data_json["products"].append(product_yr)
            json.dump(data_json, file)
        
        #Adding text
        text_success = "Data successfully added: " + str(product_yr)
        return render_template('index.html', html_page_text=text_succe
