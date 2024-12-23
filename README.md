# qa-backend-automation-tests

## Objective
- To do a GET request to the [URL](https://fake-json-api.mock.beeceptor.com/companies)
- Verify that response has status code 200
- Validate response body is according to JSON schema expected
- To use pytest marker 

## Configuration
```
pip install pytest requests jsonschema
```

# Run tests

```
pytest -m "marker_name"
```


