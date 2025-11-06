# ...existing code...

resource "azurerm_resource_group" "main" {
  name     = "rg-storage-sweden-central"
  location = "Sweden Central"
}

resource "azurerm_storage_account" "main" {
  name                     = "storagesc${random_string.suffix.result}"
  resource_group_name      = azurerm_resource_group.main.name
  location                 = azurerm_resource_group.main.location
  account_tier             = "Standard"
  account_replication_type = "LRS" # Local Redundant Storage

  # Secure by default: Enable HTTPS traffic only
  enable_https_traffic_only = true

  # Deny public access by default
  allow_blob_public_access = false

  # Tags for resource management
  tags = {
    environment = "dev"
    owner       = "copilot"
  }
}

resource "random_string" "suffix" {
  length  = 6
  upper   = false
  special = false
}
