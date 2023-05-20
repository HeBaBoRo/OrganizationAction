# OrganizationAction

## Example files

### Example 1: ...
````yaml
---
name: Example 1

on:
  push:
    branches: [ "main" ]
  pull_request:

env:
  CONFIG_VARIABLES_FOLDER: config

jobs:
  validate-config:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
          ref: ${{ github.event.pull_request.head.ref }}
      - name: Validate config
        uses: HeBaBoRo/OrganizationAction/validateConfig@main
        with:
          to: Bobby
          
  generate:
    needs: validate-config
    if: github.event_name == 'pull_request'
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
          ref: ${{ github.event.pull_request.head.ref }}
      - name: Generate files
        uses: HeBaBoRo/OrganizationAction/generateFiles@main
        with:
          to: Bobby

  validate-generated-files:
    needs: generate
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
          ref: ${{ github.event.pull_request.head.ref }}
      - name: Generate files
        uses: HeBaBoRo/OrganizationAction/generateFiles@main
        with:
          to: Bobby
          
  push:
    needs: validate-generated-files
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
          ref: ${{ github.event.pull_request.head.ref }}
      - name: Generate files
        uses: HeBaBoRo/OrganizationAction/generateFiles@main
        with:
          to: Bobby
````