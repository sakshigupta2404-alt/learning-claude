terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  credentials = file("../terraform-key.json")
  project     = "learning-ai-0053"
  region      = "us-central1"
}

resource "google_storage_bucket" "spine_test_bucket" {
  name          = "learning-ai-0053-spine-test-bucket"
  location      = "US"
  force_destroy = true
}