import requests

# URL of the graph endpoint
url = 'http://localhost:8080/graph'

# DOT language description of the graph
dot_text = """
    digraph G {
        A -> B;
        B -> C;
        C -> A;
    }
"""

# Send the DOT string as a POST request to the server
response = requests.post(url, data=dot_text)

# Check if the request was successful
if response.status_code == 200:
    # Save the image
    with open('output_graph.png', 'wb') as f:
        f.write(response.content)
    print("Graph image saved as 'output_graph.png'.")
else:
    print("Failed to generate graph:", response.text)
