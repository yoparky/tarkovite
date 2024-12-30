import requests

def run_query(query):
    headers = {"Content-Type": "application/json"}
    response = requests.post('https://api.tarkov.dev/graphql', headers=headers, json={'query': query})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, query))


def get_all_quests():
    query = """
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
    return run_query(query)

def get_all_item_data():
    query = """
    {
        itemsByName(name: "colt m4a1") {
            name
            types
            avg24hPrice
            basePrice
            width
            height
            changeLast48hPercent
            iconLink
            link
            sellFor {
            price
            source
            }
        }
    }
    """
    return run_query(query)

def get_server_status():
    query = """
    {
        status {
            currentStatuses {
            name
            message
            status
            }
            messages {
            time
            type
            content
            solveTime
            }
        }
    }
    """
    return run_query(query)