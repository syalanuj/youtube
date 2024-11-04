# %%
import great_expectations as gx
print(gx.__version__)
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/anujsyal/Desktop/anuj/youtube/youtube/great_expectations_tutorial/youtube-tutorial-440608-702e9f4c100a.json"
# %%
context = gx.get_context(mode='file')

# %%
data_source_name = "flights_data_source"
bucket_or_name = "flights-dataset-yt-tutorial"
gcs_options = {}

# %%
# define a `Data Source`
data_source = context.data_sources.add_pandas_gcs(
    name="flights_data_source", bucket_or_name="flights-dataset-yt-tutorial", gcs_options=gcs_options
)

# %%
# define `Data Asset`
asset_name = "goibibo_flights_data"
gcs_prefix = "goibibo_flights_data.csv"
data_asset = data_source.add_csv_asset(name=asset_name, gcs_prefix=gcs_prefix)

# %%
# define `Batch Definition` A Batch Definition determines which records in a Data Asset are retrieved for Validation
batch_definition_name = "goibibo_flights_data_whole"
batch_definition_path = "goibibo_flights_data.csv"
batch_definition = data_asset.add_batch_definition(
    name=batch_definition_name
)
batch = batch_definition.get_batch()
print(batch.head())
# %%
# Build Expectations and add to expectation suite
suite =  context.suites.add(
    gx.ExpectationSuite(name="flight_expectation_suite")
)
expectation1 = gx.expectations.ExpectColumnValuesToNotBeNull(column="airline")
expectation2 = gx.expectations.ExpectColumnDistinctValuesToBeInSet(
    column="class",
    value_set=['economy','business']
)
suite.add_expectation(expectation=expectation1)
suite.add_expectation(expectation=expectation2)

# %%
# define `Validation Definition`: A Validation Definition is a fixed reference that links a Batch of data to an Expectation Suite.

validation_definition = gx.ValidationDefinition(
    data=batch_definition, suite=suite, name='flight_batch_definition'
)
validation_definition = context.validation_definitions.add(validation_definition)
validation_results = validation_definition.run()
print(validation_results)
# %%
# Create a Checkpoint with Actions for multiple validation_definition
validation_definitions = [
    validation_definition # can be multiple definitions
]

# Create a list of Actions for the Checkpoint to perform
action_list = [
    # This Action sends a Slack Notification if an Expectation fails.
    gx.checkpoint.SlackNotificationAction(
        name="send_slack_notification_on_failed_expectations",
        slack_token="${validation_notification_slack_webhook}",
        slack_channel="${validation_notification_slack_channel}",
        notify_on="failure",
        show_failed_expectations=True,
    ),
    # This Action updates the Data Docs static website with the Validation
    #   Results after the Checkpoint is run.
    gx.checkpoint.UpdateDataDocsAction(
        name="update_all_data_docs",
    ),
]

checkpoint = gx.Checkpoint(
    name="flight_checkpoint",
    validation_definitions=validation_definitions,
    actions=action_list,
    result_format={"result_format": "COMPLETE"},
)

context.checkpoints.add(checkpoint)

# %%
# Run checkpoint
validation_results = checkpoint.run()
print(validation_results)
