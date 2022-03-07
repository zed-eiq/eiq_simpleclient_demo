# Demo: Simple REST API client for EIQ Intelligence Center

> ⚠️ Use with caution. For demonstration purposes only.

This is a simple Python client that interacts with the
[EIQ Intelligence Center REST API](https://developers.eclecticiq.com).

## Install

Requires:

- Python >=3.7

Install this package with `pip`:

```bash
python -m pip install git+https://github.com/zed-eiq/eiq_simpleclient_demo.git
```

## Usage

This package provides the `APIClient` class
that allows you to interact with the IC REST API
through a few convenience functions.

To start working with the IC REST API,
create a `client` object:

```python
from eiq_simpleclient import APIClient

baseurl = "https://tip.example.com/api/beta"
apikey = "loremipsum"

client = APIClient(baseurl, apikey)
```

Send a GET request to a given endpoint with the `.get`
method:

``` python
# Send a GET request to the `/users/self` endpoint
current_user = client.get("users/self")
```

Send a POST request to a given endpoint with the `.post`
method:

```python
# Send a POST request to the `/entities` endpoint

## Make ID for new entity
new_id = APIClient.make_id(
  namespace="ic-playground.example.local",
  kind="indicator",
  value="172.16.1.10"
)

## Construct payload to send
payload = {
  "data": {
    "id": new_id,
    "title": "172.16.1.10",
  },
  "type": "indicator",
}

# Send POST request to `/entities` with constructed payload
created_entity = client.post("entities", payload)
```

Responses may include nested objects that are references to
another endpoint. You can follow these references using the
`.resolve` method:

```python
# Retrieve data from an arbitrary endpoint
resolved_endpoint = client.resolve("https://tip.example.com/api/beta/sources/7a8ace31-2a21-45ab-899a-15afe86cca0c?allowed_tlp=RED")
```
