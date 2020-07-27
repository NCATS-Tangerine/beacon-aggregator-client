# kba
This is the Translator Knowledge Beacon Aggregator web service application programming interface (API) that provides integrated access to a pool of knowledge sources publishing concepts and relations through the Translator Knowledge Beacon API. This API is similar to that of the latter mentioned API with the addition of some extra informative endpoints plus session identifier and beacon indices. These latter identifiers are locally assigned numeric indices provided to track the use of specific registered beacons within the aggregator API itself.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.1.3
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

You can install from PyPI:

```sh
pip install kba
```

Then import the package:
```python
import kba
```

## Command Line Interface

This package comes with a CLI that can be used to query the Beacon Aggregator. The `--help` flag can be used with any command to see documentation.

```sh
$ kba --help
Usage: kba [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  beacons     Retrieves all beacons
  categories  Retrieves all categories
  concept     Initiates a concept query with the given search parameters
  dump        Retrieves the results of a query (by default the last query)
  kmap        Retrieves the knowledge map
  ping        Retrieves the status of a query (by default the last query)
  predicates  Retrieves all predicates
  statement   Initiates a statement query with the given search parameters
```
Initiate a concept query:
```sh
$ kba concept --keywords caffeine --categories "chemical substance" --categories pathway
Query ID:	eyUiFRZWVN5dD01VMQS1
```
Get the status of the last query posted:
```sh
$ kba ping
Last query:	eyUiFRZWVN5dD01VMQS1
Beacon 1 finished with 0 records
Beacon 2 finished with 204 records
Beacon 3 finished with 15 records
Beacon 4 has not yet returned
Beacon 5 finished with 43 records
Beacon 6 has not yet returned
Beacon 7 has not yet returned
Beacon 8 finished with 9 records
```
Get pages of records from the last query, saving it to file:
```sh
$ kba dump --page 1 --size 500 --out caffeine.json
Last query:	eyUiFRZWVN5dD01VMQS1
Saved response to caffeine.json
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import kba
from kba.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = kba.ConceptsApi()
query_id = 'query_id_example' # str | the query identifier of a concepts query previously posted by the /cliques endpoint

try:
    api_response = api_instance.get_cliques(query_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptsApi->get_cliques: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://kba.ncats.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ConceptsApi* | [**get_cliques**](docs/ConceptsApi.md#get_cliques) | **GET** /cliques/data/{queryId} |
*ConceptsApi* | [**get_cliques_query_status**](docs/ConceptsApi.md#get_cliques_query_status) | **GET** /cliques/status/{queryId} |
*ConceptsApi* | [**get_concept_details**](docs/ConceptsApi.md#get_concept_details) | **GET** /concepts/details/{cliqueId} |
*ConceptsApi* | [**get_concepts**](docs/ConceptsApi.md#get_concepts) | **GET** /concepts/data/{queryId} |
*ConceptsApi* | [**get_concepts_query_status**](docs/ConceptsApi.md#get_concepts_query_status) | **GET** /concepts/status/{queryId} |
*ConceptsApi* | [**post_cliques_query**](docs/ConceptsApi.md#post_cliques_query) | **POST** /cliques |
*ConceptsApi* | [**post_concepts_query**](docs/ConceptsApi.md#post_concepts_query) | **POST** /concepts |
*MetadataApi* | [**get_beacons**](docs/MetadataApi.md#get_beacons) | **GET** /beacons |
*MetadataApi* | [**get_concept_categories**](docs/MetadataApi.md#get_concept_categories) | **GET** /categories |
*MetadataApi* | [**get_error_log**](docs/MetadataApi.md#get_error_log) | **GET** /errorlog |
*MetadataApi* | [**get_knowledge_map**](docs/MetadataApi.md#get_knowledge_map) | **GET** /kmap |
*MetadataApi* | [**get_predicates**](docs/MetadataApi.md#get_predicates) | **GET** /predicates |
*StatementsApi* | [**get_statement_details**](docs/StatementsApi.md#get_statement_details) | **GET** /statements/details/{statementId} |
*StatementsApi* | [**get_statements**](docs/StatementsApi.md#get_statements) | **GET** /statements/data/{queryId} |
*StatementsApi* | [**get_statements_query_status**](docs/StatementsApi.md#get_statements_query_status) | **GET** /statements/status/{queryId} |
*StatementsApi* | [**post_statements_query**](docs/StatementsApi.md#post_statements_query) | **POST** /statements |


## Documentation For Models

 - [ServerBeaconConceptCategory](docs/ServerBeaconConceptCategory.md)
 - [ServerBeaconPredicate](docs/ServerBeaconPredicate.md)
 - [ServerClique](docs/ServerClique.md)
 - [ServerCliquesQuery](docs/ServerCliquesQuery.md)
 - [ServerCliquesQueryBeaconStatus](docs/ServerCliquesQueryBeaconStatus.md)
 - [ServerCliquesQueryResult](docs/ServerCliquesQueryResult.md)
 - [ServerCliquesQueryStatus](docs/ServerCliquesQueryStatus.md)
 - [ServerConcept](docs/ServerConcept.md)
 - [ServerConceptCategoriesByBeacon](docs/ServerConceptCategoriesByBeacon.md)
 - [ServerConceptCategory](docs/ServerConceptCategory.md)
 - [ServerConceptDetail](docs/ServerConceptDetail.md)
 - [ServerConceptWithDetails](docs/ServerConceptWithDetails.md)
 - [ServerConceptWithDetailsBeaconEntry](docs/ServerConceptWithDetailsBeaconEntry.md)
 - [ServerConceptsQuery](docs/ServerConceptsQuery.md)
 - [ServerConceptsQueryBeaconStatus](docs/ServerConceptsQueryBeaconStatus.md)
 - [ServerConceptsQueryResult](docs/ServerConceptsQueryResult.md)
 - [ServerConceptsQueryStatus](docs/ServerConceptsQueryStatus.md)
 - [ServerKnowledgeBeacon](docs/ServerKnowledgeBeacon.md)
 - [ServerKnowledgeMap](docs/ServerKnowledgeMap.md)
 - [ServerKnowledgeMapObject](docs/ServerKnowledgeMapObject.md)
 - [ServerKnowledgeMapPredicate](docs/ServerKnowledgeMapPredicate.md)
 - [ServerKnowledgeMapStatement](docs/ServerKnowledgeMapStatement.md)
 - [ServerKnowledgeMapSubject](docs/ServerKnowledgeMapSubject.md)
 - [ServerLogEntry](docs/ServerLogEntry.md)
 - [ServerPredicate](docs/ServerPredicate.md)
 - [ServerPredicatesByBeacon](docs/ServerPredicatesByBeacon.md)
 - [ServerStatement](docs/ServerStatement.md)
 - [ServerStatementAnnotation](docs/ServerStatementAnnotation.md)
 - [ServerStatementCitation](docs/ServerStatementCitation.md)
 - [ServerStatementDetails](docs/ServerStatementDetails.md)
 - [ServerStatementObject](docs/ServerStatementObject.md)
 - [ServerStatementPredicate](docs/ServerStatementPredicate.md)
 - [ServerStatementSubject](docs/ServerStatementSubject.md)
 - [ServerStatementsQuery](docs/ServerStatementsQuery.md)
 - [ServerStatementsQueryBeaconStatus](docs/ServerStatementsQueryBeaconStatus.md)
 - [ServerStatementsQueryResult](docs/ServerStatementsQueryResult.md)
 - [ServerStatementsQueryStatus](docs/ServerStatementsQueryStatus.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

richard@starinformatics.com
