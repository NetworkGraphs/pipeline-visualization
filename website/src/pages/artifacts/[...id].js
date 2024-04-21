import { createReadStream } from 'fs';
import {load_json} from '@/libs/utils.js'
import { config } from '@/config.js';
import {join} from 'path'

const artifacts_map = await load_json('assets/artifacts.json')

export async function GET({params}){
    try {
        const filePath = artifacts_map[params.id].filepath
        const abs_filepath = join(config.cachedir,filePath)
        console.log(`artifacts> serving '${filePath}'`)
        const stream = createReadStream(abs_filepath);
        return new Response(stream, {
            status: 200,
            headers: {'Content-Type': 'application/json'}
        });
    } catch (error) {
        return new Response('File not found', { status: 404 });
    }
}

export async function getStaticPaths(){
    const ids = Object.keys(artifacts_map)
    console.log(`serving API endpoint ${ids.length} artifacts`)
    return ids.map((id)=>({params:{id:id}}))
}
