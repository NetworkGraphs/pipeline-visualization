
document.addEventListener('DOMContentLoaded', () => {
    const artifacts = document.querySelectorAll('g.artifact');

    artifacts.forEach(artifact => {
        artifact.style.cursor = 'pointer'; // Make cursor a pointer to indicate clickable
        artifact.addEventListener('click', function() {
            const id = this.id;
            fetch(`/artifacts/${id}`)
                .then(response => response.blob()) // Get the file as a blob
                .then(blob => {
                    const url = window.URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = `${id}.json`; // Set the default filename for the download
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);
                    window.URL.revokeObjectURL(url);
                })
                .catch(error => console.error('Error downloading the file:', error));
        });
    });
});
