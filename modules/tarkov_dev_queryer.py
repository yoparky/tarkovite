import requests

def run_query_tasks(query):
    headers = {"Content-Type": "application/json"}
    response = requests.post('https://api.tarkov.dev/graphql', headers=headers, json={'query': query})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, query))


new_query = """
query {
  tasks {
    id
    name
    objectives {
      id
      type
    	description
      maps {
        normalizedName
      }
      ... on TaskObjectiveItem {
        item {
          name
          shortName
        }
        items {
          name
          shortName
        }
        count
        foundInRaid
      }
      ... on TaskObjectiveShoot{
        targetNames
        count
      }
    }
  }
}
"""

result = run_query_tasks(new_query)
print(result)