from google.cloud import bigquery

# Initialize the BigQuery client
client = bigquery.Client()

# Query to retrieve the billing information
query = """
SELECT
  DISTINCT sku.id as sku_id,
  sku.description as sku_description
FROM `fr-gcp-im-billing.fr_gcp_im_billing.XXX`
ORDER BY 2
"""

# Make the query request
query_job = client.query(query)

# Fetch the results
results = query_job.result()

# Extract the sku names and sku IDs from the results
sku_info = [(row.sku_description, row.sku_id) for row in results]

# Generate a dictionary to collect sku_id as key and sku_description as value
sku_billed = {}
for sku_description, sku_id in sku_info:
    sku_billed[sku_id] = sku_description