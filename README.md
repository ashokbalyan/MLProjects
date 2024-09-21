Complete Data Scince project 

import dagshub
dagshub.init(repo_owner='ashokbalyan', repo_name='MLProjects', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)