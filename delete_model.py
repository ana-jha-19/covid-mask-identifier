from google.cloud import automl

# TODO: fix vars as needed
project_id = "covid_mask_identifier"
model_id = "covid_id_model"

client = automl.AutoMlClient()
# Get the full path of the model.
model_full_id = client.model_path(project_id, "us-central1", model_id)
response = client.delete_model(name=model_full_id)

print("Model deleted. {}".format(response.result()))
