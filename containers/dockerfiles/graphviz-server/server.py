from flask import Flask, request, send_file
import graphviz

app = Flask(__name__)

@app.route('/graph', methods=['POST'])
def graph():
    # Get the dot format graph from the request
    dot_string = request.data.decode()
    
    try:
        # Create a graph from the dot string
        dot = graphviz.Source(dot_string)
        # Render the graph to a file
        output_path = '/tmp/graph'
        dot.render(output_path, format='png', cleanup=True)
        
        # Send the file back
        return send_file(output_path + '.png', mimetype='image/png')
    except Exception as e:
        return str(e), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
