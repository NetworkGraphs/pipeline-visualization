import { config } from '@/client_config.js';
import { Timeline } from 'vis-timeline';
import 'vis-timeline/styles/vis-timeline-graph2d.css';

async function init(){
    const containers_els = document.querySelectorAll(".visjs.timeline")
    if(containers_els.length === 0){//prevent irrelvant page execution
      return
    }

    for (const timeline_element of containers_els) {
        const data_file = timeline_element.dataset.file;
        try {
            const file_url = `${config.base}/artifacts/${data_file}`
            console.log(`fetching ${file_url}`)
            const response = await fetch(file_url);
            const data_timeline = await response.json(); // Assuming the response needs to be converted to JSON
            new Timeline(timeline_element, data_timeline, {})
        } catch (error) {
            console.error('Failed to fetch data:', error);
        }
    }
}
  
init()

