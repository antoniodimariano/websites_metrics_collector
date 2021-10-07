variable "aiven_api_token" {}
variable "aiven_project_name" {}
variable "aiven_kafka_service_name" {}

terraform {
  required_providers {
    aiven = {
      source  = "aiven/aiven"
      version = ">= 2.0.0, < 3.0.0"
    }
  }
}

provider "aiven" {
  api_token = var.aiven_api_token
}
# Kafka service
resource "aiven_kafka" "kafka-service1" {
  project = var.aiven_project_name
  cloud_name = "google-europe-west6"
  plan = "business-4"
  service_name = var.aiven_kafka_service_name


  kafka_user_config {
    // Enables Kafka Schemas
    schema_registry = true
    kafka_version = "2.7"
    kafka {
      group_max_session_timeout_ms = 70000
      log_retention_bytes = 1000000000
    }
  }
}

resource "aiven_kafka_topic" "topic1" {
  project      = var.aiven_project_name
  service_name = var.aiven_kafka_service_name
  topic_name   = "websites_metrics"
  partitions   = 3
  replication  = 2

}
# Kafka Schema
resource "aiven_kafka_schema" "kafka-value" {
  project      = var.aiven_project_name
  service_name = var.aiven_kafka_service_name
  subject_name = "websites_metrics-value"
  schema       = <<EOT
   	  {
          "doc": "example",
          "fields": [{
              "name": "url",
              "type": "string"
          },{
              "name": "http_status",
              "type": "int"
          },
{
              "name": "elapsed_time",
              "type": "float"
          },
{
              "name": "pattern_verified",
              "type": "boolean"
          }],
          "name": "example",
          "namespace": "example",
          "type": "record"
      }
    EOT
}

resource "aiven_kafka_schema" "kafka-key" {
  project      = var.aiven_project_name
  service_name = var.aiven_kafka_service_name
  subject_name = "websites_metrics-key"
  schema       = <<EOT
   	  {
          "doc": "example",
          "fields": [{
              "name": "service_name",
              "type": "string"
          }],
          "name": "example",
          "namespace": "example",
          "type": "record"
      }
    EOT
}