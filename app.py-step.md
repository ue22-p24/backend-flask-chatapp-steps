## a /api/version endpoint to get the app version

### endpoint

- We create a new endpoint `/api/version` that will return the version of
  the code (we will increment the global `VERSION` variable as we go along the
  steps)

*Note* while we're talking versions, note that in a production environment, the
API endpoints would rather be versioned like `/api/v1/...`  
so that one can define a breaking change in the API, and still support the previous one

### to try it out

```bash
http :5001/api/version
```
