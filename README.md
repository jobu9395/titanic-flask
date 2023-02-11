* This is a simple repo showing how to serve an SKLearn ML model via Flask
* To run this project, clone the repo
* It is recommended to create a virtual environment using conda

* To create an environment with the necessary dependencies and then activate it, execute the following:
```
conda env create -f environment.yml
conda activate titanic-flask
```

* If you ever need to update the environment with a new dependency, execute the following:
```
conda env update --prefix ./env --file environment.yml  --prune
```

* The current version of this repo has the data pre-installed in the `data/` subdirectory. 

* First, execute the full notebook in `model/model,ipynb`.  This trains the random forest classifier model that will generate predictions on if a passenger survived.  Make sure your kernel is pointing to the right conda env.

* Once the model is trained, a the following model file will be generated: `model/model.pkl`.  This file will be referenced in our Flask app for inference.

* To test the app, execute the following:
```
python main.py
```

* In a separate terminal window, you can hit the endpoint with the following command (this is also stored in the `sample-request.txt` file).
```
curl -d '[
    {"Pclass": "3", "Age": "22.0", "SibSp": "1", "Parch": "0", "Fare": "70", "Sex": "male"}
]' -H "Content-Type: application/json" \
     -X POST http://localhost:5000/predict && \
    echo -e "\n -> predict OK"
```

* If everything is working correctly, this is the response you'll see:
```
{
  "label": "A person with these stats would have died",
  "prediction": 0,
  "status": 200
}

 -> predict OK
 ```

* Thanks for checking out the repo.  Feel free to fork and/or open up PRs.